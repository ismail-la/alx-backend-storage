#!/usr/bin/env python3
'''Task 15's module.
Improve 12-log_stats.py by adding the top 10 of the most present IPs in
the collection nginx of the database logs:

The IPs top must be sorted (like the example below)
'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Function that prints stats about Nginx request logs.
    '''
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count_req = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, count_req))
    status_count_checks = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_count_checks))


def print_ips_top(server_collection):
    '''Prints statistics about the top 10 HTTP IPs in a collection.
    '''
    print('IPs:')
    request_logs = server_collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for request_log in request_logs:
        ip = request_log['_id']
        ip_count_requests = request_log['totalRequests']
        print('\t{}: {}'.format(ip, ip_count_requests))


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)
    print_ips_top(client.logs.nginx)


if __name__ == '__main__':
    run()
