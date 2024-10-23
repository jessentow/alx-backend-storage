#!/usr/bin/env python3
"""
This changes school topics
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    This will update document with a specific attr: value
    """
    return mongo_collection.update_many(
        {
            "name": name
        },
        {
            "$set": {
                "topics": topics
            }
        })
