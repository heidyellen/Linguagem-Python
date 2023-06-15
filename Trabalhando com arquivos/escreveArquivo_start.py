#
# Escrevendo arquivos com funções do Python
#
def EscreveArquivo():
  arquivo = open("NovoArquivo.txt", "w+")
  arquivo.write("Linha gerada com a funcao 'EscreveArquivo' \r\n")
  
  arquivo.close()
  
EscreveArquivo()
  
def alteraArquivo():
  arquivo = open("NovoArquivo.txt", "a+")
  arquivo.write("Linha gerada com a funcao 'alteraArquivo' \r\n")
  
  arquivo.close()
  
alteraArquivo()