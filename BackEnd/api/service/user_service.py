import peewee
from fastapi import HTTPException, status
from datetime import datetime

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


def update_user(user: user_schema.User):
    try:
        user_to_udpate = UserModel.get_by_id(user.id)
        user_to_udpate.name = user.name
        user_to_udpate.surname = user.surname
        user_to_udpate.updateDate = datetime.now()
        user_to_udpate.save() 

        return user_schema.User(
            id = user_to_udpate.id,
            username = user_to_udpate.username,
            email = user_to_udpate.email,
            name = user_to_udpate.name,
            surname = user_to_udpate.surname
        )
    except Exception as ex:
        return ex
        

def delete_user(userId: int):
    try:
        user_to_delete = UserModel.get_by_id(userId)
        user_to_delete.delete_instance(recursive=True)
        return "User was deleted succesfully"
    except:
        return "The user delete failed"


def get_user_byid(userId: int):
    try:
        user = UserModel.get_by_id(userId)
        return user_schema.User(
            id = user.id,
            username = user.username,
            email = user.email,
            name = user.name,
            surname = user.surname,
            userRole = user.userRole
        )
    except Exception as ex:
        return ex


def get_all_users():
    try:
        usersList = []
        for u in UserModel.select():
            user = user_schema.User(
                id = u.id,
                username = u.username,
                email = u.email,
                name = u.name,
                surname = u.surname,
                userRole = u.userRole
            ) 
            usersList.append(user)
        return usersList
    except Exception as ex:
        return ex