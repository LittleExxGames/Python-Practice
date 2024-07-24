from flask import Flask, request, jsonify
import json,sqlite3

app = Flask(__name__)

@app.route('/')  # The root/Index of the server
def home():
    return '''<span style='text-align:center'>
                <h1>All user Database: Database Management</h1>
                <h3>Authorized Users Only</h3><hr/>
            </span>'''
            
@app.route('/revise')    # domain/revise route
def edit_request():
    user_id = request.args.get('user_id') #URL is of form http://domain/revise?user_id=x&username=y 
    username = request.args.get('username') 
    password = request.args.get('password') #URL is of form http://domain/revise?user_id=x&username=y&password=value 
    auth = request.args.get('auth') #URL is of form http://domain/revise?user_id=x&username=y&auth=1
    print(user_id,username,password,auth)
    if (not user_id): # missing user_id=name
        return jsonify({'error': 'Please provide user user_id.'}), 400
    elif(not username): # missing username=kind
        return jsonify({'error': 'Please provide user username.'}), 400
    elif(not password and not auth): # password=value not present if only getting password
        user = access_row(user_id,username)
        if(user):
            return jsonify(user)
        else:
             return jsonify({'User not found': user_id +":" + username}), 400 
    elif(password and auth):
        user = access_row(user_id,username)
        if(user):
            password = int(password)
            auth = int(auth)
            update_both(user_id,username,password,auth)
            user = access_row(user_id,username)
            return jsonify(user)
    elif(password):  # password=value  present if changing password
        user = access_row(user_id,username)  # get password with this user_id and username
        if(user):
            password = int(password)   # change string from URL to decimal
            update_password(user_id,username,password) # Call SQL update method
            user = access_row(user_id,username)  # Get updated version (version in table)
            return jsonify(user)
        else:
           return jsonify({'user not found': user_id+"  :" + username}), 400 
    elif(auth):
        user = access_row(user_id,username)
        if(user):
            auth = int(auth)   # change string from URL to decimal
            update_auth(user_id,username,auth) # Call SQL update method
            user = access_row(user_id,username)  # Get updated version (version in table)
            return jsonify(user)
        else:
           return jsonify({'user not found': user_id+"  :" + username}), 400 
    else:
        return jsonify({'error': 'Please provide password or level.'}), 400
    
@app.route('/users')
def get_users():
    conn = sqlite3.connect('people.db')  # Connect to the database
    cursor = conn.cursor()  # Get a cursor
    cursor.execute('SELECT * FROM users')  # Execute a query to get all users
    users = cursor.fetchall()  # Fetch all rows from the query
    conn.close()  # Close the connection
    return jsonify(users)  # Convert the list of users to JSON and return it
    
    
        

def access_row(which,chem):
    conn = sqlite3.Connection('people.db')  # Connect
    cursor = conn.cursor()   # Get cursor
    cursor.execute("SELECT * FROM users WHERE user_id = ? and username=?", (which,chem))  #Read SQL
    product = cursor.fetchone()  #Get row
    conn.close() # release resources
    if product:
        return product  #Got a record
    else:
         return False 
    
def update_password(user_id,username,password):   # Delegate the updating to this function (decomposition)
    conn = sqlite3.connect('people.db') # Connect
    cursor = conn.cursor() # Get cursor
    result = cursor.execute('''UPDATE users SET password=? WHERE user_id = ? and username=?''', (password,user_id,username))
    conn.commit() # Make changes permanent
    conn.close()  # release resources
    return result  
  
def update_auth(user_id,username,auth):   # Delegate the updating to this function (decomposition)
    conn = sqlite3.connect('people.db') # Connect
    cursor = conn.cursor() # Get cursor
    result = cursor.execute('''UPDATE users SET level=? WHERE user_id = ? and username=?''', (auth,user_id,username))
    conn.commit() # Make changes permanent
    conn.close()  # release resources
    return result  

def update_both(user_id,username,password,auth):   # Delegate the updating to this function (decomposition)
    conn = sqlite3.connect('people.db') # Connect
    cursor = conn.cursor() # Get cursor
    result = cursor.execute('''UPDATE users SET password=?, level=? WHERE user_id = ? and username=?''', (password,auth,user_id,username))
    conn.commit() # Make changes permanent
    conn.close()  # release resources
    return result  
  
if __name__ == '__main__':
    app.run(debug=True)