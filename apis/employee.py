from os import stat
from tkinter import E
from urllib import response
from sqlalchemy.sql.expression import null
from db.db import SessionHelper
from flask import Response
from flask import request, jsonify
from db.models import Employee

def create_employee():
    try:

        session_helper = SessionHelper()
        session = session_helper.get_session()

        if request.method == 'POST':
            name = request.form['name']
            mobile_no = request.form['mobile_no']
            email = request.form['email']
            employee_branch = request.form['employee_branch']
            
            if  name != "" and mobile_no != "" and email != "" and employee_branch != "":
                employee_item = Employee(name=name, mobile_no=mobile_no, email=email, employee_branch=employee_branch)
                session.add(employee_item)
                session.commit()
                session.refresh(employee_item)
                return Response(status=201, response= "Employee Item created succesfully")
            else:
                return Response(status=400, response= "Field cannot be empty")
    
    except Exception as e:
        return Response(status= 400, response=  "An error occured "+str(e))
    session_helper.close_session()


def find_all_employees():
    try:


        session_helper = SessionHelper()
        session = session_helper.get_session()
        all_employees = []

        employee_items = session.query(Employee)
        for item in employee_items:
            all_employees.append({"id": item.id, "name": item.name, "mobile_no": item.mobile_no,"email": item.email, "employee_branch": item.employee_branch})
        session_helper.close_session()
        return {"data": all_employees}
    except Exception as e:
        session_helper.close_session()
        return Response(status= 400, response=  "An error occured "+str(e))