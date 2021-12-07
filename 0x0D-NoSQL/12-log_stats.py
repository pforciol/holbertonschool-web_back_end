#!/usr/bin/env python3
""" Log Stats module. """
from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)
db = client.logs

if __name__ == "__main__":
    print("{} logs".format(db.nginx.count_documents({})))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("\tmethod {}: {}".format(
            method, db.nginx.count_documents({"method": method})))

    print("{} status check".format(db.nginx.count_documents(
        {"method": "GET", "path": "/status"})))
