import mysql.connector


connection= mysql.connector.connect(
    host='localhost',
    database='sdp',
    user='root',
    password='root123'
)

if connection.is_connected():
    print("successfully connected to the database")
    cursor = connection.cursor()
    create_table_query="""
    create table if not exists students (
        id int auto_increment primary key,
        name varchar(255) not null,
        age int,
        gender varchar(10)
    )
    """
    cursor.execute(create_table_query)
    print("table 'students'created successfully.")   
    
    insert_query="""
    insert into students (name,age,gender)
    values(%s,%s,%s)
    """
    student_records= [
        ('alice',22,'female'),
        ('bob',22,'male'),
        ('charlie',23,'male')
    ]
    cursor.executemany(insert_query,student_records)
    connection.commit()
    print(f"{cursor.rowcount} records inserted into 'students' table")
    
    
    
