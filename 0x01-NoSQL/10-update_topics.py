#!/usr/bin/env python3
"""
A function that changes all topics of a school document based on the name
"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """Updates the topics of a school document based on the name.

    Args:
        mongo_collection: The pymongo collection object.
        name: The school name to update.
        topics: A list of strings representing the topics
                approached in the school.
    """

    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
