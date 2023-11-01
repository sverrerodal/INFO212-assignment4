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

def findAllEmployees():
    with _get_connection().session() as session:
        employees = session.run("MATCH (a:Employee) RETURN a;")
        nodes_json = [node_to_json(record["a"]) for record in employees] 
        print(nodes_json)
        return nodes_json
    
def findEmployeeByName(name):
    with _get_connection().session() as session:
        employees = session.run("MATCH (a:Employee) where a.name=$name RETURN a;", name=name) 
        print(employees)
        nodes_json = [node_to_json(record["a"]) for record in employees]
        print(nodes_json)
        return nodes_json
    

def save_employee(name, address, branch):
    #name, address, branch
    employees = _get_connection().execute_query("MERGE (a:Employee{name: $name, address: $address, branch: $branch}) RETURN a;", name = name, address = address, branch = branch)
    nodes_json = [node_to_json(record["a"]) for record in employees] 
    print(nodes_json)
    return nodes_json

def update_employee(name, address, branch): 
    with _get_connection().session() as session:
        employees = session.run("MATCH (a:Employee{name:$name}) set a.name=$name, a.address=$address, a.branch = $branch RETURN a;", name=name, address=address, branch=branch)
        print(employees)
        nodes_json = [node_to_json(record["a"]) for record in employees] 
        print(nodes_json)
        return nodes_json

def delete_employee(name):
    _get_connection().execute_query("MATCH (a:Employee{name: $name}) delete a;", name = name)