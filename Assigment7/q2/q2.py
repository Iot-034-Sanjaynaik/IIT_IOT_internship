# import Flask class from flask module
from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

# create a server usinf Flask
server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/soil_moisture')
def create_student():
    # extract data form form
    sensor_id = request.form.get('sensor_id')
    moisture_level = request.form.get('moisture_level')
    reading_time = request.form.get('reading_time')

    # create a query to add student into table
    query = f"insert into soil_moisture values({sensor_id}, '{moisture_level}', '{reading_time}');"

    #print(query)
    #execute the query 
    executeQuery(query=query)

    return "soil_moisture is added successfully"

@server.get('/soil_moisture')
def retrieve_students():
    # create a select query
    query = "select * from soil_moisture;"

    # execute select query
    data = executeSelectQuery(query=query)

    return f"soil_moisture : {data}"

@server.put('/soil_moisture')
def update_student():
    # extract data form form
    sensor_id = request.form.get('sensor_id')
    moisture_level = request.form.get('moisture_level')

    # create a query
    query = f"update soil_moisture SET moisture_level = '{moisture_level}' where sensor_id = {sensor_id};"
    # execute the query
    executeQuery(query=query)

    return "moisture_level is updated successfully"
@server.delete('/soil_moisture')
def delete_student():
    # extract data form form
    sensor_id = request.form.get('sensor_id')
    # create a query
    query = f"delete from soil_moisture where sensor_id = {sensor_id};"

    # execute the query
    executeQuery(query=query)

    return "soil_moisture is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)