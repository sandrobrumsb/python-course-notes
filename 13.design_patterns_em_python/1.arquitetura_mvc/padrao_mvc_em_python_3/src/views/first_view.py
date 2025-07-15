from click import command


def introduction_page():
    message = """
    Sistema cadastral
    * Cadastrar pessoa - 1
    * Buscar Pessoa por Nome - 2
    * Sair - 3
    """
    print(message)
    command = input('Comando: ')
    
    return command
