# import Flask class from flask module
from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

# create a server usinf Flask
server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/sensor_readings')
def create_student():
    # extract data form form
    id = request.form.get('id')
    temperature = request.form.get('temperature')
    humidity = request.form.get('humidity')
    timestamp = request.form.get('timestamp')

    # create a query to add student into table
    query = f"insert into sensor_readings values({id}, '{temperature}', '{humidity}', '{timestamp}');"

    #print(query)
    #execute the query 
    executeQuery(query=query)

    return "sensor_readings is added successfully"

@server.get('/sensor_readings')
def retrieve_students():
    # create a select query
    query = "select * from sensor_readings;"

    # execute select query
    data = executeSelectQuery(query=query)

    return f"sensor_readings : {data}"

@server.put('/sensor_readings')
def update_student():
    # extract data form form
    id = request.form.get('id')
    temperature = request.form.get('temperature')

    # create a query
    query = f"update sensor_readings SET temperature = '{temperature}' where id = {id};"

    # execute the query
    executeQuery(query=query)

    return "temperature is updated successfully"

@server.delete('/sensor_readings')
def delete_student():
    # extract data form form
    id = request.form.get('id')

    # create a query
    query = f"delete from sensor_readings where id = {id};"

    # execute the query
    executeQuery(query=query)

    return "sensor_readings is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000,debug=True)
