from fastapi import APIRouter,HTTPException
from models.api import FailureResponse,InfoResponse
from modules.middleware.token import GenerateJWT
from modules.middleware import JsonWebToken
from modules.hashing.hashing import verify_password
from database.db_functions import user_functions
from models.api.api_responses import (

    JsonWebTokenResponse,
    StandardMessageResponse,

)
from models.api.api_requests import (
    UserSignupRequest,
    UserLoginRequest
)

auth_router = APIRouter(prefix="/auth",redirect_slashes=True)



@auth_router.post("/login",
                  response_model=StandardMessageResponse[JsonWebTokenResponse],
                  name="Login Route",
                  summary="This route is to get a JWT for the users to login",
                  description="The endpoint works by passing in a user object validates the current user and returns the token as part of the response"
                  )
def login(user_login: UserLoginRequest):
    username = user_login.username
    password = user_login.password

    user  = user_functions.get_user_by_username(username=username)

    if user != None and verify_password(stored_passwprd_hash=str(user.password),password=password):
            f_user = JsonWebToken(user_id=str(user.id),email=str(user.email))
            token = GenerateJWT(f_user)
            return InfoResponse(
                text ="sucessfully logged in",
                data= JsonWebTokenResponse(token_string=token)
            )
    else:
            raise HTTPException(
                status_code=404,
                 detail = FailureResponse(
                    text = "failed to find user",
                    data=None
                ).model_dump()
            )




@auth_router.post("/signup",
                  response_model=StandardMessageResponse[JsonWebTokenResponse],
                  name="Signup Route",
                  summary="This route creates new users",
                  description="Thsi creates a user then returns a token for the user that was just created to be signed in"
                  )
def signup(user_signup: UserSignupRequest):
    r_username = user_signup.username
    r_email = user_signup.email
    r_password = user_signup.password
    created_user = user_functions.create_user(username=r_username,password= r_password,email=r_email)
    if created_user != None:
        f_user = JsonWebToken(user_id=str(created_user.id),email=str(created_user.email))
        token = GenerateJWT(f_user)
        response = InfoResponse(
        text="created new user",
        data=JsonWebTokenResponse(
            token_string=token,
            )
        )
        return response
    else:
        raise HTTPException(
            status_code= 500,
            detail= FailureResponse(
                text="failed to create user"
            ).model_dump()
        )
