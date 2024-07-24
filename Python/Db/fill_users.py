import sqlite3
from users import users

    
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
    

def main():
    database = {'dbname':'people.db','tblname':'users'}  # database description using name:value pairs
    fields = getFields(database)  # List of contact table fields
    if (dbCount(database) == 0):
        for user in users:
            fieldata = [user['user_id'],user['username'],user['password'],user['auth_level']]
            insertRow(database,fields,fieldata)

main()
