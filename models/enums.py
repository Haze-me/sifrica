from enum import Enum

class MessageTypeEnum(str, Enum):
    """
    Enum ensuring standard message types for API responses.

    Benefits:
    - Prevents typos across your app.
    - Easy to extend (e.g., add 'DEBUG' if needed).
    - Improves Swagger docs clarity.
    """
    SUCCESS = "success"
    FAILURE = "failure"
    WARNING = "warning"
    INFO = "info"


class TalentLevelEnum(str,Enum):
    LEVEL_100 = "first-level"
    LEVEL_200 = "second-level"
    LEVEL_300 = "third-level"
    LEVEL_400 = "fourth-level"
    LEVEL_500 = "fifth-level"
    GRADUATE  = "graduate"


class GeoZoneEnum(str,Enum):
    NE = "north-east"
    NW = "north-west"
    NC = "north-central"
    SE = "south-east"
    SW = "south-west"
    SS = "south-south"

class GenderEnum(str,Enum):
    MALE = "male"
    FEMALE = "female"
