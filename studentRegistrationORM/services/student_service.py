from dao.student_dao import StudentDAO



class StudentService:
    def __init__(self):
        self.dao = StudentDAO()

    def register_student(self, name, age, email):
        return self.dao.create(name, age, email)

    def update_student(self, student_id, name, age, email):
        print("Aluno atualizado")    

    def remove_student(self,student_id):
        print(" Aluno removido")  

    def list_students(self):
        print("lista Alunos")        