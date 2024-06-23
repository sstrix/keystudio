**Python script to drive the KEYESTUDIO 4 Channel DC 5V Modulo Relay Expansion Board Power Relay Board Module per Raspberry Pi 4 3 2 A+ B+ 2B 3B**

usage: use "rele.py --help" for more information

Gestione rele scheda keystudio per rpi
uso:    rele.py 1 on            accende  il primo rele (o numero rele specificato)
        rele.py 1 off           spegne   il primo rele (...)
        rele.py 0 toggle        inverte  lo stato di tutti i rele

con 0 si indicano TUTTI i rele, con i numeri da 1 a 4 si sceglie quale rele comandare

gli stati sono:
-----------------------------------
on              accende
off             spegne
toggle          inverte
inching         è un toggle temporizzato in base allo stato attuale
                * se spento: accende per -d secondi e rispegne
                * se acceso: spegne per -d secondi e riaccende
inchtoon        (leggi inch to on)   [qualsiasi stato attuale] -> off -> (timer) -> on   (se è già off:  attende il timer -d e poi accende),
inchtooff       (leggi inch to off)  [qualsiasi stato attuale] -> on  -> (timer) -> off  (se è già on:   attende il timer -d e poi spegne)
-----------------------------------

-d, --delay 3   attende 3 secondi nei comandi di inching, è il timer per il cambio di stato

positional arguments:
  rele                  numero del rele [1..4 | 0:tutti]
  status                imposta stato del rele [on|off|toggle|inching|inchtoon|inchtooff]

options:
  -h, --help                 show this help message and exit
  -d DELAY, --delay DELAY    ritardo per inching in secondi [2 secondi default]
