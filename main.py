from modelo.modelo_clinica import Clinica
from cli.cli import CLI

def main():
    sistema = Clinica()
    cli = CLI(sistema)
    cli.iniciar()

if __name__ == "__main__":
    main()