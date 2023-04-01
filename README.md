### About the project:

+ As the name implies, a project is a book containing to-do lists. 
+ Each such list is unique within the user, and all tasks in each list are unique within the list.

### Technology stack:

[![backend](https://skillicons.dev/icons?i=python,django)](https://skillicons.dev)
![backend](https://img.shields.io/badge/DRF-red?style=flat-square&logo=Django)
[![backend](https://skillicons.dev/icons?i=postgres,js,vue,css,html)](https://skillicons.dev)


### How to run the project:
1. clone the repository.
2. install the virtual environment using requirements.txt or pyproject.toml(if you are also using poetry).
3. create a postgres database.
4. sd backend and create .env file.
  * .env file contents:
  ```
   SK=your_secret_key

   DB_NAME=database_name
   DB_USER=database_username
   DB_PASSWORD=database_password
   DB_HOST=localhost
   DB_PORT=5432
  ```
5. enter commands:
  ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 8000
  ```
   * and finally go to 
   ```
    http://127.0.0.1:8000/
   ```
