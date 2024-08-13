#!/usr/bin/env python3
"""
search tppic
"""


def schools_by_topic(mongo_collection, topic):
    """
    function that returns the list of school
    having specific topic
    
    return school
    """
    school = mongo_collection.find({"topics": topic})
    return school
