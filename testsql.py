import pymysql


def fetchId(db_name, employee_table_name, manager_id):
    conn = pymysql.connect(
            host='localhost',
            user='root', 
            password = "shayan",
            db=db_name,
            )

    print("CONNECTED WITH DATABASE SERVER")
        
    cur = conn.cursor()

    query = "select employee_id from " + employee_table_name + " where manager_id="+ manager_id
    cur.execute(query)
    output = cur.fetchall()
    l = []
    
    for i in range(len(output)):
        l.append(output[i][0])
    
    return l

