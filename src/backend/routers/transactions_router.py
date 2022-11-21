from fastapi import APIRouter, Response, status, HTTPException, Request
from db import db_manager
from db.utils import CategoryIdNotExist, UserIdNotExist, TransactionIdNotExist
from models import *

router = APIRouter()


@router.post("transactions", status_code=status.HTTP_201_CREATED)
async def add_transaction(request: Request):
    try:
        req = await request.json()
        transaction = Transaction(**req)
        db_manager.add_transaction(transaction)
        return {"message": "add_transaction success", "id": transaction.id}
    except CategoryIdNotExist as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )
    except UserIdNotExist as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )


@router.delete("transactions/{transaction_id}", status_code=status.HTTP_200_OK)
def delete_transaction(transaction_id: str):
    try:
        db_manager.delete_transaction(transaction_id)
        return {"message": "delete_transaction success"}
    except TransactionIdNotExist as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )
