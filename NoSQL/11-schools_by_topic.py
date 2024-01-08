#!/usr/bin/env python3
"""Function schools_by_topic"""


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of schools having a specific topic"""
    return list(mongo_collection.find({"topic": topic}))

