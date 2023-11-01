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

def order_car(name, booking):
    with _get_connection().session() as session:
        customers = session.run("MATCH (a:Customer) where a.name=$name, a.booking=$booking RETURN a;", name=name, booking="") 
        print(customers)
        nodes_json = [node_to_json(record["a"]) for record in customers]
        if "" in nodes_json('booking'): # CHECK IF WORKS
            customers = session.run("MATCH (a:Customer{name:$name}) set a.booking=$booking RETURN a;", name=name, booking=booking) 
            return True # reg nr not found in a customers booking, proceeding
        else:
            return False # a reg nr found in customers booking, stopping
        
def cancel_car_order(name, booking):
    with _get_connection().session() as session:
        customers = session.run("MATCH (a:Customer) where a.name=$name, a.booking=$booking RETURN a;", name=name, booking=booking) 
        print(customers)
        nodes_json = [node_to_json(record["a"]) for record in customers]
        if nodes_json == []:
            print("Booking not found")
            return False
        else:
            return True

def rent_car(name, booking):
    with _get_connection().session() as session:
        customers = session.run("MATCH (a:Customer) where a.name=$name, a.booking=$booking RETURN a;", name=name, booking=booking) 
        print(customers)
        nodes_json = [node_to_json(record["a"]) for record in customers]
        if nodes_json == []:
            print("Booking not found")
            return False
        else:
            return True

def return_car():
    pass
