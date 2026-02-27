import json
import os
from student import Student


class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            return json.load(file)

    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, name, student_id, grade):
        for student in self.students:
            if student["student_id"] == student_id:
                return False  # ID must be unique

        new_student = Student(name, student_id, grade)
        self.students.append(new_student.to_dict())
        self.save_students()
        return True

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s["student_id"] != student_id]
        self.save_students()

    def update_student(self, student_id, name, grade):
        for student in self.students:
            if student["student_id"] == student_id:
                student["name"] = name
                student["grade"] = grade
        self.save_students()

    def get_all_students(self):
        return self.students