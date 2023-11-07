# Discussion Forum App (Django-Reditt Clone)
## Project Description
This project is a Python Django-based discussion forum application, inspired by the popular platform Reddit. It provides a platform for users to engage in discussions, share ideas, and express their thoughts on various topics. The application is built using Python, Django, and Django Rest Framework and utilizes a SQL Lite database for data storage.

## Key Features:
- User Registration and Authentication: Users can register, create profiles, and securely authenticate to access the platform.
- Posts and Comments: Users can create posts within subreddits, comment on posts, and upvote or downvote content.
- Sorting and Filtering: The platform offers options to sort and filter discussions by popularity, date, and relevance.
- User Interaction: Users can follow and message other users, enhancing the community experience.

## Technologies Used:
- Python: The primary programming language for backend development.
- Django: A high-level Python web framework for rapid development.
- SQL Lite: A lightweight and efficient database system for data storage.

This project serves as a versatile and engaging platform for online discussions and showcases the power of Python and Django in web application development. Whether you're interested in contributing to the open-source community or exploring the development of discussion forums, this project is a great starting point. Feel free to explore the code, suggest improvements, or use it as a reference for your own projects.

## Project Setup
1. Clone github repository
```sh
git clone <project> 
```
2. Create virtual envirnoment
Windows:
```sh
    python -m venv <env name>
```
Linux/Unix:
```sh
    pip install virtualenv
    virtualenv <env name>
```
3. Activate virtual envirnoment
Windows:
```sh
<env name>/scripts/activate
```
Linux/Unix:
```sh
<env name>/bin/activate
```
4. Run migrations:
```sh
python manage.py makemigrations
python manage.py migrate
```
5. Run development server on port
```sh
python manage.py runserver
```
