import sys
from pathlib import Path

#pega o caminho do arquivo atual no caso main.py
current_file= Path(__file__)

#pega pasta rais do projeto
project_root = Path(__file__).parent.parent  

#adiciona a raiz do projeto no path do python
sys.path.append(str(project_root))



from db.Connection import connect_db, close_db
from services.student_service import StudentService

def show_menu():
    print("\n=====Sistema de Cadastro de Alunos=====")
    print("1. Cadastrar Aluno ")
    print("2. Listar Aluno ")
    print("5. Sair")
 
    print("=========================================")

def main():
    connect_db()
    service = StudentService()

    while True:
        show_menu()
        
        opcao= input("Escolha a opcao:")

        if opcao == "1":
           name = input("Informe o Nome :")
           age = int(input("Informe a Idade:"))
           email= input("Infome o Email:")
           service.register_student(name, age, email)
           print("Aluno Cadastrado com sucesso!")

        elif opcao == "5":
            print("Saindo do sistema")
            break
        else:
            print("Opçao invalida") 
    close_db()

if __name__ == "__main__":
    main()              
