# module for carrying out hashing tasks

import os
from hashlib import sha256

def hash_api_key(ak: str) -> str:
    """
        calculate the sha256 hash of a given api key
    """
    hashed = sha256(ak.encode())
    return hashed.hexdigest()
    