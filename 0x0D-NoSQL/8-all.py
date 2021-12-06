#!/usr/bin/env python3
""" All module. """
from pymongo.collection import Collection


def list_all(mongo_collection: Collection):
    """
        Lists all documents in a collection.

        Args:
            mongo_collection: the collection to list.

        Return:
            The list of documents or an empty list if no documents.
    """
    return mongo_collection.find()
