from flask import Flask, redirect, request, render_template, jsonify, url_for
import mysql.connector
import pandas as pd

app = Flask(__name__, static_url_path='/static')

# Establish a connection to the MySQL database
connect = mysql.connector.connect(
    host='localhost',
    user='root',
    password='megh',
    database='test'
)

@app.route('/')
def index():
    data = get_data()
    return render_template('user_login.html', data=data)


@app.route('/get_data', methods=['GET','POST'])
def get_data():
    sql = "SELECT * FROM savedata"
    df = pd.read_sql(sql, connect)
    
    custom_columns = ['First Name', 'Last Name','ID',  'Contact No.', 'Gender']

    table_html = "<table class='table table-bordered'><thead><tr>"
    for column in custom_columns:
        table_html += "<th style='text-align:center'>" + column + "</th>"
    table_html += "</tr></thead><tbody>"

    for index, row in df.iterrows():
        table_html += "<tr>"
        for value in row:
            table_html += "<td style='text-align:center'>" + str(value) + "</td>"
        table_html += "</tr>"
    
    table_html += "</tbody></table>"
    
    return table_html


@app.route('/save', methods=['POST','GET'])
def save_data():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        idea = request.form['id']
        contact = request.form['contact']
        gender = request.form['gender']
        
        cursor = connect.cursor()
        
        # Check if the record with the provided ID exists
        query_check = "SELECT * FROM savedata WHERE id = %s"
        cursor.execute(query_check, (idea,))
        existing_record = cursor.fetchone()
        
        if existing_record:
            # If the record exists, update it
            update_query = "UPDATE savedata SET firstname = %s, lastname = %s, contact = %s, gender = %s WHERE id = %s"
            cursor.execute(update_query, (firstname, lastname, contact, gender, idea))
            connect.commit()  # Commit the changes to the database
            cursor.close()
            return 'Data updated successfully'
        else:
            # If the record does not exist, insert a new record
            insert_query = "INSERT INTO savedata (firstname, lastname, id, contact, gender) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (firstname, lastname, idea, contact, gender))
            connect.commit()  # Commit the changes to the database
            cursor.close()
            return 'Data saved successfully'



@app.route('/update', methods=['GET', 'POST'])
def update_data():
    if request.method == 'POST':
        student_id = request.form['id']
        cursor = connect.cursor()
        query = "SELECT firstname, lastname, contact, gender FROM savedata WHERE id = %s"
        cursor.execute(query, (student_id,))
        student_data = cursor.fetchone()
        cursor.close()

        if student_data:
            return jsonify({
                'firstname': student_data[0],
                'lastname': student_data[1],
                'contact': student_data[2],
                'gender': student_data[3],
            })
        else:
            return jsonify({'error': 'Student not found'})

    return render_template('index.html')


@app.route('/delete', methods=['POST'])
def delete_data():
    if request.method == 'POST':
        idr = request.form['id']
        cursor = connect.cursor()
        query = "DELETE FROM savedata WHERE id=%s"  # Corrected the column name
        cursor.execute(query, (idr,))  # Ensure the parameter is passed as a tuple
        connect.commit()
        cursor.close()
        return 'Data deleted successfully'
    

@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    
    if request.method == 'POST':
        # Process login form submission
        cursor = connect.cursor()
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username and password match any record in the database
        cursor.execute("SELECT * FROM userdata WHERE username = %s AND password1 = %s", (username, password))
        user = cursor.fetchone()
        
        if user:  # If user exists in the database
            print("User present")
            return redirect(url_for('success'))  # Redirect to success page or any other page
        else:
            print("User not present")
            # Optionally, you can render an error message or return to the login page with a message
            return render_template('user_login.html', error="Invalid username or password")
    else:
        # Render the login page initially when the link is clicked
        return render_template('user_login.html')

    

@app.route('/success')
def success():
    return render_template('frame-18.html')

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = connect.cursor()
        
        # Check if the username and password match any record in the database
        cursor.execute("SELECT * FROM admindata WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        
        if user:  # If user exists in the database
            return redirect(url_for('success1'))
        else:
            return render_template('admin_login.html', error="Invalid username or password")

        # Returning a simple message to indicate user presence
    else:
        # Render the login page initially when the link is clicked
        return render_template('admin_login.html')

@app.route('/success1')
def success1():
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        cursor = connect.cursor()
        # Fetch data from the form
        id1 = request.form['id']
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        gender = request.form['gender']

        # Save email and password into userdata table
        user_query = "INSERT INTO userdata (username, password1) VALUES (%s, %s)"
        cursor.execute(user_query, (email, password))
        connect.commit()

        # Save other data into savedata table
        data_query = "INSERT INTO savedata (id, firstname, lastname, contact, gender) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(data_query, (id1, first_name, last_name, phone, gender))
        connect.commit()

        return redirect(url_for('index'))  # Redirect to the registration page
    else:
        return render_template('registeration.html')  # Render the registration page



if __name__ == '__main__':
    app.run(debug=True)