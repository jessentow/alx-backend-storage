#!/usr/bin/env python3
"""This will give list of collection"""


def schools_by_topic(mongo_collection, topic):
    """
    This returns list of school that is having same topic
    """
    return list(mongo_collection.find({"topics": topic}))
