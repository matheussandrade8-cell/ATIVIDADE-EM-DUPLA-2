import os
os.system("cls")
import time
numero=int(input("digite um numero:"))

for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")
    time.sleep(1)