# Bank Transactions Manager

## Overview

A fullstack project. This web app is a bank transactions manager that helps people track all the transactions in our bank (deposits and withdraws).

## Technologies

React hooks, fastapi and mysql.

## Endpoints

Request:

```
GET http://localhost:8000/users/0/balance
```

Response:

```
{
    "balance": 0.0
}
```

Request:

```
GET http://localhost:8000/users/0/transactions

```

Response:

```
    "transactions": [
        {
            "id": 0,
            "amount": 10.0,
            "vendor": "super yoda",
            "category_name": "Food",
            "user_id": 0
        },
        {
            "id": 1,
            "amount": -500.0,
            "vendor": "estee lauder",
            "category_name": "Healthcare",
            "user_id": 0
        },
        {
            "id": 2,
            "amount": -100.0,
            "vendor": "b pharam",
            "category_name": "Healthcare",
            "user_id": 0
        },
        {
            "id": 3,
            "amount": 200.0,
            "vendor": "laundry services",
            "category_name": "Housing",
            "user_id": 0
        },
        ...
    }
```

Request:

```
GET http://localhost:8000/users/0/breakdown

```

Response:

```
{
    "breakdown": [
        {
            "category_name": "Clothing",
            "total": -855.0
        },
        {
            "category_name": "Food",
            "total": 10.0
        },
        {
            "category_name": "Healthcare",
            "total": -600.0
        },
        {
            "category_name": "Housing",
            "total": 200.0
        },
        {
            "category_name": "Transportation",
            "total": -340.0
        }
    ]
}
```

Request:

```
DELETE http://localhost:8000/transactions/2
```

Response:

```
{
"message": "delete_transaction success"
}
```

Request:

```
http://localhost:8000/transactions
        {
        "id": 2,
        "amount": -100,
        "vendor": "b pharam",
        "category_name": "Healthcare",
        "user_id": 0
      }
```

Response:

```
{
    "message": "add_transaction success",
    "id": 2
}
```
