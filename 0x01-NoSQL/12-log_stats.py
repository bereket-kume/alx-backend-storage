#!/usr/bin/env python3
"""
Python script to provide stats about Nginx logs stored in MongoDB
"""


from pymongo import MongoClient


def log_stats():
    """
    Function to print stats about Nginx logs
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_coll = client.logs.nginx
    
    total_logs = log_coll.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = log_coll.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = log_coll.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    client.close()

if __name__ == "__main__":
    log_stats()
