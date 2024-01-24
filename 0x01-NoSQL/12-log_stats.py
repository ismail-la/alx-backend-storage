#!/usr/bin/env python3
'''
Task 12's module.
a Python script that provides some stats about Nginx logs stored in MongoDB
'''

import pymongo
from pymongo import MongoClient


def prints_log_nginx_stats(mongo_collection):
    """provides some stats about Nginx logs"""
    print(f"{mongo_collection.estimated_document_count()} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    gets_number = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{gets_number} status check")


if __name__ == "__main__":
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_nginx_stats(mongo_collection)
