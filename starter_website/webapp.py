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

    unique_animal_ids = []
    for row in result:
        unique_animal_ids.append(row[0])

    if len(unique_animal_ids) == 0:
        return render_template('animal_browse.html', rows=result)

    query2 = "SELECT `Animals`.`Animal ID`, Animals.Name, Animals.Species, Animals.Age, Animals.Habitat, Animals.Injury, `Animals`.`Feeding ID`, Keepers.Name FROM Animals JOIN AnimalsKeepers ON Animals.`Animal ID` = AnimalsKeepers.`Animal ID` JOIN Keepers ON `AnimalsKeepers`.`Keeper ID` = `Keepers`.`Keeper ID`"
    result2 = execute_query(db_connection, query2).fetchall()
    strings_to_append = []
    for i in range(len(unique_animal_ids)):
        temp_str = ""
        temp_uid = unique_animal_ids[i]
        for row in result2:
            if row[0] == temp_uid:
                temp_str = temp_str + row[7] + " "
        strings_to_append.append(temp_str)

    appended_tuples = []
    for i in range(len(result)):
        appended_tuples.append(result[i] + (strings_to_append[i],))

    starting_tuple = (appended_tuples[0],)
    for i in range(1, len(appended_tuples)):
        starting_tuple = starting_tuple + (appended_tuples[i],)
    print(starting_tuple)

    return render_template('animal_browse.html', rows=starting_tuple)

@webapp.route('/browse_keepers')
def browse_keepers():
    print("Fetching and rendering keepers web page")
    db_connection = connect_to_database()
    query = "SELECT * from Keepers;"
    result = execute_query(db_connection, query).fetchall()

    unique_keeper_ids = []
    for row in result:
        unique_keeper_ids.append(row[0])

    if len(unique_keeper_ids) == 0:
        return render_template('keeper_browse.html', rows=result)

    query2 = "SELECT `Keepers`.`Keeper ID`, Keepers.Name, `Keepers`.`Job Title`, Animals.Name FROM Keepers JOIN AnimalsKeepers ON `Keepers`.`Keeper ID` = `AnimalsKeepers`.`Keeper ID` JOIN Animals ON `AnimalsKeepers`.`Animal ID` = `Animals`.`Animal ID`"
    result2 = execute_query(db_connection, query2).fetchall()

    strings_to_append = []
    for i in range(len(unique_keeper_ids)):
        temp_str = ""
        temp_uid = unique_keeper_ids[i]
        for row in result2:
            if row[0] == temp_uid:
                temp_str = temp_str + row[3] + " "
        strings_to_append.append(temp_str)

    appended_tuples = []
    for i in range(len(result)):
        appended_tuples.append(result[i] + (strings_to_append[i],))

    starting_tuple = (appended_tuples[0],)
    for i in range(1, len(appended_tuples)):
        starting_tuple = starting_tuple + (appended_tuples[i],)
    print(starting_tuple)

    return render_template('keeper_browse.html', rows=starting_tuple)

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

@webapp.route('/add_diet')
def prompt_add_diet():
    return render_template("add_diet.html")

@webapp.route('/add_diet', methods=['POST'])
def add_diet():
    db_connection = connect_to_database()
    diet = request.form['diet-input']
    food = request.form['food-input']

    data = (diet,food)
    print(data)
    query = "INSERT INTO `Diets` (`Diet`, `Foods`) VALUES (%s,%s);"
    execute_query(db_connection, query, data)

    query = "SELECT * from Diets;"
    result = execute_query(db_connection, query).fetchall()
    return render_template('diet_browse.html', rows=result)


@webapp.route('/browse_instructions')
def browse_instructions():
    print("Fetching and rendering instructions web page")
    db_connection = connect_to_database()
    query = "SELECT * from `Special Care Instructions`;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('instruction_browse.html', rows=result)

@webapp.route('/add_instruction')
def prompt_add_instruction():
    return render_template("add_instruction.html")

