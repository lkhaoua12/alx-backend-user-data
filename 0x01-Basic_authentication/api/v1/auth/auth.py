#!/usr/bin/env python3
""" the template for all authentication system implemented """
from flask import request
from typing import List, TypeVar


class Auth():
    """ base class for auth system """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check if the url require auth """
        return False

    def authorization_header(self, request=None) -> str:
        """ check the request header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ check the current user """
        return None

    
