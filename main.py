import json
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data : dict = json.load(file)
        return data


def save_to_knowledge_base(file_path:str, data:dict):
    with open(file_path, 'w') as file:
        json.dump(data,file,indent=2)


def find_best_match (user_input:str, question: list[str]):
    matches : list = get_close_matches(user_input,question,n=1,cutoff=0.6)
    return matches[0] if matches else None

def get_answer (question: str , knowledge_base: dict):
    for q in knowledge_base['questions']:
        if q['question'] == question:
            return q['answer']


def chatbot():
    knowledge_base:dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_question:str = input('You: ')

        if user_question == 'quit':
            break

        best_match : str | None = find_best_match(user_question, [q['question'] for q in knowledge_base['questions']])

        if best_match :
            answer = get_answer(best_match,knowledge_base)
            print(f'Bot: {answer}')
        else :
            print(f'I Don\'t know the answer can you teach me')
            new_answer:str = input('type your answer here or "skip" to skip: ')

            if new_answer != "skip":
                knowledge_base['questions'].append({'question': user_question, 'answer': new_answer})
                save_to_knowledge_base('knowledge_base.json', knowledge_base)
                print('Bot : thank you I learned a new response')


if __name__ == '__main__':
    chatbot()