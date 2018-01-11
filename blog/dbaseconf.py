
import psycopg2

class connection :
    def __init__(self):
        conn = psycopg2.connect("dbname=pythonpractice user=postgres password=123456")
        cur = conn.cursor()
        self.cur = cur
        self.conn = conn
    
    def __str__(self):
        return 'psql connect'