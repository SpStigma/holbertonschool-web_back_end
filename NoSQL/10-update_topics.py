#!/usr/bin/env python3
"""Function update_topics"""


def update_topics(mongo_collection, name, topics):
    """function that changes all topics of a school document based on the name"""
    mongo_collection.update({"name": name}, {"$set": {"topics": topics}}, {"multi": True})
