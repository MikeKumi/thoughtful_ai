from enum import Enum

class DispatchStacks(str, Enum):
    STANDARD = 'STANDARD'
    SPECIAL = 'SPECIAL'
    REJECTED = 'REJECTED'
