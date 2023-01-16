from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.icskrbr.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
col = db.students

student_id1007 = {
    "student_ID": "1007",
    "first_name": "Ifeoluwa",
    "last_name": "Adeniji"
}

student_id1008 = {
    "student_ID": "1008",
    "first_name": "James",
    "last_name": "Bond"
}

student_id1009 = {
    "student_ID": "1009",
    "first_name": "John",
    "last_name": "Wick"
    }

student_ID = [student_id1007, student_id1008, student_id1009]
print( "INSERT STATEMENTS ")
for i in student_ID:
    returnedID = col.insert_one(i).inserted_id
    print("Inserted student record " + i["first_name"] + " " + i["last_name"] + " into the students collection with document_id " + str(returnedID)) 
    
    
                 
                  