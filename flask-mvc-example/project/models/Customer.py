from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re

URI = "neo4j+s://8aaceb6d.databases.neo4j.io"
AUTH = ("neo4j", "yWZQROLZYZIZpXHZnWeIO_c_1FHnB0ZGIrJYMci5MxM")


def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()

    return driver

def node_to_json(node): 
    node_properties = dict(node.items()) 
    return node_properties

def findAllCustomers():
    with _get_connection().session() as session:
        customers = session.run("MATCH (a:Customer) RETURN a;")
        nodes_json = [node_to_json(record["a"]) for record in customers] 
        print(nodes_json)
        return nodes_json
    
def findCustomerByName(name):
    with _get_connection().session() as session:
        customers = session.run("MATCH (a:Customer) where a.name=$name RETURN a;", name=name) 
        print(Customers)
        nodes_json = [node_to_json(record["a"]) for record in customers]
        print(nodes_json)
        return nodes_json
    

def save_customer(name, age, address):
    customers = _get_connection().execute_query("MERGE (a:Customer{name:$name, age:$age, address:$address, status:$status}) RETURN a;", name = name, age = age, address = address, status = status)
    nodes_json = [node_to_json(record["a"]) for record in customers] 
    print(nodes_json)
    return nodes_json

def update_customer(name, age, address): 
    with _get_connection().session() as session:
        customers = session.run("MATCH (a:Customer{name:$name}) set a.name = $name, a.age = $age, a.address = $address, a.status = $status RETURN a;", name = name, age = age, address = address, status = status)
        print(customers)
        nodes_json = [node_to_json(record["a"]) for record in customers] 
        print(nodes_json)
        return nodes_json

def delete_Customer(name):
    _get_connection().execute_query("MATCH (a:Customer{name: $name}) delete a;", name = name)