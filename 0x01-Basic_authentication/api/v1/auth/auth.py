#!/usr/bin/env python3
""" Authentication Module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    A class to handle authentication operations
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a given path requires authentication

        Args:
            path (str): The path to check
            excluded_paths (List[str]): A list of paths that do not require authentication.

        Returns:
            bool: False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from a request.
        Args:
            request: The request object, optional.

        Returns:
            str: None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from a request.

        Args:
            request: The request object, optional.

        Returns:
            TypeVar('User'): None
        """
        return None
