# Numeros al azar

#Importo libreria
import random

print(random.random()) # Valor random entre 0 y 1
print(random.normalvariate(100,1)) # Random correspondiente a una normal 100,1
# Aca puedo usar cualquier distribucion. beta. gamma, exp

# Operaciones matematicas

import math

print(math.pi)

e = math.e
print(round(e, 1))

# FECHAS
import datetime as dt # El as dt es un alias
# Tambien podemos importar sub-paquetes de una lu
from datetime import datetime as dt_dt
from datetime import date as dt_date

hoy = dt_dt.now()
print(hoy, type(hoy))

# Si solo quiero la fecha
hoy = dt_date.today()
print(hoy, type(hoy))
# Este tipo de dato que es propio de la libreria datetime me permite despues aplicarle metodos de esta libreria
# Si lo quiero en str:
fecha = dt.datetime.today().ctime()
print(fecha, type(fecha))

#Convertir un string en date

exp_date_str = "2024-09-20"
exp_date = dt_dt.strptime(exp_date_str, "%Y-%m-%d")
print(exp_date_str)
print(exp_date)
print(type(exp_date))

hoy = dt_dt.today()
#Diferencia de fechas
dias = (exp_date-hoy).days
print(dias)