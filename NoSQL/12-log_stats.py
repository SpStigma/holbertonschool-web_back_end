#!/usr/bin/env python3
"""module has 2 method"""
from pymongo import MongoClient

def get_log_stats(nginx_collection):
    """get logstat"""
    total_logs = nginx_collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: nginx_collection.count_documents({"method": method}) for method in methods}

    # Status check count
    status_check_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})

    return total_logs, method_counts, status_check_count

def display_stats(total_logs, method_counts, status_check_count):
    """display stat"""
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    total_logs, method_counts, status_check_count = get_log_stats(nginx)
    display_stats(total_logs, method_counts, status_check_count)
