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
3. Create a virtual environment: python -m venv your_env_name
4. Activate the virtual environment:
   - On Windows:
  
  ```
  venv\Scripts\activate
  ```
   - On macOS and Linux:

  ```
  source venv/bin/activate
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
2. Create a new quiz by clicking on "Create Quiz" in the navigation menu.
3. Add questions to your quiz.
4. Share the quiz link with others.
5. Take quizzes by clicking on "All Quizzes" or using a shared link.
6. View quiz results.
7. See who has taken your quizzes in the "Results" section (only for logged-in users).





