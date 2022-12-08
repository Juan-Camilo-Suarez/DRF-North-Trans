## DRF-North-Trans
### Installing and running the project
1. Create a virtual environment:\
```python -m venv venv```
2. Activate virtual environment:\
```venv\Scripts\activate.bat``` - для Windows \
```source venv/bin/activate``` - для Linux и MacOS
3. Install dependencies:\
```pip install -r requirements.txt```
4. Установка pre-commit хуков для запуска линтеров перед коммитом:\
```pre-commit install**************```
5. Install PostgreSQL from Docker:\
   ```docker-compose up -d```
6. Apply migrations to database:\
```python manage.py migrate```
7. Server start:\
```python manage.py runserver```
