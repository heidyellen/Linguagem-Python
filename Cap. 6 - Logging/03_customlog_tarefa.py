# Personalizando o retorno do logging
import logging

dados = {'pessoa': 'jess'}
# TODO: Crie uma outra função para rodar o log
def outra_funcao():
    logging.debug("Esta é uma mensagem de informação", extra=dados)


def main():
    # TODO: Defina o nível de log para debug e um arquivo para salvar
    # o retorno. Use também uma formatação personalizada
    formato = "%(asctime)s: %(levelname)s: %(funcName)s: Pessoa:%(pessoa)s"
    logging.basicConfig(
        level=logging.DEBUG, 
        format=formato
        )
    
    logging.info("Esta é uma mensagem de informação", extra=dados)
    logging.warning("Esta é uma mensagem de aviso", extra=dados)


if __name__ == "__main__":
    main()
