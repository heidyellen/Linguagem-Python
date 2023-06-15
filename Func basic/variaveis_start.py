
# Declarando e inicializando uma variável
f = 0 
print(f)

# declarando a mesma variável novamente
f = "abc"
print(f)

# Gerando um erro, tentando unir variáveis de tipos diferentes

print ("Isso é ums string " + str(123))

# Variável Global X Variável local 

def AlgumaFunc():
  global f
  f = "def"
  print(f)
  
  AlgumaFunc()
  print(f)