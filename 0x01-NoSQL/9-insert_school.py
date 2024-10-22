#!/usr/bin/env python3
"""
a function that inserts a new document in to a collection
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into a MongoDB collection
        based on keyword arguments.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Keyword arguments representing the document.

    Returns:
        The _id of the newly inserted document.
    """

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
