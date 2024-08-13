#!/usr/bin/env python3

def list_all(mongo_collection):
    """
        python function that lists all documents in a collection
    """
    data = mongo_collection.find()
    if not data:
        return []
    return data
