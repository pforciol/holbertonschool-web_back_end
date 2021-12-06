#!/usr/bin/env python3
""" Insert School module. """
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs):
    """
        Insert a new document in a collection based on **kwargs.

        Args:
            mongo_collection: the collection to list.
            **kwargs: optional arguments with school data.

        Return:
            The new _id.
    """
    return mongo_collection.insert_one({**kwargs}).inserted_id
