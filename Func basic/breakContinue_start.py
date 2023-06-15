#
# Exemplo de como usar os comando Break e Continue
#
def loopBreake():
 for x in range (5,10):
   if x == 7:
     break
   print("O valor de X é: ", x)
  
#loopBreake()

def loopContinue():
  for x in range (5,10):
    if x == 7:
      continue
    print("O valor de x é", x)

loopContinue()