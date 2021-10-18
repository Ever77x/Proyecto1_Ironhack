#!/usr/bin/env python
# coding: utf-8

# # Proyecto 1 Iron Hack 

# ## adivina el numero

# In[8]:


import random


# In[9]:


def adivina (x): ## <-- limite superior 
    
    print("=========================")
    print("  ¡Bienvenid@ al Juego!  ")
    print("=========================")
    print("""Tu meta: Es adivinar el numero generado por
          la computadora""")
    
    numero_aleatorio = random.randint(1,x) ## <-- generar numeros enteros aleatorios 
    ## <-- en numeros aleatorios estoy poniendo el numero inferior y el numero superior -x-
    
    prediccion = 0 ## el valor inicial es 0 para que no coincida con el numero aleatorio 
    
    while prediccion != numero_aleatorio: ## mientras la prediccion sea distinta a aleatorio hacer un proceso
        #el usuario ingresa un numero
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: "))  ## f-string
        
        if prediccion < numero_aleatorio:
            print("Intenta otro vez. Este numero es menor al que debes adivinar.")
        elif prediccion > numero_aleatorio:
            print("Intenta otro vez. Este numero es mayor al que debes adivinar.")
        
    print(f"¡Felicitaciones! Adivinaste el numero {numero_aleatorio} correctamente")
    


# In[ ]:


adivina(10)


# In[ ]:




