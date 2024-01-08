#!/usr/bin/env python3
"""Function update_topics"""


def update_topics(mongo_collection, name, topics):
    """"""
    mongo_collection.update({"name": name}, {"$set": {"topics": topics}})
