from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.icskrbr.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
col = db.students
students = col.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- \n")

for doc in students:

    print(" Student ID: " + doc["student_ID"] +
    "\n  First Name: " + doc["first_name"] +
    "\n  Last Name: " + doc[ "last_name"] +
    "\n")
    
result = db.collection.update_one({"student_ID": "1007"}, {"$set": {"last_name": "Adeniji"}})
cursor =col.find_one({"student_ID": "1007"})

print("\n -- DISPLAYING STUDENT DOCUMENT 1007 -- \n")

print(" Student ID: " + students["student_ID"] +
"\n First Name: " + students["first_name"] +
"\n Last Name: " + students [ "last_name"] + "\n")

input("\n\n End of program, press any key to continue...")