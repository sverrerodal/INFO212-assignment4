from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re
import json

URI = "neo4j+s://8aaceb6d.databases.neo4j.io"
AUTH = ("neo4j", "yWZQROLZYZIZpXHZnWeIO_c_1FHnB0ZGIrJYMci5MxM")


def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()

    return driver

def node_to_json(node): 
    node_properties = dict(node.items()) 
    return node_properties

def order_car():
    pass

def cancel_car_order():
    pass

def rent_car():
    pass

def return_car():
    pass
