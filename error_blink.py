"""
Was supposed to be a way to display error codes on the Orange Pi's built-in LED
"""

from typing import List, Dict, Tuple
from enum import Enum

class ErrorCode(Enum):
    NetworkService = 0
    NetworkDown = 1
    NetworkDns = 2
    NetworkInterface = 3

    StorageDown1 = 4
    StorageDown2 = 5
    StorageDown3 = 6

    DockerDown1 = 7
    DockerDown2 = 8
    DockerEngineDown = 9

STATUSES: Dict[ErrorCode, Tuple[bool, bool, bool, bool, bool]] = {
    ErrorCode.NetworkService:   (True, False, False, False, False),
    ErrorCode.NetworkDown:      (True, False, False, False, True),
    ErrorCode.NetworkDns:       (True, False, False, True, True),
    ErrorCode.NetworkInterface: (True, False, True, True, True),

    ErrorCode.StorageDown1:     (False, True, False, False, False),
    ErrorCode.StorageDown2:     (False, True, False, False, True),
    ErrorCode.StorageDown3:     (False, True, False, True, True),

    ErrorCode.DockerDown1:      (True, True, False, False, False),
    ErrorCode.DockerDown2:      (True, True, False, False, True),
    ErrorCode.DockerEngineDown: (True, True, False, True, True)

}


def perform_tests() -> List[ErrorCode]:
    
    return []
