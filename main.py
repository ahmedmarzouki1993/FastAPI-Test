from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student (BaseModel):
   id : int
   name: str
   grade: int 


#creation of list of  students:

students = [
   Student(id =1 ,name="ali zitouni" ,grade=3),
    Student(id =2 ,name="zied toumi" ,grade=5),
     Student(id =3 ,name="yousef ali" ,grade=4),
]

@app.get("/students/")
def read_students():
   return students

@app.post("/students/")
def create_student(New_student:Student):
   students.append(New_student)
   return New_student


@app.put("/students/{student_id}")
def update_student(student_id : int , updated_student:Student):
    for index,student in enumerate(students):
       if student.id == student_id:
          #he will change the student from the list students with index
          students[index] = updated_student
          return updated_student
    return {"error":"not found"}    















@app.delete("/students/{student_id}")
def delete_student (student_id:int):
   for index , student in enumerate(students):
      if student.id == student_id:
        del students[index]
        return {"message":"student deleted"}   
   return {"error":"student not found"}
    
          