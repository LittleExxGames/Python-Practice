import sqlite3

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
    
def main():
    database = {'dbname':'people.db','tblname':'users'}  # database description using name:value pairs
    fieldlist = [{'name':'user_id','dtype':'integer','modify':'primary key autoincrement'},{'name':'username','dtype':'varchar(30)','modify':''},
            {'name':'password','dtype':'varchar(20)','modify':''},{'name':'level','dtype':'integer','modify':''}]
    
    create_table(database,fieldlist)  # call to the create_table method sending database, field descriptions via dictionaries

main()
