#!/usr/bin/env python3
"""Function to return a list of schools by a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have a specific topic in their "topics".
    """
    specific_topic_list = mongo_collection.find({"topics": topic})
    return list(specific_topic_list)
