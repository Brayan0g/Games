# juego del ahorcado 
# @brayangonzalez11
"""
Explicacion 
1. elegir aleatoriamente una palabra 
de una lista de palabras.
2. mostrar el dibujo de una horca.
3. mostrar un guio bajo por cada letra 
de la palabra
4. pedir al usuario que introduzca una
letra: si no es una unica letra indicar.
si ya se ha dicho indicarlo.
5. comprobar si esa letra esta contenida en 
la palabra elegida. 
6. si esta: volver a mostrar el dibujo 
de la horca como la ultima vez.
sustituir el guion correspondiente por la
letra dicha.
7. si no esta: mostrar el dibujo de la 
horca al que se añade una parte
8. si falla 6 veces: se completa el dibujo
del arhocado
9. si acierta todas las letras de la 
palabra: gano!
"""
import random
import os

palabras = ["COLOMBIA", "ECUADOR", "VENEZUELA", "BRASIL",
          "PERU", "ARGENTINA", "CHILE", "BOLIVIA", "PARAGUAY", "URUGUAY", 
           "GUAYANA", "SURINAM"]
palabra = random.choice(palabras)

fallo0 = """
          !===N
              N
              N
              N
      =========
"""
fallo1 = """
          !===N
          0   N
              N
              N
      =========
"""
fallo2 = """
          !===N
         _0   N
              N
              N
      =========
"""
fallo3 = """
          !===N
         _0_  N
              N
              N
      =========
"""
fallo4 = """
          !===N
         _0_  N
          l   N
              N
      =========
"""
fallo5 = """
          !===N
         _0_  N
          l   N
         /    N
      =========
"""

fallo6 = """
          !===N
         _0_  N
          l   N
         / \  N
      =========
"""
letras_correctas ="" # letras correctas dichas po el usuario
letras_todas = "" # todas las letras dichas por el usuario
fallos=0

while True:
  os.system("cls")
  print(" ******************** ")
  print("** Juego del Ahorcado **")
  print(" ******************** ")
  if fallos==0:
    print(fallo0)
  elif fallos==1:
    print(fallo1)
  elif fallos==2:
    print(fallo2)
  elif fallos==3:
    print(fallo3)
  elif fallos==4:
    print(fallo4)
  elif fallos==5:
    print(fallo5)
  elif fallos==6:
    print(fallo6)
    
  print()
  
  #mostramos las letras acertadas y guiones bajoes en las no acertadas
  
  resultado = ""
  
  for letra in palabra:
    if letra in letras_correctas:
      resultado += letra
    else:
      resultado+="_"
  print("      {}".format(resultado))
  print()
  print()

#comprobamos si se ha acertado la palabra o se han terminado los intentos

  if resultado==palabra:
    print("*** Has Ganado ***")
    break
  if fallos>5:
    print("*** La Palabra es: ", palabra)
    print("*** Has Perdido ***")
    break
#bucle para que el usuario teclee una letra que cumpla los requisitos
  while True:
    letra_usuario_sin_formato= input("Dime una letra:")
    letra_usuario = letra_usuario_sin_formato.upper ()
    if len (letra_usuario)<1 or len(letra_usuario)>1:
      print("Introduce una letra")
    elif letra_usuario in letras_todas:
      print("Esa letra ya la has dicho")
    elif not letra_usuario.isalpha():
      print("Introduce una letra")
    else:
      letras_todas+=letra_usuario
      break
#Comprobamos si la letra dicha por el usuario esta en la palabra 
  if letra_usuario not in palabra: 
    fallos+=1 
  else:
    letras_correctas+=letra_usuario