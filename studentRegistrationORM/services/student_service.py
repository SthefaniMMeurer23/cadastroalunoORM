from dao.student_dao import StudentDAO



class StudentService:
    def __init__(self):
        self.dao = StudentDAO()

    def register_student(self, name, age, email):
        return self.dao.create(name, age, email)

    def update_student(self, id_student , name, age, email):
        print("Aluno atualizado")    

    def remove_student(self,id_student ):
        return self.dao.delete(id_student)
    
    def list_students(self):
        

        print("lista Alunos")        