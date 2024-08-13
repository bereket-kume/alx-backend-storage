#!/usr/bin/env python3
"""
List all documents in python
"""


def list_all(mongo_collection):
    """
        python function that lists all documents in a collection

        param mongo_collection
        return list
    """
    data = mongo_collection.find()
    if not data:
        return []
    return data
