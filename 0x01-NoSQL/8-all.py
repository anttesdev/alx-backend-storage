#!/usr/bin/env python3
"""
A function that lists the documents in a collection
"""

import pymongo

def list_all(mongo_collection):
    """Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of documents in the collection.
    """

    documents = mongo_collection.find()
    list_of_documents = list(documents)
    return list_of_documents
