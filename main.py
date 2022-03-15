from flask import Flask, render_template
from apis import employee
from dotenv import load_dotenv


load_dotenv()


app = Flask(__name__)

print(__name__)

#Employees
app.add_url_rule("/employee/get_employees", view_func= employee.find_all_employees, methods=["GET"] )
app.add_url_rule("/employee/insert_employee", view_func= employee.create_employee, methods=["POST"] )


#Views
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)