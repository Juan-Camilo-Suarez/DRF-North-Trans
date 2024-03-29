# DRF-North-Trans [code on gitlab](https://gitlab.com/juancamilosuarez3/DRF-North-Trans)


https://user-images.githubusercontent.com/71409094/221936750-1e230874-1ff3-4e54-8029-62854f497e3f.mp4


## 1. Introduction
### 1.1 Description
The project is a logistics platform that uses Django Rest Framework, Docker, nginx, and Rest API. The platform uses an authentication and authorization system to allow users to log in based on their roles as admin, driver, and customer. Employees who have access to the platform can manage the registration process that requires users to go through an identity verification process via a personal phone call.

The platform allows users to upload requests for cargo transport and view a list of all cargo transport requests, including their own. Employees of the platform have the ability to accept or reject cargo transport requests. The platform stores all user data, including their cargo transport requests.

In addition, the platform features the functionality to view the photograph of the transport invoice and any damage photos after the transport has been completed. Users can view these photos once the transport has been completed. The driver who carries out the transport is responsible for taking the corresponding photos.

The platform uses Django Rest Framework to create a REST API that runs in a Docker container. The platform uses nginx as a web server.
### 1.2 Main features

* User authentication and registration.

* Registration with identity verification through a personal phone call, for which an application form is necessary.

* Search and filtering: users can search for clothing items by keyword.

* Users can view their purchase history. 

* Freight Forwarding Requests Database: Users can upload a freight forwarding request to the platform and view a list of all freight forwarding requests.

* Storage of users and of all cargo transport requests.
* Functionality to view the photograph of the transport invoice (and the photo of any damage) after the transport is complete.

* Swagger API.

* Docker and Nginx.

* Configuration to deploy on a private serve.
### 1.3 Limitations & Unknowns
* Swagger
* Token usage
## 2. Architecture 
### 2.1 Data Base Structure
![image](https://user-images.githubusercontent.com/71409094/221935976-6f46c200-48bc-480b-8430-4f6e7154945c.png)


## Installing and running the project
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
6. Installing pre-commit hooks to run linters before commit:\
```pre-commit install```
7. Install PostgreSQL from Docker:\
   ```docker-compose up -d```
8. Apply migrations to database:\
```python src/manage.py migrate```
9. Server start:\
```python src/manage.py runserver```

## Deploy project

1. deploy with docker-compose:\
   ```docker-compose -f docker-compose.prod.yml up -d  ```

