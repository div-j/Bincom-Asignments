#creating function
def fibgen(n):
    """
    Fibonacci series of length n.
    """
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

#calling function
print(fibgen(4))

# question 2: create a todo_list 

from getpass import getpass
import psycopg2

conn = psycopg2.connect(database="mydb", user="myuser", password=getpass("Enter password: "), host="localhost")
cur = conn.cursor()

def create_table():
    """
    Creates a to-do list table in a Postgres database.
    """
    cur.execute("CREATE TABLE todo_list (id SERIAL PRIMARY KEY, task TEXT, completed BOOLEAN)")
    conn.commit()

def add_task(task):
    """
    Adds a task to the to-do list.
    """
    cur.execute("INSERT INTO todo_list (task, completed) VALUES (%s, %s)", (task, False))
    conn.commit()

def update(id):
    """
    Marks a task as completed in the to-do list.
    """
    cur.execute("UPDATE todo_list SET completed = True WHERE id = %s", (id,))
    conn.commit()

def delete_task(id):
    """
    Deletes a task from the to-do list.
    """
    cur.execute("DELETE FROM todo_list WHERE id = %s", (id,))
    conn.commit()


def get_tasks():
    """
    Gets all tasks in the to-do list.
    """
    cur.execute("SELECT * FROM todo_list")
    rows = cur.fetchall()
    return rows
    
conn.close()
 
