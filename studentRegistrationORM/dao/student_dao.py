from models.student import Student

class StudentDAO:
    #grava geristro novo na tabelado banco de dados
    def create(self,name,age,email):
        return Student.create(name=name, age=age, email=email)
    
    #listar registros
   
    #busca o registro pelo id 

    def get_by_id(self,id_student):
        try:
            return Student.get(Student.id == id_student) 
        
        except Student.DoesNotExist:
            return None

    #deleta registro
    def delete(self, id_student):
        student = self.get_by_id(id_student)
        

        if student :
            student.delete_instance()
            return True

  

    #atualiza os registros

    #buscas todos os registros 

    #busca o registro pelo id 
