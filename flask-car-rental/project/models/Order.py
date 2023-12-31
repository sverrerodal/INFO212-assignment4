from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re
import json

URI = 'neo4j+s://8aaceb6d.databases.neo4j.io'
AUTH = ('neo4j', 'yWZQROLZYZIZpXHZnWeIO_c_1FHnB0ZGIrJYMci5MxM')


def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()

    return driver

def node_to_json(node): 
    node_properties = dict(node.items()) 
    return node_properties


def check_customers_bookings(type, customer, car):
    #checking if customer has a booking already (the booking key should be empty if no bookings)
    if type == "ORDER_CAR":
        if customer.get("booking") == "":
            return True
        return False
    elif type == "CANCEL_OR_RENT":
        if customer.get("booking") == car.get("reg"):
            return True
        return False
    print("-- ERROR IN CHECK_CUSTOMER_BOOKINGS - NO TYPE FOUND --")
    return False
