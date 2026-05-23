from pydantic import BaseModel
from typing  import Optional
class Student(BaseModel):
    name:str="Rajveer"
    age: Optional[int] = None
    
new_student = {"name":"Satyarth","age":"20"}
student= Student(**new_student)
print(student.name)
print(student.age)