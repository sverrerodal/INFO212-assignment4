from project import app
from flask import render_template, request, redirect, url_for
from project.models.Employee import *

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