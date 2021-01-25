import pyrebase
import json

#Initialize Firebase
firebaseConfig={
    "apiKey": "AIzaSyBzmB5NCWo9q58OiPtz732Xva5JlAxl4L8",
    "authDomain": "api-endpoint-edc0a.firebaseapp.com",
    "databaseURL": "https://api-endpoint-edc0a-default-rtdb.firebaseio.com",
    "projectId": "api-endpoint-edc0a",
    "storageBucket": "api-endpoint-edc0a.appspot.com",
    "messagingSenderId": "607112984808",
    "appId": "1:607112984808:web:ce6a2045b8ed9b0c3cf15d",
    "measurementId": "G-YBXCF6DDBV"
    }

firebase=pyrebase.initialize_app(firebaseConfig)
 
db=firebase.database()

tower=input("Enter Tower:")
floor=input("Enter Floor:")
unit=input("Enter Unit no:")
error=False
li = [0, 0, 0, 0, 0, 0, 0]
try:
    data=db.child("Demo").child(tower).child(floor).child("units").child(unit).child("unit_status").get()
    status=int(data.val()) #convert object file to int
    if status==0:
        li[0]=1
    else:
        li[status - 1] = 1
except:
    error=True

result={
    "error": error,
    "categories": [
        "Yet to review",
        "Projectmanager Inspected & Snags given to Programhead",
        "Projectmanager Snags attended & Handed Over",
        "Customer Intimated for inspection",
        "Customer Snags Given to Architect",
        "Customer Snags Attended & Handed over to Supervisor",
        "Handed over to Customer"
    ],
    "data": li
}
json_dump = json.dumps(result)

print(json_dump)