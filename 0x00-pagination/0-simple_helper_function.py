#!/usr/bin/env python3
"""
Simple pagination
"""

def index_range(page, page_size):
    """
    page index
    """
    return (page - 1) * page_size, page * page_size
