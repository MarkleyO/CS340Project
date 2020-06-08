from flask import Flask, render_template
from flask import request, redirect
from db_connector.db_connector import connect_to_database, execute_query
#create the web application
webapp = Flask(__name__)

#provide a route where requests on the web application can be addressed
@webapp.route('/hello')
#provide a view (fancy name for a function) which responds to any requests on this route
def hello():
    return "Hello World!"

@webapp.route('/browse_animals')
def browse_animals():
    print("Fetching and rendering animals web page")
    db_connection = connect_to_database()
    query = "SELECT * from Animals;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('animal_browse.html', rows=result)

@webapp.route('/browse_keepers')
def browse_keepers():
    print("Fetching and rendering keepers web page")
    db_connection = connect_to_database()
    query = "SELECT * from Keepers;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('keeper_browse.html', rows=result)

@webapp.route('/browse_schedule')
def browse_schedule():
    print("Fetching and rendering schedule web page")
    db_connection = connect_to_database()
    query = "SELECT * from `Feeding Times`;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('schedule_browse.html', rows=result)

@webapp.route('/browse_diets')
def browse_diets():
    print("Fetching and rendering diets web page")
    db_connection = connect_to_database()
    query = "SELECT * from Diets;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('diet_browse.html', rows=result)

@webapp.route('/browse_instructions')
def browse_instructions():
    print("Fetching and rendering instructions web page")
    db_connection = connect_to_database()
    query = "SELECT * from `Special Care Instructions`;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('instruction_browse.html', rows=result)

@webapp.route('/browse_animals', methods=['POST'])
def search_ID():
    db_connection = connect_to_database()
    text = request.form['text']
    value = request.form['submit_button']
    if text == "":
        query = "SELECT * from Animals;"
        result = execute_query(db_connection, query).fetchall()
        return render_template('animal_browse.html', rows=result)

    query = "SELECT * FROM Animals WHERE `" + value + "` = %s"
    data = (text,)
    result = execute_query(db_connection, query, data)

    print(value)
    print(text)
    return render_template('animal_browse.html', rows=result)

@webapp.route('/add_animal')
def prompt_add_animal():
    return render_template("add_animal.html")

@webapp.route('/add_animal', methods=['POST'])
def add_animal():
    db_connection = connect_to_database()
    animal_id = request.form['animal-input']
    name = request.form['name-input']
    species = request.form['species-input']
    age = request.form['age-input']
    habitat = request.form['habitat-input']
    feeding = request.form['feeding-input']
    injury = request.form['injury-input']

    data = (animal_id, name, species, age, habitat, injury, feeding)
    print(data)
    query = "INSERT INTO `Animals` (`Animal ID`, `Name`, `Species`, `Age`, `Habitat`, `Injury`, `Feeding ID`) VALUES (%s,%s,%s,%s,%s,%s,%s);"
    execute_query(db_connection, query, data)

    query = "SELECT * from Animals;"
    result = execute_query(db_connection, query).fetchall()
    return render_template('animal_browse.html', rows=result)

#@webapp.route('/delete_animal/<int:id>')
#def delete_animal(id):
#    '''deletes a person with the given id'''
#    db_connection = connect_to_database()
#    query = "DELETE FROM `Animals` WHERE `Animal ID` = %s"
#    data = (id,)

#    result = execute_query(db_connection, query, data)
#    return (str(result.rowcount) + "row deleted")

