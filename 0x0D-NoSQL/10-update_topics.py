#!/usr/bin/env python3
""" Update Topics module. """
from typing import List
from pymongo.collection import Collection


def update_topics(mongo_collection: Collection, name: str, topics: List[str]):
    """
        Changes all topics of a school document based on the name.

        Args:
            mongo_collection: the collection to list.
            name: the name of the school to update.
            topics: the list of topics approached in school.
    """
    mongo_collection.update_one(
        {"name": name},
        {'$set': {
            "topics": topics
        }}
    )
