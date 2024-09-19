#!/usr/bin/env python3
"""Function that updates the topics of a school in MongoDB."""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the school's name.
    """
    return mongo_collection.update_many(
        {"name": name},  # Filter by school name
        {"$set": {"topics": topics}}  # Set the new topics
    )
