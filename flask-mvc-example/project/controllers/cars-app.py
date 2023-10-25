from project import app
from flask import render_template, request, redirect, url_for
from project.models.Car import *

@app.route('/get_cars', methods=['GET'])
def query_records():
    return findAllCars()

@app.route('/get_cars_by_reg_number', methods=['POST'])
def find_car_by_reg_number():
    record = json.loads(request.data) 
    print(record)
    print(record['reg'])
    return findCarByReg(record['reg'])

@app.route('/save_car', methods=["POST"])
def save_car_info():
    record = json.loads(request.data)
    print(record)
    return save_car(record['make'], record['model'], record['reg'], record['year'], record['capacity'])