
import phonenumbers
from phonenumbers import geocoder
import time
import folium
from opencage.geocoder import OpenCageGeocode
import sys
from colorama import Fore
import os
from art import tprint
from tqdm import tqdm
from phonenumbers import timezone, carrier, is_possible_number, is_valid_number


tprint("Searchphone")
print(Fore.WHITE + "\t \t \t \t \t \t \t \t Developer: https://github.com/daarkfight00 ✔ \n ")
print(Fore.GREEN + "Questo software e' stato realizzato solo per scopo illustrativo, percio' non sono responsabile delle azioni che chiunque possa compiere con questo programma...")
print(Fore.CYAN  +"\nThis software is for illustrative purposes only, so I am not responsible for the actions that anyone can perform with this program...")
messaggio = Fore.RED +"\n \n \t \t \t \t \t Please Don't Use It For illegal Activity  [X]\n \n"
for char in messaggio:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
input(Fore.WHITE  +"Press a key to continue")
os.system('cls')
numero = input('Inserert the phone number with +"Country code" : ')
print('Searching \n \n')
for i in tqdm(range(100), colour = "green"):
    time.sleep(0.1)
os.system('cls')
numero_telefono = phonenumbers.parse(numero)
operatore_telefonico = phonenumbers.parse(numero, "Ro")
posizione = geocoder.description_for_number(numero_telefono, "en")
x = phonenumbers.parse(numero)
if phonenumbers.is_possible_number(x):
    print(Fore.WHITE +"The number can exist [✔]")
else:
    print(Fore.WHITE +"The number can't exist [X]")
y = phonenumbers.parse(numero)
if phonenumbers.is_valid_number(y):
    print(Fore.CYAN +"The number is valid [✔✔]")
else:
    print(Fore.CYAN +"The number isn't valid [XX]")
print(Fore.RED + f"Country: {timezone.time_zones_for_geographical_number(numero_telefono)}")
print(Fore.BLUE +"Telephone operator: ", carrier.name_for_number(operatore_telefonico, "en"))
input('Press a key to end')
os.system('cls')
tprint("Searchphone")
messaggio = Fore.RED +"\nDeveloper https://github.com/daarkfight00\n"
for char in messaggio:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
messaggio = Fore.GREEN +"Thanks for your use ;) "
for char in messaggio:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
time.sleep(5)
os.system("cls")
