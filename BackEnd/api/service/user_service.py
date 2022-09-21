from unicodedata import name
from fastapi import HTTPException, status

from api.model.user_model import User as UserModel
from api.schema import user_schema
from api.service.auth_service import get_password_hash


def create_user(user: user_schema.UserRegister):

    get_user = UserModel.filter((UserModel.email == user.email) | (UserModel.username == user.username)).first()
    if get_user:
        msg = "Email already registered"
        if get_user.username == user.username:
            msg = "Username already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(
        username=user.username,
        email=user.email,
        name=user.name,
        surname=user.surname,
        password=get_password_hash(user.password)
    )

    db_user.save()

    return user_schema.User(
        id = db_user.id,
        username = db_user.username,
        email = db_user.email,
        name = db_user.name,
        surname = db_user.surname
    )