@webapp.route('/add_instruction', methods=['POST'])
def add_instruction():
    db_connection = connect_to_database()
    injury = request.form['injury-input']
    bandaging = request.form['bandaging-input']
    medicine = request.form['medicine-input']
    data = (injury,bandaging,medicine)
    print(data)
    query = "INSERT INTO `Special Care Instructions` (`Injury`, `Bandaging`, `Medicine`) VALUES (%s,%s,%s);"
    execute_query(db_connection, query, data)

    query = "SELECT * from `Special Care Instructions`;"
    result = execute_query(db_connection, query).fetchall()
    return render_template('instruction_browse.html', rows=result)

@webapp.route('/browse_animals', methods=['POST'])
def search_ID():
    db_connection = connect_to_database()
    text = request.form['text']
    value = request.form['submit_button']
    if text == "":
        query = "SELECT * from Animals;"
        result = execute_query(db_connection, query).fetchall()

        unique_animal_ids = []
        for row in result:
            unique_animal_ids.append(row[0])

        query2 = "SELECT `Animals`.`Animal ID`, Animals.Name, Animals.Species, Animals.Age, Animals.Habitat, Animals.Injury, `Animals`.`Feeding ID`, Keepers.Name FROM Animals JOIN AnimalsKeepers ON Animals.`Animal ID` = AnimalsKeepers.`Animal ID` JOIN Keepers ON `AnimalsKeepers`.`Keeper ID` = `Keepers`.`Keeper ID`"
        result2 = execute_query(db_connection, query2).fetchall()
        strings_to_append = []
        for i in range(len(unique_animal_ids)):
            temp_str = ""
            temp_uid = unique_animal_ids[i]
            for row in result2:
                if row[0] == temp_uid:
                    temp_str = temp_str + row[7] + " "
            strings_to_append.append(temp_str)

        appended_tuples = []
        for i in range(len(result)):
            appended_tuples.append(result[i] + (strings_to_append[i],))

        starting_tuple = (appended_tuples[0],)
        for i in range(1, len(appended_tuples)):
            starting_tuple = starting_tuple + (appended_tuples[i],)
        print(starting_tuple)

        return render_template('animal_browse.html', rows=starting_tuple)

    query = "SELECT * FROM Animals WHERE `Animals`.`" + value + "` = %s"
    data = (text,)
    result = execute_query(db_connection, query, data).fetchall()
    print(result)

    unique_animal_ids = []
    for row in result:
        unique_animal_ids.append(row[0])
    print(unique_animal_ids)

    query2 = "SELECT `Animals`.`Animal ID`, Animals.Name, Animals.Species, Animals.Age, Animals.Habitat, Animals.Injury, `Animals`.`Feeding ID`, Keepers.Name FROM Animals JOIN AnimalsKeepers ON Animals.`Animal ID` = AnimalsKeepers.`Animal ID` JOIN Keepers ON `AnimalsKeepers`.`Keeper ID` = `Keepers`.`Keeper ID` WHERE Animals.`" + value + "` = %s"
    data = (text,)
    result2 = execute_query(db_connection, query2, data).fetchall()
    print(result2)

    strings_to_append = []
    for i in range(len(unique_animal_ids)):
        temp_str = ""
        temp_uid = unique_animal_ids[i]
        for row in result2:
            if row[0] == temp_uid:
                temp_str = temp_str + row[7] + " "
        strings_to_append.append(temp_str)
    print(strings_to_append)

    appended_tuples = []
    for i in range(len(result)):
        appended_tuples.append(result[i] + (strings_to_append[i],))
    print(appended_tuples)
    # starting_tuple = (appended_tuples[0],)
    # for i in range(1, len(appended_tuples)):
    #     starting_tuple = starting_tuple + (appended_tuples[i],)
    # print(starting_tuple)

    return render_template('animal_browse.html', rows=appended_tuples)


@webapp.route('/add_animal')
def prompt_add_animal():
    db_connection = connect_to_database()
    times_query = "SELECT `Feeding Time ID` FROM `Feeding Times`;"
    times_result = execute_query(db_connection, times_query).fetchall()
    injury_query = "SELECT Injury FROM `Special Care Instructions`;"
    injury_result = execute_query(db_connection, injury_query).fetchall()
    print(times_result, injury_result)
    return render_template("add_animal.html", times=times_result, injury=injury_result)

