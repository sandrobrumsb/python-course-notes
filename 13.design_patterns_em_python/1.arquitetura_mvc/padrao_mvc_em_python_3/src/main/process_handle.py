from sympy import true
from .constructor.introduction_process import introduction_process


def start() -> None:
    while True:
        command = introduction_process()

        if command == "1":
            print("Comando 1 foi acionado")
        elif command == "2":
            print("Comando 2 foi acionado")
        elif command == "5":
            exit()
        else:
            print("\n Comando nao encontrado!!\n\n")
