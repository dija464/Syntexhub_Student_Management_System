from flask import Flask, render_template, request, redirect
from manager import StudentManager

app = Flask(__name__)
manager = StudentManager()


@app.route("/")
def index():
    students = manager.get_all_students()
    edit_student = request.args.get("edit")
    student_to_edit = None

    if edit_student:
        for s in students:
            if s["student_id"] == edit_student:
                student_to_edit = s

    return render_template("index.html",
                           students=students,
                           student_to_edit=student_to_edit)


@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    student_id = request.form["student_id"]
    grade = request.form["grade"]

    manager.add_student(name, student_id, grade)
    return redirect("/")


@app.route("/update", methods=["POST"])
def update():
    name = request.form["name"]
    student_id = request.form["student_id"]
    grade = request.form["grade"]

    manager.update_student(student_id, name, grade)
    return redirect("/")


@app.route("/delete/<student_id>")
def delete(student_id):
    manager.delete_student(student_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)