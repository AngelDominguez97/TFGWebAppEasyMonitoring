from enum import Enum

class ChooseMinutes(str, Enum):
    min1 = "1"
    min5 = "5"
    min15 = "15"

class ChooseSnmpVersion(str, Enum):
    v2c = "v2c"
    v3 = "v3"