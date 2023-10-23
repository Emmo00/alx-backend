#!/usr/bin/env python3
"""
Simple pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    page index
    """
    return (page - 1) * page_size, page * page_size
