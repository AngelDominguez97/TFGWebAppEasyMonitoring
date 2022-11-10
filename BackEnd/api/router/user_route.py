from fastapi.security import OAuth2PasswordRequestForm
from api.schema.token_schema import Token

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from api.schema import user_schema
from api.service import user_service
from api.service import auth_service

from api.utils.db import get_db

from typing import List


user_router = APIRouter(prefix="/api", tags=["Users"])


@user_router.post(
    "/user/signin",
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Create a new user"
)
def create_user(user: user_schema.UserRegister = Body(...)):
    """
    ## Create a new user in the app

    ### Args
    The app can recive next fields into a JSON
    - email: A valid email
    - username: Unique username
    - password: Strong password for authentication

    ### Returns
    - user: User info
    """
    return user_service.create_user(user)


@user_router.post(
    "/user/update",
    status_code=status.HTTP_200_OK,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Update an existing user"
)
def update_user(user: user_schema.User = Body(...)):
    """
    ## Update an existing user in the app

    ### Args
    The app can recive next fields into a JSON
    - email: A valid email
    - username: Unique username
    - name: Name of the user
    - surname: surname of the user 
    - userRole: the role of the user (user)

    ### Returns
    - user: User info
    """
    return user_service.update_user(user)


@user_router.delete(
    "/user/delete{userId}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Delete an existing user by its id"
)
def update_user(userId: str):
    """
    ## Delete an existing user in the app by its id

    ### Args
    The app can recive next fields into a JSON
    - id: The id of the user to be deleted

    ### Returns
    - info about how worked the delete
    """
    return user_service.delete_user(userId)


@user_router.get(
    "/user{userId}",
    status_code=status.HTTP_200_OK,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Get one user registered in the database"
)
def get_user_byid(userId: int):
    """
    ## Get one user registered in the app by its id

    ### Args
    - id: The id of the user

    ### Returns
    - The user data
    """
    return user_service.get_user_byid(userId)


@user_router.get(
    "/user/allusers",
    status_code=status.HTTP_200_OK,
    response_model=List[user_schema.User],
    dependencies=[Depends(get_db)],
    summary="Get all users in the database"
)
def get_all_users():
    """
    ## Get all users registered in the app

    ### Args
    NONE

    ### Returns
    - Json with all the users in the app
    """
    return user_service.get_all_users()


@user_router.post(
    "/user/login",
    response_model=Token
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    ## Login for access token

    ### Args
    The app can receive next fields by form data
    - username: Your username or email
    - password: Your password

    ### Returns
    - access token and token type
    """
    access_token = auth_service.generate_token(form_data.username, form_data.password)
    return Token(access_token=access_token, token_type="bearer")

@user_router.get(
    "/user/me",
    response_model=user_schema.User
)
async def read_users_me(current_user: user_schema.User = Depends(auth_service.get_current_user)):
    """
    ## Get data from actual user logged

    ### Args
    The app can recive next fields into a JSON
    - current_user: the current user logged in the front

    ### Returns
    - user: User info
    """
    
    return user_schema.User(
        id = current_user.id,
        username = current_user.username,
        email = current_user.email,
        name = current_user.name,
        surname = current_user.surname,
        userRole = current_user.userRole
    )