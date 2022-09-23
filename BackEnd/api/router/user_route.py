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


user_router = APIRouter(prefix="/api", tags=["Users"])


@user_router.post(
    "/user/",
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
    "/login",
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
    "/me",
    response_model=user_schema.User
)
async def read_users_me(current_user: user_schema.User = Depends(auth_service.get_current_user)):
    return user_schema.User(
        id = current_user.id,
        username = current_user.username,
        email = current_user.email,
        name = current_user.name,
        surname = current_user.surname,
        userRole = current_user.userRole
    )