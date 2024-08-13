#!/usr/bin/env python3
"""
Top students
"""


def top_students(mongo_collection):
    """
    function that returns all student sorted by average score

    return the list of student from to top to lower
    """
    students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score'
                        },
                    },
                    'topics': 1
                },
            },
            {
                '$sort': {'averageScore': -1}
            }
        ]
    )
    return students
