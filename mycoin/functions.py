"""
Contains basic utility functions.
"""

import hashlib


def hash_me(string):
    """
    calculate hash of string

    args:
    string <str> : value to get hash from

    md5 -> sha1 -> sha512 -> sha384 -> sha256

    returns <string> : hashed value

    """

    # hashing the string

    md5 = hashlib.md5(string.encode()).hexdigest()
    sha1 = hashlib.sha1(md5.encode()).hexdigest()
    sha512 = hashlib.sha512(sha1.encode()).hexdigest()
    sha384 = hashlib.sha384(sha512.encode()).hexdigest()
    sha256 = hashlib.sha256(sha384.encode()).hexdigest()

    return sha256