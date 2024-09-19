#!/usr/bin/env python3
"""Python function that lists all documents in a MongoDB collection."""


def list_all(mongo_collection):
    """
    List all documents in the given MongoDB collection.
    """
    documents = mongo_collection.find()  # Retrieve all documents
    return list(documents)  # Convert cursor to a list and return
