#!/usr/bin/env python3
""" the template for all authentication system implemented """
from flask import request
from typing import List, TypeVar



class Auth():
    """ base class for auth system """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if the URL requires authentication."""
        if path is None:
            return True
        if not excluded_paths or not path.strip():
            return True

        for excluded_path in excluded_paths:
            if path == excluded_path or path + '/' == excluded_path:
                return False

        return True


    def authorization_header(self, request=None) -> str:
        """ check the request header """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """ check the current user """
        return None
