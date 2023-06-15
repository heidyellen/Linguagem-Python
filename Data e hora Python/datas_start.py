#
# Arquivo com exemplos de manipulação de  datas
#

from datetime import date
from datetime import time
from datetime import datetime

def ManipularDataHora():
  hoje = date.today()
  print("Hoje é:", hoje)
  print("Partes da data:", hoje.day, hoje.month, hoje.year)
  print("Número do dia da semana:", hoje.weekday())
  dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
  print("Nome do dia da semana é:", dias[hoje.weekday()])

  data=datetime.now()
  print("Data e hora:", data)
  
  tempo = datetime.time(data)
  print("Hora atual", tempo)
ManipularDataHora()