#display update form and process any updates, using the same function
@webapp.route('/animal_update/<int:id>', methods=['POST','GET'])
def update_animal(id):
    print('In the function')
    db_connection = connect_to_database()
    #display existing data
    if request.method == 'GET':
        print('The GET request')
        animal_query = 'SELECT `Animal ID`, `Name`, `Species`, `Age`, `Habitat`, `Injury`, `Feeding ID`  from Animals WHERE `Animal ID`= %s'  % (id)
        animal_result = execute_query(db_connection, animal_query).fetchone()
        print("here")

        if animal_result == None:
            return "No such person found!"

        injury_query = 'SELECT `Injury` from `Special Care Instructions`'
        injury_result = execute_query(db_connection, injury_query).fetchall()

        feeding_query = 'SELECT `Feeding Time ID` from `Feeding Times`'
        feeding_result = execute_query(db_connection, feeding_query).fetchall()

        print('Returning')
        return render_template('animal_update.html', rows = animal_result, injury = injury_result, feeding= feeding_result)

    elif request.method == 'POST':
        print('The POST request')
        animal_id = request.form['animal-input']
        name = request.form['name-input']
        species = request.form['species-input']
        age = request.form['age-input']
        habitat = request.form['habitat-input']
        injury = request.form['injury-input']
        feeding = request.form['feeding-input']


        query = "UPDATE `Animals` SET `Name` = %s, `Species` = %s, `Age` = %s, `Habitat` = %s, `Injury` =%s, `Feeding ID` =%s WHERE `Animal ID` = %s"
        data = (name, species, age, habitat, injury, feeding, animal_id)

        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/browse_animals')

@webapp.route('/add_new_people', methods=['POST','GET'])
def add_new_people():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT id, name from bsg_planets'
        result = execute_query(db_connection, query).fetchall()
        print(result)

        return render_template('people_add_new.html', planets = result)
    elif request.method == 'POST':
        print("Add new people!")
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        homeworld = request.form['homeworld']

        query = 'INSERT INTO bsg_people (fname, lname, age, homeworld) VALUES (%s,%s,%s,%s)'
        data = (fname, lname, age, homeworld)
        execute_query(db_connection, query, data)
        return ('Person added!')

@webapp.route('/')
def index():
    return render_template("index.html")

@webapp.route('/home')
def home():
    db_connection = connect_to_database()
    query = "DROP TABLE IF EXISTS diagnostic;"
    execute_query(db_connection, query)
    query = "CREATE TABLE diagnostic(id INT PRIMARY KEY, text VARCHAR(255) NOT NULL);"
    execute_query(db_connection, query)
    query = "INSERT INTO diagnostic (text) VALUES ('MySQL is working');"
    execute_query(db_connection, query)
    query = "SELECT * from diagnostic;"
    result = execute_query(db_connection, query)
    for r in result:
        print(f"{r[0]}, {r[1]}")
    return render_template('home.html', result = result)

@webapp.route('/db_test')
def test_database_connection():
    print("Executing a sample query on the database using the credentials from db_credentials.py")
    db_connection = connect_to_database()
    query = "SELECT * from bsg_people;"
    result = execute_query(db_connection, query)
    return render_template('db_test.html', rows=result)

#display update form and process any updates, using the same function
@webapp.route('/update_people/<int:id>', methods=['POST','GET'])
def update_people(id):
    print('In the function')
    db_connection = connect_to_database()
    #display existing data
    if request.method == 'GET':
        print('The GET request')
        people_query = 'SELECT id, fname, lname, homeworld, age from bsg_people WHERE id = %s'  % (id)
        people_result = execute_query(db_connection, people_query).fetchone()

        if people_result == None:
            return "No such person found!"

        planets_query = 'SELECT id, name from bsg_planets'
        planets_results = execute_query(db_connection, planets_query).fetchall()

        print('Returning')
        return render_template('people_update.html', planets = planets_results, person = people_result)
    elif request.method == 'POST':
        print('The POST request')
        character_id = request.form['character_id']
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        homeworld = request.form['homeworld']

        query = "UPDATE bsg_people SET fname = %s, lname = %s, age = %s, homeworld = %s WHERE id = %s"
        data = (fname, lname, age, homeworld, character_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/browse_bsg_people')

@webapp.route('/delete_people/<int:id>')
def delete_people(id):
    '''deletes a person with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM bsg_people WHERE id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return (str(result.rowcount) + "row deleted")
