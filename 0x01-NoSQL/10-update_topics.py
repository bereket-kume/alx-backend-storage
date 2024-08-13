#!/usr/bin/env python3
"""
update collection
"""


def update_topics(mongo_collection, name, topics):
    """
    function that changes all topics of the school
    document based on the name
    return: nothing
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
