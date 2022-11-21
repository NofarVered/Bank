from fastapi import APIRouter, Response, status, HTTPException, Request
from db import db_manager
from db.utils import UserNotFound
from models import *

router = APIRouter()


@router.get("/users/{user_id}/transactions", status_code=status.HTTP_200_OK)
def get_transactions(user_id: str):
    try:
        transactions = db_manager.get_all_transactions_by_user_id(int(user_id))
        return {"transactions": transactions}
    except UserNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )


@router.get('/users/{user_id}/balance')
def get_balance(user_id: str):
    try:
        balance = db_manager.get_user_balance(int(user_id))
        return {"balance": balance}
    except UserNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )


@router.get('/users/{user_id}/breakdown')
def get_breakdown(user_id: str):
    try:
        breakdown = db_manager.get_all_expenses_by_category(int(user_id))
        return {"breakdown": breakdown}
    except UserNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )
