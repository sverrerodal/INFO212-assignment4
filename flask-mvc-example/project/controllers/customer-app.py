from project import app
from flask import render_template, request, redirect, url_for
from project.models.Customer import *

@app.route('/get_customers', methods=['GET'])
def find_customers():
    return findAllCustomers()

@app.route('/get_customers_by_name', methods=['POST'])
def find_customer_by_name():
    record = json.loads(request.data) 
    print(record)
    print(record['name'])
    return findCarByReg(record['name'])

@app.route('/save_customer', methods=["POST"])
def save_customer_info():
    record = json.loads(request.data)
    print(record)
    return save_customer(record['name'], record['age'], record['address'], record['status'])