from pyscript import display, document, window

class Student:
    def __init__(self, name, section, subject):
        self.full_name = name
        self.class_group = section
        self.pref_subject = subject

    def get_info(self):
      return f"• <strong>{self.full_name}</strong> ({self.class_group}) — Favorite: {self.pref_subject}<br>"

student_data = [
    Student("Charlize Galang", "10-Ruby", "SS"),
    Student("Amanda Gonzales", "10-Ruby", "ICT"),
    Student("Kaitlyn Nardo", "10-Ruby", "English"),
    Student("Jade Cabatingan", "10-Ruby", "Math"),
    Student("Erin Rebadulla", "10-Ruby", "Science")
]

def render_all(event):
    output_div = document.getElementById("results-box")
    output_div.innerHTML = ""

    for person in student_data:
        output_div.innerHTML += person.get_info() + "<br>"

def register_student(event):
    name_in = document.getElementById("inp_name").value
    sec_in = document.getElementById("inp_sec").value
    sub_in = document.getElementById("inp_fav").value

    if name_in and sec_in:
        new_entry = Student(name_in, sec_in, sub_in)
        student_data.append(new_entry)
        document.getElementById("results-box").innerHTML = "<em>New student added successfully!</em>"
        document.getElementById("inp_name").value = ""
        document.getElementById("inp_sec").value = ""
        document.getElementById("inp_fav").value = ""

window.register_student = register_student
window.render_all = render_all