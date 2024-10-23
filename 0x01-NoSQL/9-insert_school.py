#!/usr/bin/env python3
"""
 This inserts a new document in a collection
"""
import pymongo

def insert_school(mongo_collection, **kwargs):
    """
    This function inserts a document in a collection based on kwargs
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
