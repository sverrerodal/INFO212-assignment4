from project import app
from flask import render_template, request, redirect, url_for
from project.models.Car import *
from project.models.Customer import *
from project.models.Employee import *
from project.models.Order import *

import json

# # # # # # # # # #
# Car starts here #
# # # # # # # # # # 

@app.route('/get_cars', methods=['GET'])
def find_cars():
    return findAllCars()

@app.route('/get_cars_by_reg_number', methods=['POST'])
def find_car_by_reg_number():
    record = json.loads(request.data) 
    print(record)
    print(record['reg'])
    return findCarByReg(record['reg'])

@app.route('/save_car', methods=['POST'])
def save_car_info():
    record = json.loads(request.data)
    print(record)
    return save_car(record['make'], record['model'], record['reg'], record['year'], record['capacity'])

@app.route('/delete_car', methods=['DELETE'])
def delete_car_info():
    record = json.loads(request.data)
    print(record)
    delete_car(record['reg'])
    return findAllCars()

@app.route('/update_car', methods=['PUT'])
def update_car_info():
    record = json.loads(request.data)
    print(record)
    return update_car(record['make'], record['model'], record['reg'], record['year'], record['capacity'])


# # # # # # # # # # # # # 
# Customer starts here  #
# # # # # # # # # # # # # 

@app.route('/get_customers', methods=['GET'])
def find_customers():
    return findAllCustomers()

@app.route('/get_customers_by_name', methods=['POST'])
def find_customer_by_name():
    record = json.loads(request.data) 
    print(record)
    print(record['name'])
    return findCustomerByName(record['name'])

@app.route('/save_customer', methods=['POST'])
def save_customer_info():
    record = json.loads(request.data)
    print(record)
    return save_customer(record['name'], record['age'], record['address'], record['booking'])

@app.route('/delete_customer', methods=['DELETE'])
def delete_customer_info():
    record = json.loads(request.data)
    print(record)
    delete_customer(record['reg'])
    return findAllCustomers()

@app.route('/update_customer', methods=['PUT'])
def update_customer_info():
    record = json.loads(request.data)
    print(record)
    return update_customer(record['name'], record['age'], record['address'], record['booking'])

# # # # # # # # # # # # # 
# Employee starts here  #
# # # # # # # # # # # # # 

@app.route('/get_employees', methods=['GET'])
def find_employees():
    return findAllEmployees()

@app.route('/get_employees_by_name', methods=['POST'])
def find_employee_by_name():
    record = json.loads(request.data) 
    print(record)
    print(record['name'])
    return findEmployeeByName(record['name'])

@app.route('/save_employee', methods=["POST"])
def save_employee_info():
    record = json.loads(request.data)
    print(record)
    return save_employee(record['name'], record['address'], record['branch'])

@app.route('/delete_employee', methods=['DELETE'])
def delete_employee_info():
    record = json.loads(request.data)
    print(record)
    delete_employee(record['name'])
    return findAllEmployees()

@app.route('/update_employee', methods=['PUT'])
def update_employee_info():
    record = json.loads(request.data)
    print(record)
    return update_employee(record['name'], record['address'], record['branch'])

# # # # # # # # # # #
# Order starts here #
# # # # # # # # # # #

@app.route('/order_car', methods=['PUT'])
def order_car_info():
    record = json.loads(request.data)
    print(record)
    if order_car(record['name'], record['reg']):            # {"name":"Sverre", "reg":"EK12345"}
        set_car_status(record['reg'], "booked")
    return findCustomerByName(record['name'])

    # check if customer has booked another car
    # change car status to "booked"
    
@app.route('/cancel_car_order', methods=['PUT'])
def cancel_car_order_info():
    record = json.loads(request.data)
    print(record)
    if cancel_car_order(record['name'], record['reg']):     # {"name":"Sverre", "reg":"EK12345"}
        set_car_status(record['booking'], "available")
    return findCustomerByName(record['name'])

    # check customer has booked the car (reg nr)
    # if they have -> set car status to "available"
    
@app.route('/rent_car', methods=['PUT'])
def rent_car_info():
    record = json.loads(request.data)
    print(record)
    if rent_car(record['name'], record['booking']):
        set_car_status(record['reg'], "rented")             # {"name":"Sverre", "booking":"EK12345"}
    return

    # Check customer for booking of the specific car
    # change car status to "rented"
    
@app.route('/return_car', methods=['PUT'])
def return_car_info():
    record = json.loads(request.data)
    print(record)
    if return_car(record['name'], record['booking']) and find_car_by_reg_number(record['booking']).get("status") == "rented":
        set_car_status(record['booking'], record['status']) 
    return
                                                            # {"name":"Sverre", "booking":"EK12345", "status":"damaged"}
    
    # check if customer has rented the car
    # car status set to "available" or "damaged"
