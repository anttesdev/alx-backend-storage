#!/usr/bin/env python3
"""
 a function that returns the list of school having a specific topic
 """


import pymongo


def schools_by_topic(mongo_collection, topic):
    """Returns a list of schools that have a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic: The topic to search for.

    Returns:
        A list of school documents that have the specified topic.
    """

    return list(mongo_collection.find({"topics": topic}))
