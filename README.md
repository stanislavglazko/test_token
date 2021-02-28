# CRUD users via token

<a href="https://codeclimate.com/github/stanislavglazko/test_token/maintainability"><img src="https://api.codeclimate.com/v1/badges/b7b30af125ffdfe678d1/maintainability" /></a>

[![Build Status](https://travis-ci.com/stanislavglazko/test_token.svg?branch=main)](https://travis-ci.com/stanislavglazko/test_token)

My tool makes CRUD users via token.
You create user, my tool automatically creates UserProfile for you.
You can read, update or delete UserProfile.
If you delete UserProfile, user will be deleted too.

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
            'email': 'email'}
    ```
2) Login and get token:
    ```
    POST /auth/token/login/
    data = {'username': 'username', 'password': 'password'}
    ```
3) Get info about user via token:
    ```
    GET /auth/users/me/  'Token ' + token
    ```
4) Get info about UserProfile via token:
    ```
    GET accounts/accounts/id  'Token ' + token
    ```
5) Update UserProfile:
    ```
    PUT /accounts/accounts/id/ 'Token ' + token
    data = {'city': 'city', 'is_administrator': True/False}
    ```
6) Delete UserProfile and user:
    ```
    DELETE /accounts/accounts/id/ 'Token ' + token
    ```
 7) Show all UserProfiles:
    ```
    GET /accounts/accounts/ 'Token ' + token
    ```
