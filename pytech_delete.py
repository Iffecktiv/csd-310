from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.icskrbr.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
col = db.students
students =col.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- \n")

# For some weird reason. my code still keeps duplication, i can't seem to figure it out.

for doc in students:

    print("Student ID: " + doc["student_ID"])
    print("First Name: " + doc["first_name"])
    print("Last Name: " + doc[ "last_name"])
    print("")  
    
student_ID = {

    "student_id": "1010",

    "first_name": "Wout",

    "last_name": "Weghorst"

}


print( "INSERT STATEMENTS ")

student_ID = col.insert_one(student_ID).inserted_id

print("  Inserted student record into the students collection with document_id " + str(student_ID))

#Calling the find_one() method and display the results to the terminal window.

print("\n\n  -- DISPLAYING STUDENT TEST DOC -- ")

student_ID = db.students.find_one({"student_id": "1010"})

print("  Student ID: " + student_ID["student_id"])

print("  First Name: " + student_ID["first_name"])

print("  Last Name: " + student_ID["last_name"])

print("")

#Calling the delete_one() method by student_id 1010.

student_ID = db.students.delete_one({"student_id": "1010"})

#Calling the find() method and display the results to the terminal window.
 

students = col.find({})
 

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")  

for doc in students:

    print("  Student ID: " + doc["student_ID"])

    print("  First Name: " + doc["first_name"])

    print("  Last Name: " + doc["last_name"])

    print("")


input("\n\n  End of program, press any key to exit... ")