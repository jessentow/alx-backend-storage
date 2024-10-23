#!/usr/bin/env python3
"""
This will List all documents in Python
"""
import pymongo


def list_all(mongo_collection):
    """
    The function to list all doc in a collection
    """
    if mongo_collection is not None:
        return list(mongo_collection.find())
    else:
        return []           
