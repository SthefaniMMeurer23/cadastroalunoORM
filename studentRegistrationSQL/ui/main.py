import sys
import os

PROJECT_DIR = "C:\\Projetos\\studentRegistrationSQL\\"

sys.path.append(os.path.abspath(PROJECT_DIR))

from db.connection import create_tables
import services.student_service as service


def show_students():
    students = service.display_record()

    for student in students:
        print (f"{student.id}- {student.name}- {student.email}- {student.age}")
    


#Menu principal
def main_menu() -> str:
    print("\n Sistema de Cadastro de Alunos")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Atualizar Aluno")
    print("4. Excluir Aluno")
    print("5. Sair")

    opcao:str = input("Escolha uma opção:")
    return opcao

if __name__ == "__main__":
    create_tables()    

    while True:
        opcao = main_menu()
        
        if opcao == "1":   
            name:str = input("Nome:")
            email:str = input("E-Mail:")
            age:int = int (input("Idade:"))
           

            service.create_record(name,email,age)
            show_students()


        elif opcao == "2":
           show_students()

        elif opcao == "3":
            show_students()
            id: int= input ("informe o id do aluno que voce deseja atualizar :")
            name : str= input ("informe o novo nome:")
            email: str =input ("informe o novo email:")
            age : int = int(input('informe o nova idade:'))

            service.update_record(name, email, age,id)
            


        #elif opcao == "4": 

      
      
        elif opcao == "5":
            break
        else:
            print("Opcao Invalida")
