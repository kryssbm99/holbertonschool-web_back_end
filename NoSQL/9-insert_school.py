#!/usr/bin/env python3
"""Inserting a new document into a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the collection using keyword arguments.
    """
    result = mongo_collection.insert_one(kwargs)  # Insert document
    return result.inserted_id  # Return the ID of the new document
