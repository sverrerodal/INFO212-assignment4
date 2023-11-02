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

def findAllCars():
    with _get_connection().session() as session:
        cars = session.run('MATCH (a:Car) RETURN a;')
        nodes_json = [node_to_json(record['a']) for record in cars] 
        print(nodes_json)
        return nodes_json
    
def findCarByReg(reg):
    with _get_connection().session() as session:
        cars = session.run('MATCH (a:Car) where a.reg=$reg RETURN a;', reg=reg) 
        print(cars)
        nodes_json = [node_to_json(record['a']) for record in cars]
        print(nodes_json)
        return nodes_json
    

def save_car(make, model, reg, year, capacity, location, status):
    cars = _get_connection().execute_query('MERGE (a:Car{make: $make, model: $model, reg: $reg, year: $year, capacity:$capacity, location:$location, status:$status}) RETURN a;', make = make, model = model, reg = reg, year = year, capacity = capacity, location = location, status = status)
    nodes_json = [node_to_json(record['a']) for record in cars] 
    print(nodes_json)
    return nodes_json

def update_car(make, model, reg, year, capacity, location, status): 
    with _get_connection().session() as session:
        cars = session.run('MATCH (a:Car{reg:$reg}) set a.make=$make, a.model=$model, a.year = $year, a.capacity = $capacity, a.location = $location, a.status = $status RETURN a;', reg=reg, make=make, model=model, year=year, capacity=capacity, location=location, status=status)
        print(cars)
        nodes_json = [node_to_json(record['a']) for record in cars] 
        print(nodes_json)
        return nodes_json

def delete_car(reg):
    _get_connection().execute_query('MATCH (a:Car{reg: $reg}) delete a;', reg = reg)

def set_car_status(reg, new_status): 
    with _get_connection().session() as session:
        if 'booked' == findCarByReg(reg).get('status'):
            return findCarByReg(reg)
        else:
            cars = session.run('MATCH (a:Car{reg:$reg}) set a.status = $status RETURN a;', reg=reg, status=new_status)
            print(cars)
            nodes_json = [node_to_json(record['a']) for record in cars] 
            print(nodes_json)
            return nodes_json