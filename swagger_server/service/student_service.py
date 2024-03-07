import os

from pymongo import MongoClient

# Connecting to Database
mongo_db = MongoClient(os.getenv('MONGO_URI'))


def add(student=None):
    if mongo_db.local.student.find_one({"first_name": student.first_name, "last_name": student.last_name}):
        return 'already exists', 409
    result = mongo_db.local.student.insert_one(student.to_dict())
    return str(result.inserted_id), 200


def get_by_id(student_id=None):
    student = mongo_db.local.student.find_one({"student_id": student_id})
    if not student:
        return 'not found', 404
    student['student_id'] = str(student['_id'])
    del student["_id"]
    return student


def delete(student_id=None):
    result = mongo_db.local.student.find_one_and_delete({"student_id": student_id})
    if not result:
        return 'not found', 404
    return student_id
