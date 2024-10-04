import json
import textwrap
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
        return data


def save_to_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_exact_match(user_input: str, questions: list[str]):
    user_input_lower = user_input.lower()  # Convert input to lowercase
    # Check if a lowercase version of the input matches any question (also converted to lowercase)
    return next((q for q in questions if q.lower() == user_input_lower), None)


def find_best_match(user_input: str, questions: list[str]):
    # Use difflib to find the closest match if no exact match is found
    matches = get_close_matches(user_input, [q.lower() for q in questions], n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_answer(question: str, knowledge_base: dict):
    for q in knowledge_base['questions']:
        if q['question'].lower() == question.lower():
            return q['answer']


def chatbot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    # Define the terminal width for text wrapping (use 70 characters, adjust if needed)
    terminal_width = 70

    while True:
        user_question: str = input('You: ')

        if user_question == 'quit':
            break

        # Step 1: Check for an exact match
        exact_match: str | None = find_exact_match(user_question, [q['question'] for q in knowledge_base['questions']])

        if exact_match:
            answer = get_answer(exact_match, knowledge_base)
            wrapped_answer = textwrap.fill(answer, width=terminal_width)  # Wrap the response to fit terminal width
            print(f'Bot: {wrapped_answer}')
        else:
            # Step 2: If no exact match, look for the best match
            best_match: str | None = find_best_match(user_question, [q['question'] for q in knowledge_base['questions']])

            if best_match:
                # Ask user if the best match was accurate
                answer = get_answer(best_match, knowledge_base)
                wrapped_answer = textwrap.fill(answer, width=terminal_width)
                print(f'Bot: I found something similar to your question. Did you mean:\n"{best_match}"')
                user_confirmation = input("Type 'yes' if this is correct, or 'no' if it isn't: ").lower()

                if user_confirmation == 'yes':
                    print(f'Bot: {wrapped_answer}')
                else:
                    # Step 3: If the best match wasn't accurate, ask the user to teach the bot
                    print(f'I don\'t know the exact answer, can you teach me?')
                    new_answer: str = input('Type your answer here or "skip" to skip: ')

                    if new_answer != "skip":
                        knowledge_base['questions'].append({'question': user_question, 'answer': new_answer})
                        save_to_knowledge_base('knowledge_base.json', knowledge_base)
                        print('Bot: Thank you, I learned a new response.')
            else:
                # Step 4: If no close match found, ask the user to provide an answer
                print(f'I don\'t know the answer, can you teach me?')
                new_answer: str = input('Type your answer here or "skip" to skip: ')

                if new_answer != "skip":
                    knowledge_base['questions'].append({'question': user_question, 'answer': new_answer})
                    save_to_knowledge_base('knowledge_base.json', knowledge_base)
                    print('Bot: Thank you, I learned a new response.')


if __name__ == '__main__':
    chatbot()
