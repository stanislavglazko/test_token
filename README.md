# CRUD users via JWT

<a href="https://codeclimate.com/github/stanislavglazko/test_token/maintainability"><img src="https://api.codeclimate.com/v1/badges/b7b30af125ffdfe678d1/maintainability" /></a>

<a href="https://codeclimate.com/github/stanislavglazko/test_token/test_coverage"><img src="https://api.codeclimate.com/v1/badges/b7b30af125ffdfe678d1/test_coverage" /></a>

[![Build Status](https://travis-ci.com/stanislavglazko/test_token.svg?branch=main)](https://travis-ci.com/stanislavglazko/test_token)

My tool makes CRUD users via JWT.

### How to install
Python3 should be already installed.

1) clone the repo
2) use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
    ```
    pip install -r requirements.txt
    ```
3) add .env file in the directory of the tool:
    ```
    SECRET_KEY=<your_secret_key>
    ```

### How to use
1) Create user: 
    ```
    POST /auth/users/  
    data = {'username': 'username',
            'password': 'password',
            'email': 'email',
            'city': 'city' (CharField, max_length=30),
            'is_administrator': True/False(default)}
    ```
2) Create JWT token: 
    ```
    POST /auth/jwt/create/  
    data = {'username': 'username', 'password': 'password'}
    ```
3) Get info about user via token:
    ```
    GET /auth/users/me/  'Bearer ' + token
    ```
4) Update user:
    ```
    PUT /accounts/profile/id 'Bearer ' + token
    data = {'city': 'city', 'is_administrator': True/False}
    ```
5) Delete user:
    ```
    DELETE /accounts/profile/id 'Bearer ' + token
    ```
6) Show all users:
    ```
    GET /accounts/all-profiles 'Bearer ' + token
    ```