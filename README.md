# QuizApp
###### This is a documentation regarding the project I've created.

## Table of contents

 - [Project Overview](#project-overview)
 - [Features](#features)
 - [Tools](#tools)
 - [Installation](#installation)
 - [Usage](#usage)


### Project Overview

QuizApp is a Python-Django-based web application that allows users to create, share, and take quizzes. It provides a platform for users to test their knowledge on various topics and share quizzes with others.

![Screenshot (67)](https://github.com/user-attachments/assets/75275698-61dd-40df-852e-200039bd579a)


### Features

- User Authentication: Register, log in, and log out functionality;
- Quiz Creation: Logged-in users can create quizzes with multiple-choice questions;
- Quiz Taking: Users (both logged-in and anonymous) can take quizzes and see their results;
- Results Tracking: Quiz creators can see who has taken their quizzes;
- Quiz Sharing: Users can share quiz links with others.

### Tools

- Python 3.x
- Django 3.x
- HTML/CSS
- Bootstrap 5
- SQLite (default Django database)

### Installation

1. Clone the repository: git clone https://github.com/your-username/quizapp.git
2. Navigate to the project directory: cd quizapp
3. Create a virtual environment: python -m venv env_name
4. Activate the virtual environment:
   - On Windows:
  
  ```
  source env_name\Scripts\activate
  ```
   - On macOS and Linux:

  ```
  source env_name/bin/activate
  ```

5. Install the required packages:
   ```
    pip install -r requirements.txt
   ```
6. Run database migrations:
   ```
   python manage.py migrate
   ```
7. Create a superuser (admin):
   ```
   python manage.py createsuperuser
   ```
8. Start the development server:
   ```
   python manage.py runserver
   ```
9. Open a web browser and go to `http://localhost:8000` to view the application.

### Usage

1. Register a new account or log in with existing credentials.
   
![register form](https://github.com/user-attachments/assets/37153344-de10-477d-a468-4c22b250aad2)

![login form](https://github.com/user-attachments/assets/4ad1d72a-24d9-4cd4-ac8f-92979ee7d410)


2. Create a new quiz by clicking on "Create Quiz" in the navigation menu.

![create quiz](https://github.com/user-attachments/assets/2828cec5-accf-47c2-a4cf-7068215265ce)


3. Add questions to your quiz.

![options ](https://github.com/user-attachments/assets/cd884a38-3f8f-49d7-b9f0-a0561504a79e)

4. Share the quiz link with others.

![quiz review](https://github.com/user-attachments/assets/f848cf2d-d51f-463d-a2b1-db80a6711b57)

![quiz link](https://github.com/user-attachments/assets/8dc791c2-c6a7-497e-bb58-13d6d2995684)

   
5. Take quizzes by clicking on "All Quizzes" or using a shared link.


![all quizzes](https://github.com/user-attachments/assets/de3ee2fc-1196-4bd3-a229-e1d1ad456c60)

![quiz taking](https://github.com/user-attachments/assets/4c5596b5-55d4-4e37-9aaa-2512e399e96a)


6. View quiz results.

![quiz result](https://github.com/user-attachments/assets/f6e9e74d-0bb5-4829-a336-5408c5856145)

   
7. See who has taken your quizzes in the "Results" section (only for logged-in users).


![quizzes with takers](https://github.com/user-attachments/assets/c2fb97b4-3b4d-4e53-95dd-2c59432d1a94)



