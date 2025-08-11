from fastapi import APIRouter,Depends,HTTPException
from models.api import (
    SuccessResponse,
    InfoResponse,
    FailureResponse
)
from database.db_functions import user_functions
from modules.middleware.middleware import jwt_token_dependecy

from models.api.api_responses import (
    StandardMessageResponse,
    UserResponse,
)

from models.api.api_requests import UserUpdateRequest

user_router = APIRouter(prefix="/users",redirect_slashes= True,dependencies=[Depends(jwt_token_dependecy)])

@user_router.get(
    "/{user_id}",
    response_model=StandardMessageResponse[UserResponse],
    name="Get User",
    summary="Retrieve user information by user ID",
    description="""
Get a user's information by their unique user ID.

- Returns user details if found.
- Example: `/user/12345`
"""
)
def get_user(user_id:int):
    try:
        fetched_user = user_functions.get_user_by_id(user_id)
        if fetched_user != None:
            response = SuccessResponse("sucessfuly retrived user info", UserResponse(
            user_id = str(fetched_user.id),
            username= str(fetched_user.username),
            first_name= str(fetched_user.first_name),
            last_name= str(fetched_user.last_name),
            ))
            return response
        else:
            raise HTTPException(
                status_code=404,
                detail= FailureResponse(
                    text="failed to find user",
                    )
                )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail= FailureResponse(
            text= "something occured",
            data=e
            ).model_dump())

@user_router.patch(
    "/{user_id}",
    response_model=StandardMessageResponse[UserResponse],
    name="Update User Partially",
    summary="Partially update user data",
    description="""
**PATCH = Partial Update**

You can send **only the fields you want to update**.

- Fields you omit will remain unchanged.
- All fields are optional but must be valid.
- Example valid payloads:
    - `{ "username": "new_username" }`
    - `{ "first_name": "John", "last_name": "Doe" }`
"""
)
def update_user(user_id: int, user_update: UserUpdateRequest):
    sucess = user_functions.update_user(
        id = user_update.user_id,
        username= user_update.username,
        email= user_update.email,
        password= user_update.password,
        first_name= user_update.first_name,
        last_name= user_update.last_name
    )
    if sucess != False:
        return SuccessResponse(text="sucessfuly updated user"),
    else:
        raise HTTPException( status_code=500, detail=FailureResponse(text="failed to update user"))

@user_router.delete(
    "/{user_id}",
    response_model=StandardMessageResponse[None],
    name="Delete User",
    summary="Delete a user by user ID",
    description="""
Delete a user from the system by their unique user ID.

- This action is irreversible.
- Example: `/user/12345`
"""
)
def delete_user(user_id: int):
    if user_functions.delete_user(user_id) != False:
        return SuccessResponse(text="üser deleted sucesfully")
    else:
        raise HTTPException(
            status_code= 500,
            detail= FailureResponse(
                "failed to delete user"
            )
        )
