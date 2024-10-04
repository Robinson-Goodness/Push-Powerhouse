# Push-Powerhouse
Overview

The Push-Powerhouse repository is set up to support a multi-team project working on different parts of a complex system. To better understand this approach, our team has embarked on the development of a chatbot using the Python programming language. Sub-teams are responsible for developing and pushing features to isolated branches, enabling branch protection, and updating the README file as required with the latest changes. This strategy ensures collaboration, proper code testing, and efficient bug fixing.

This repository consists of three branches:
1.	Main Branch (main) 
-	This is the primary branch of the repository.
-	It contains the stable, final, and production-ready code.
-	Code in this branch has been fully tested for bugs, ensuring it is ready for deployment.
-	Direct commits to this branch are restricted. All changes come in the form of pull requests which are reviewed before a merge is allowed.

2.	Develop Branch (develop) 
-	Contains the integration for different features and bug fixes.
-	Every system feature branch (e.g., user authentication feature, etc), except for chatbot features, should be branched off from here and merged back into the develop branch when the feature has been completely implemented as shown in the code below:
```
git checkout develop
git checkout -b feature/new-login-system
```
The above displays the creation of a new-login-system branch from the develop branch that is reponsible for the user login authentication code.
-	The develop branch contains most recent development changes needed for the next release.
-	When the develop branch is ready for release, it should be merged into the main branch.
3.	Chatbot Branch (chatbot)
-	A dedicated branch to the development of the chatbot functionality only.
-	This branch is used for ALL chatbot-related features and upgrades.
-	When the features and functionality are tested and deemed stable, they should be merged into the develop branch.
