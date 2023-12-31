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

    # Mye av koden her er kopiert fra forelesningsnotatene, med noen endringer der programmet ikke kjørte ordentlig. 
    # Customer og Employee bruker opp igjen samme kode som i Car ettersom de trenger de samme funksjonene, bare tilpasset seg selv

@app.route('/get_cars', methods=['GET'])
def find_cars():
    return findAllCars()

@app.route('/get_car_by_reg_number', methods=['POST'])
def find_car_by_reg_number():
    record = json.loads(request.data) 
    print(record)
    print(record['reg'])
    return findCarByReg(record['reg'])

@app.route('/save_car', methods=['POST'])
def save_car_info():
    record = json.loads(request.data)
    print(record)
    return save_car(record['make'], record['model'], record['reg'], record['year'], record['capacity'], record['location'], record['status'])

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
    return update_car(record['make'], record['model'], record['reg'], record['year'], record['capacity'], record['location'], record['status'])


# # # # # # # # # # # # # 
# Customer starts here  #
# # # # # # # # # # # # # 

@app.route('/get_customers', methods=['GET'])
def find_customers():
    return findAllCustomers()

@app.route('/get_customer_by_name', methods=['POST'])
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
    delete_customer(record['name'])
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

@app.route('/get_employee_by_name', methods=['POST'])
def find_employee_by_name():
    record = json.loads(request.data) 
    print(record)
    print(record['name'])
    return findEmployeeByName(record['name'])

@app.route('/save_employee', methods=['POST'])
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

    # Her legges først customer og car inn i hver sin variabel for å gjøre det enklere å hente ut de forskjellige verdiene
    # Kjøres så en if-sjekk for å se om customer allerede har en booking, dersom booking-keyen i customer er en tom streng kan programmet kjøres videre.
    # check_customer_bookings() ligger i Order.py modellen
    # Car oppdateres med å bruke update_car fra tidligere i oppgaven, og fyller ut det meste med dataen som allerede låg der, utenom "status" som oppdateres
    # videre i oppgaven basert på hvilken type kommando som kjøres.
    #
    # check_customer_bookings() har en egen input "type" som gjør at samme funksjonen kan brukes opp igjen selv om de forskjellige 
    # oppgavene trenger en litt annen sjekk.
    #

@app.route('/order_car', methods=['PUT'])
def order_car_info():
    record = json.loads(request.data)
    print(record)
    customer = findCustomerByName(record['name'])[0]
    car = findCarByReg(record['reg'])[0]
    if check_customers_bookings("ORDER_CAR", customer, None):
        update_car(car['make'], car['model'], car['reg'], car['year'], car['capacity'], car['location'], 'BOOKED')
        update_customer(customer['name'], customer['age'], customer['address'], record['reg'])
    return findCarByReg(record['reg'])

    # check if customer has booked another car
    # change car status to 'booked'
    
    
    
@app.route('/cancel_car_order', methods=['PUT'])
def cancel_car_order_info():
    record = json.loads(request.data)
    print(record)
    customer = findCustomerByName(record['name'])[0]
    car = findCarByReg(record['reg'])[0]
    if check_customers_bookings("CANCEL_OR_RENT", customer, car):
        update_car(car['make'], car['model'], car['reg'], car['year'], car['capacity'], car['location'], 'AVAILABLE')
        update_customer(customer['name'], customer['age'], customer['address'], "")
    return findCarByReg(record['reg'])

    # check customer has booked the car (reg nr)
    # if they have -> set car status to 'available'
    
@app.route('/rent_car', methods=['PUT'])
def rent_car_info():
    record = json.loads(request.data)
    print(record)
    customer = findCustomerByName(record['name'])[0]
    car = findCarByReg(record['reg'])[0]
    if check_customers_bookings("CANCEL_OR_RENT", customer, car):
        update_car(car['make'], car['model'], car['reg'], car['year'], car['capacity'], car['location'], 'RENTED')
    return findCarByReg(record['reg'])

    # Check customer for booking of the specific car
    # change car status to 'rented'

@app.route('/return_car', methods=['PUT'])
def return_car_info():
    record = json.loads(request.data)
    print(record)
    customer = findCustomerByName(record['name'])[0]
    car = findCarByReg(record['reg'])[0]
    if check_customers_bookings("CANCEL_OR_RENT", customer, car):
        update_car(car['make'], car['model'], car['reg'], car['year'], car['capacity'], car['location'], record['status'])
        update_customer(customer['name'], customer['age'], customer['address'], "")
    return findCarByReg(record['reg'])
    
    # {'name':'Sverre', 'booking':'EK12345', 'status':'DAMAGED'} 
    #                                              (eller 'AVAILABLE')
    
    # check if customer has rented the car
    # car status set to 'AVAILABLE' or 'DAMAGED'
