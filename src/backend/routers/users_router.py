from fastapi import APIRouter, Response, status, HTTPException, Request
from db import db_manager
from db.utils import CategoryIdNotExist, UserIdNotExist, TransactionIdNotExist
from ..models import *

router = APIRouter()


@router.get('/users/{user_id}/balance')
def get_balance(user_id: str):
    try:
        balance = db_manager.get_user_balance(int(user_id))
        return {"balance": balance}
    except UserIdNotExist as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )


@router.get('/users/{user_id}/breakdown')
def get_breakdown(user_id: str):
    breakdown = db_manager.get_all_expenses_by_category(int(user_id))
    return {"breakdown": breakdown}