@webapp.route('/add_animal', methods=['POST'])
def add_animal():
    db_connection = connect_to_database()
    animal_id = request.form['animal-input']
    name = request.form['name-input']
    species = request.form['species-input']
    age = request.form['age-input']
    habitat = request.form['habitat-input']
    feeding = request.form['feed-input']
    injury = request.form['injury-input']

    if injury == "":
        data = (animal_id, name, species, age, habitat, feeding)
        print(data)
        query = "INSERT INTO `Animals` (`Animal ID`, `Name`, `Species`, `Age`, `Habitat`, `Injury`, `Feeding ID`) VALUES (%s,%s,%s,%s,%s,NULL,%s);"
        execute_query(db_connection, query, data)
    else:
        data = (animal_id, name, species, age, habitat, injury, feeding)
        print(data)
        query = "INSERT INTO `Animals` (`Animal ID`, `Name`, `Species`, `Age`, `Habitat`, `Injury`, `Feeding ID`) VALUES (%s,%s,%s,%s,%s,%s,%s);"
        execute_query(db_connection, query, data)



    # query = "SELECT * from Animals;"
    # result = execute_query(db_connection, query).fetchall()
    return redirect('/browse_animals') # render_template('animal_browse.html', rows=result)


@webapp.route('/add_animal_keeper_connection')
def prompt_add_animal_keeper_connection():
    db_connection = connect_to_database()
    animal_query = "SELECT Animals.Name, `Animals`.`Animal ID` FROM Animals"
    keeper_query = "SELECT Keepers.Name, `Keepers`.`Keeper ID` FROM Keepers"
    animal_result = execute_query(db_connection, animal_query).fetchall()
    keeper_result = execute_query(db_connection, keeper_query).fetchall()
    return render_template("add_connection.html", animal=animal_result, keeper=keeper_result)

@webapp.route('/add_animal_keeper_connection', methods=['POST'])
def add_animal_keeper_connection():
    db_connection = connect_to_database()
    animal = request.form['animal-input']
    keeper = request.form['keeper-input']
    data = (animal, keeper)
    print(data)

    query = "INSERT INTO `AnimalsKeepers` (`Animal ID`, `Keeper ID`) VALUES (%s,%s);"
    execute_query(db_connection, query, data)

    query = "SELECT * from Animals;"
    result = execute_query(db_connection, query).fetchall()

    unique_animal_ids = []
    for row in result:
        unique_animal_ids.append(row[0])

    query2 = "SELECT `Animals`.`Animal ID`, Animals.Name, Animals.Species, Animals.Age, Animals.Habitat, Animals.Injury, `Animals`.`Feeding ID`, Keepers.Name FROM Animals JOIN AnimalsKeepers ON Animals.`Animal ID` = AnimalsKeepers.`Animal ID` JOIN Keepers ON `AnimalsKeepers`.`Keeper ID` = `Keepers`.`Keeper ID`"
    result2 = execute_query(db_connection, query2).fetchall()
    strings_to_append = []
    for i in range(len(unique_animal_ids)):
        temp_str = ""
        temp_uid = unique_animal_ids[i]
        for row in result2:
            if row[0] == temp_uid:
                temp_str = temp_str + row[7] + " "
        strings_to_append.append(temp_str)

    appended_tuples = []
    for i in range(len(result)):
        appended_tuples.append(result[i] + (strings_to_append[i],))

    starting_tuple = (appended_tuples[0],)
    for i in range(1, len(appended_tuples)):
        starting_tuple = starting_tuple + (appended_tuples[i],)
    print(starting_tuple)

    return render_template('animal_browse.html', rows=starting_tuple)


@webapp.route('/add_schedule')
def prompt_add_schedule():
    db_connection = connect_to_database()
    diets_query = 'SELECT Diet from `Diets`'
    diets_result = execute_query(db_connection, diets_query).fetchall()

    return render_template("add_schedule.html", diet=diets_result)

