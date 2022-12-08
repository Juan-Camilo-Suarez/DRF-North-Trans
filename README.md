## DRF-North-Trans
### Installing and running the project
1. Create a virtual environment:\
```python -m venv venv```
2. Activate virtual environment:\
```venv\Scripts\activate.bat``` - для Windows \
```source venv/bin/activate``` - для Linux и MacOS
3. Install poetry:\
```pip install poetry  ```
4. Enter the virtual environment:\
   ``` poetry shell  ```
5. Install dependencies:\
   ``` poetry install  ```
6. Установка pre-commit хуков для запуска линтеров перед коммитом:\
```pre-commit install**************```
7. Install PostgreSQL from Docker:\
   ```docker-compose up -d```
8. Apply migrations to database:\
```python manage.py migrate```
9. Server start:\
```python manage.py runserver```
