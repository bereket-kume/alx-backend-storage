#!/usr/bin/env python3
"""
Insert new Document
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a
    collection based on arguments
    
    return id of new document
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