@webapp.route('/add_schedule', methods=['POST'])
def add_schedule():
    db_connection = connect_to_database()
    #if request.method == 'GET':

    request.method == 'POST'
    feeding_id = request.form['feedingid-input']
    diet = request.form['diet-input']
    time = request.form['time-input']

    data = (feeding_id, diet, time)
    print(data)
    query = "INSERT INTO `Feeding Times` (`Feeding Time ID`, `Diet`, `Time`) VALUES (%s,%s,%s);"
    execute_query(db_connection, query, data)

    query = "SELECT * from `Feeding Times`;"

    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('schedule_browse.html', rows=result)


@webapp.route('/add_keeper')
def prompt_add_keeper():
    return render_template("add_keeper.html")


@webapp.route('/add_keeper', methods=['POST'])
def add_keeper():
    db_connection = connect_to_database()
    #if request.method == 'GET':

    request.method == 'POST'
    keeper_id = request.form['keeperid-input']
    name = request.form['name-input']
    job = request.form['job-input']

    data = (keeper_id, name, job)
    print(data)
    query = "INSERT INTO `Keepers` (`Keeper ID`, `Name`, `Job Title`) VALUES (%s,%s,%s);"
    execute_query(db_connection, query, data)

    query = "SELECT * from Keepers;"
    result = execute_query(db_connection, query).fetchall()

    unique_keeper_ids = []
    for row in result:
        unique_keeper_ids.append(row[0])

    if len(unique_keeper_ids) == 0:
        return render_template('keeper_browse.html', rows=result)

    query2 = "SELECT `Keepers`.`Keeper ID`, Keepers.Name, `Keepers`.`Job Title`, Animals.Name FROM Keepers JOIN AnimalsKeepers ON `Keepers`.`Keeper ID` = `AnimalsKeepers`.`Keeper ID` JOIN Animals ON `AnimalsKeepers`.`Animal ID` = `Animals`.`Animal ID`"
    result2 = execute_query(db_connection, query2).fetchall()

    strings_to_append = []
    for i in range(len(unique_keeper_ids)):
        temp_str = ""
        temp_uid = unique_keeper_ids[i]
        for row in result2:
            if row[0] == temp_uid:
                temp_str = temp_str + row[3] + " "
        strings_to_append.append(temp_str)

    appended_tuples = []
    for i in range(len(result)):
        appended_tuples.append(result[i] + (strings_to_append[i],))

    starting_tuple = (appended_tuples[0],)
    for i in range(1, len(appended_tuples)):
        starting_tuple = starting_tuple + (appended_tuples[i],)
    print(starting_tuple)

    return render_template('keeper_browse.html', rows=starting_tuple)
    return render_template('keeper_browse.html', rows=result)


@webapp.route('/delete_animal/<int:id>')
def delete_animal(id):
    '''deletes an animal with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM `Animals` WHERE `Animal ID` = %s"
    data = (id, )
    result = execute_query(db_connection, query, data)
    #return render_template('animal_browse.html', rows=result)
    return redirect('/browse_animals')
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

        print(injury)
        if injury == "":
            print("inside if")
            injury_query = "UPDATE `Animals` SET `Name` = %s, `Species` = %s, `Age` = %s, `Habitat` = %s,`Injury`=NULL,`Feeding ID` =%s WHERE `Animal ID` = %s"
            data_1 = (name, species, age, habitat, feeding, animal_id)
            injury_result = execute_query(db_connection, injury_query,data_1)

        else:
            query = "UPDATE `Animals` SET `Name` = %s, `Species` = %s, `Age` = %s, `Habitat` = %s, `Injury` =%s, `Feeding ID` =%s WHERE `Animal ID` = %s"
            data = (name, species, age, habitat, injury, feeding, animal_id)
            result = execute_query(db_connection, query, data)

            print(str(result.rowcount) + " row(s) updated")
        return redirect('/browse_animals')


@webapp.route('/')
def index():
    return render_template("index.html")
