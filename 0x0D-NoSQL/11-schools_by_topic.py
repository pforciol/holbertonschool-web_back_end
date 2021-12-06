#!/usr/bin/env python3
""" Schools by Topic module. """
from pymongo.collection import Collection


def schools_by_topic(mongo_collection: Collection, topic: str):
    """
        Returns the list of schools having a specific topic

        Args:
            mongo_collection: the collection to list.
            topic: the topic wanted.

        Return:
            The list of schools
    """
    return mongo_collection.find({
        "topics": topic
    })
