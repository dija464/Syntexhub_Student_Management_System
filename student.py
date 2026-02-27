class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def to_dict(self):
        return {
            "name": self.name,
            "student_id": self.student_id,
            "grade": self.grade
        }