import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://faceattendencerts-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":{
        "name": "Samuel Marcio",
        "major": "Computer Sci",
        "starting_year": 2021,
        "total_attendance": 6,
        "standing": "A+",
        "year": 3,
        "last_attendance_time": "2023-12-11 00:54:34"
    }, 
    "852741":{
        "name": "Emily Blunt",
        "major": "Music",
        "starting_year": 2020,
        "total_attendance": 5,
        "standing": "A-",
        "year": 4,
        "last_attendance_time": "2023-12-10 00:52:12"
    },
    "963852":{
        "name": "Elon Musk",
        "major": "Economics",
        "starting_year": 2021,
        "total_attendance": 2,
        "standing": "B-",
        "year": 3,
        "last_attendance_time": "2023-12-11 00:42:15"
    } 
}

for key, value in data.items():
    ref.child(key).set(value)
