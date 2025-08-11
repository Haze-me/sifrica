from models.enums import MessageTypeEnum
from typing import Any
from pydantic import BaseModel
from models.api.api_responses import StandardMessageResponse




def objectToJson(obj: BaseModel) -> dict[str, Any]:
    """
    Converts a Pydantic model to a dictionary using aliases for JSON serialization.

    Args:
        obj: Pydantic model instance.

    Returns:
        Dictionary with alias keys for correct JSON output.
    """
    return obj.model_dump(by_alias=True)


def SuccessResponse(text: str, data: Any = None) -> StandardMessageResponse:
    """
    Generates a standardized success response.
    """
    return StandardMessageResponse(
        message_type=MessageTypeEnum.SUCCESS,
        text=text,
        data=data
    )


def FailureResponse(text: str, data: Any = None) -> StandardMessageResponse:
    """
    Generates a standardized failure response.
    """
    return StandardMessageResponse(
        message_type=MessageTypeEnum.FAILURE,
        text=text,
        data=data
    )


def InfoResponse(text: str, data: Any = None) -> StandardMessageResponse:
    """
    Generates a standardized info response.
    """
    return StandardMessageResponse(
        message_type=MessageTypeEnum.INFO,
        text=text,
        data=data
    )


def WarningResponse(text: str, data: Any = None) -> StandardMessageResponse:
    """
    Generates a standardized warning response.
    """
    return StandardMessageResponse(
        message_type=MessageTypeEnum.WARNING,
        text=text,
        data=data
    )
