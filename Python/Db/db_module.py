import sqlite3
from users import users

def create_table(database, fields):
    conn = sqlite3.connect(database['dbname'])
    cursor = conn.cursor()
    sql = "CREATE TABLE "+  database['tblname'] + "("
    for f in fields:
        sql += f['name'] + " " + f['dtype'] + " " + f['modify'] + ","
    sql = sql[:-1]
    sql += ")"
    cursor.execute("DROP TABLE IF EXISTS " +  database['tblname'] )
    cursor.execute(sql)   
    conn.commit()
    conn.close()
    
def getFields(database):
    conn = sqlite3.connect(database['dbname'])
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({database['tblname']})")
    return [info[1] for info in cursor.fetchall()]

def dbCount(database):
    conn = sqlite3.connect(database['dbname'])
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {database['tblname']}")
    return cursor.fetchone()[0]
    
def insertRow(database,_fields,_fieldata):
    if(len(_fields)!= len(_fieldata)): 
        print("Field list does not equal data provided");return
    conn = sqlite3.connect(database['dbname'])
    cursor = conn.cursor()    
    sql = "INSERT INTO "+ database['tblname'] + "("
    for f in _fields:
        sql += f + ","
    sql = sql[:-1] + ")"
    sql += " VALUES("
    for f in range(len(_fieldata)):
        sql += "?" + ","
    sql = sql[:-1] + ")"
    cursor.execute(sql,_fieldata)  
    conn.commit()
    conn.close() 
    
def getRecords(database, wclause):
    title = "All records from the table "+database['tblname']+":"
    if(len(wclause)>0): 
        title = title[:-1] + " " + wclause
    conn = sqlite3.connect(database['dbname'])
    cursor = conn.cursor()
    sql = "SELECT * FROM " +database['tblname'] + " "+ wclause
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(title)
    for row in rows:
        print(row)
        conn.close()   
        
def delRecord(database, user_id):
    conn = sqlite3.connect(database['dbname'])
    cursor = conn.cursor()
    removeRec = "DELETE FROM %s WHERE user_id = %s" % (database['tblname'], user_id)
    cursor.execute(removeRec)
    conn.commit()
    conn.close()
    
def updateRec(database, user_id, fieldlist):
    conn = sqlite3.connect(database['dbname'])
    cursor = conn.cursor()
    set_clause = ", ".join([f"{field['name']} = ?" for field in fieldlist])
    values = [field['value'] for field in fieldlist]
    values.append(user_id)
    sql = f"UPDATE {database['tblname']} SET {set_clause} WHERE user_id = ?"
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

def main():
    database = {'dbname':'people.db','tblname':'users'}  # database description using name:value pairs
    fieldlist = [{'name':'user_id','dtype':'integer','modify':'primary key autoincrement'},{'name':'username','dtype':'varchar(30)','modify':''},
            {'name':'password','dtype':'varchar(20)','modify':''},{'name':'level','dtype':'integer','modify':''}]
    
    create_table(database,fieldlist)  # call to the create_table method sending database, field descriptions via dictionaries
    fields = getFields(database)  # List of contact table fields
    if (dbCount(database) == 0):
        for user in users:
            fieldata = [user['user_id'],user['username'],user['password'],user['auth_level']]
            insertRow(database,fields,fieldata)
    whereclause = ""  #Initialize the 'where' (condition) clause variable
    getRecords(database,whereclause) # call to the getRecords method sending the database name and a 'where' (condition) clause
    print("-"*25)  # Print a dashed dividing line

main()
