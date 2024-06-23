#!/usr/bin/python# https://docs.python.org/3/library/argparse.html

# https://machinelearningmastery.com/command-line-arguments-for-your-python-script/
# https://docs.python.org/3/library/argparse.html
# https://logicaprogrammabile.it/raspberry-pi-come-usare-linee-gpio/

import argparse
import RPi.GPIO as GPIO
import time

parser = argparse.ArgumentParser(description="Gestione rele scheda keystudio per rpi\n"+
                                "uso:   rele.py 1 on            accende  il primo rele (o numero rele specificato)\n"+
                                "       rele.py 1 off           spegne   il primo rele (...)\n"+
                                "       rele.py 0 toggle        inverte  lo stato di tutti i rele \n\n"+

                                "con 0 si indicano TUTTI i rele, con i numeri da 1 a 4 si sceglie quale rele comandare \n\n"+

                                "gli stati sono:\n"+
                                "-----------------------------------\n"+
                                "on             accende\n"+
                                "off            spegne\n"+
                                "toggle         inverte\n"+
                                "inching        è un toggle temporizzato in base allo stato attuale\n"+
                                "               * se spento: accende per -d secondi e rispegne\n"+
                                "               * se acceso: spegne per -d secondi e riaccende\n"+
                                "inchtoon       (leggi inch to on)   [qualsiasi stato attuale] -> off -> (timer) -> on   (se è già off:  attende il timer -d e poi accende),\n"+
                                "inchtooff      (leggi inch to off)  [qualsiasi stato attuale] -> on  -> (timer) -> off  (se è già on:   attende il timer -d e poi spegne)\n"+
                                "-----------------------------------\n\n"+

                                "-d, --delay 3  attende 3 secondi nei comandi di inching, è il timer per il cambio di stato\n"
                                ,
                                usage='use "%(prog)s --help" for more information',
                                formatter_class=argparse.RawTextHelpFormatter)
#                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("rele", help="numero del rele [1..4 | 0:tutti]")
parser.add_argument("status", help="imposta stato del rele [on|off|toggle|inching|inchtoon|inchtooff]")
parser.add_argument("-d","--delay", default="2", help="ritardo per inching in secondi [2 secondi default]")
args = parser.parse_args()
config = vars(args)

rele=int(config["rele"])
status=config["status"]

if rele<0 or rele >4:
        print("errore: rele ",rele," non disponibile")
        quit()

#print(config)
#print("rele:   ", rele)
#print("status: ", status)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinList = [4, 22, 6, 26]
inchtime=int(config["delay"]) #secondi

for i in pinList:
        GPIO.setup(i, GPIO.OUT)


def allOn():
        for r in range(1,5,1):
                on(r)

def allOff():
        for r in range(1,5,1):
                off(r)

def allToggle():
        for r in range (1,5,1):
                toggle(r)

def allRead():
        ret=""
        for r in range(1,5,1):
                ret=ret+str(read(r))
        return ret

def on(r):
        pin=pinList[r-1]
        GPIO.output(pin, GPIO.HIGH)

def off(r):
        pin=pinList[r-1]
        GPIO.output(pin, GPIO.LOW)

def read(r):
        pin=pinList[r-1]
        return GPIO.input(pin)

def toggle(r):
        s=read(r) # status
        if (s==0):
                on(r)
        else:
                off(r)

match status:
        case "off":
                if (rele==0):
                        allOff()
                else:
                        off(rele)

        case "on":
                if (rele==0):
                        allOn()
                else:
                        on(rele)
        case "read":
                if  (rele==0):
                        print(allRead());
                else:
                        print(read(rele));
        case "toggle":
                if (rele==0):
                        allToggle()
                else:
                        toggle(rele)
        case "inching":
                if (rele==0):
                        allToggle()
                        time.sleep(inchtime)
                        allToggle()
                else:
                        toggle(rele)
                        time.sleep(inchtime)
                        toggle(rele)
        case "inchtoon":
                if (rele==0):
                        allOff()
                        time.sleep(inchtime)
                        allOn()
                else:
                        off(rele)
                        time.sleep(inchtime)
                        on(rele)
        case "inchtooff":
                if (rele==0):
                        allOn()
                        time.sleep(inchtime)
                        allOff()
                else:
                        on(rele)
                        time.sleep(inchtime)
                        off(rele)

#print(rele,":",status))
