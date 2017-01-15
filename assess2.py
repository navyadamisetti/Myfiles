import json
import requests
import pymysql
from pprint import pprint

conn=pymysql.connect(host="localhost",user="root",passwd="navya",db="navya")  # Connecting to the DataBase.

obj = conn.cursor()            # creating an object for cursor class: Allows Python code to execute Queries.

reqdata = requests.get("http://roadtrippers.herokuapp.com/api/v1/cities/")  #getting data using requests

roadtrip = json.loads(reqdata.content)    #coverting into values

for i in range(0,len(roadtrip["cities"])):
	n=roadtrip["cities"][i]
	Id= n['id']
	names=n['name']
	cover=n['cover']
	states=n['state']
	obj.execute("INSERT INTO json (ID,NAME,COVER,STATE) VALUES (%s , %s , %s , %s)",(Id,names,cover,states));

print "Insertion of data into database is successfully completed"

obj.execute("select * from json")                                       #

rows=obj.fetchall()            # fetchall()-Used to fetch all rows of a query

for row in rows:               # Printing the row
    print "Name=",row[1]
    print "Cover=",row[2],"\n"
	
     
conn.commit() 
conn.close()
