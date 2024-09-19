#!/usr/bin/env python3
"""Script to provide statistics about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def log_stats():
    """
    Function that provides statistics about Nginx logs stored in MongoDB.
    Counts total logs, logs by HTTP methods, and logs for specific GET requests to /status.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')  # Connect to the MongoDB server
    nginx_collection = client.logs.nginx  # Access the 'nginx' collection in the 'logs' database

    # Count total number of logs
    log_count = nginx_collection.count_documents({})
    print(f"{log_count} logs")

    # Count by HTTP methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Count the number of GET requests with path /status
    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()