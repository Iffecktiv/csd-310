#Adding the required python code to connect to the connection,
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.icskrbr.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
col = db.students
students =col.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- \n")

# For some weird reason. my code keeps duplication, i can't seem to figure it out.

for doc in students:

    print("Student ID: " + doc["student_ID"])
    print("First Name: " + doc["first_name"])
    print("Last Name: " + doc[ "last_name"])
    print("")
# Do I need to show 'Adeniji II' in the "DOCUMENTS FROM find() QUERY?"
result = db.collection.update_one({"student_ID": "1007"}, {"$set": {"last_name": "Adeniji II"}})
cursor =col.find_one({"student_ID": "1007"})

print("\n -- DISPLAYING STUDENT DOCUMENT 1007 -- \n")

print(" Student ID: " + cursor["student_ID"] +
"\n First Name: " + cursor["first_name"] +
"\n Last Name: " + cursor [ "last_name"] + "\n")

input("\n\n End of program, press any key to continue...")