# rele.py

Python script to drive the KEYESTUDIO 4 Channel DC 5V Modulo Relay Expansion Board Power Relay Board Module per Raspberry Pi 4 3 2 A+ B+ 2B 3B


## Usage


```
use "python rele.py --help" for more information

manage keystudio board relays for rpi
test:   rele.py 1 on            turn on first relay (or specified relay number)
        rele.py 1 off           turn off first relay (...)
        rele.py 0 toggle        toggle status of all relays

0 mean ALL four relays on the board, with numbers from 1 to 4 can choose which relay drive

status are:

on              turn on 
off             turn off
toggle          invert status
inching         is a timed toggle switching the actual status
                * if relay is turned off: turn on for -d seconds then turn off
                * if relay if turned on: turn off for -d seconds then turn on
inchtoon        (read as inch to on)   [any current state] -> off -> (timer) -> on   (if yet off:  wait for the timer -d then turn on),
inchtooff       (read as inch to off)  [any current state] -> on ->  (timer) -> off  (if yet on:  wait for the timer -d then turn off),

-d, --delay 3   wait 3 seconds in inching commands

positional arguments:
  rele                  relay number [1..4 | 0:all]
  status                set relay status [on|off|toggle|inching|inchtoon|inchtooff]

options:
  -h, --help                 show this help message and exit
  -d DELAY, --delay DELAY    inching delay in seconds [default is 2 seconds]

```


## License

[MIT](https://choosealicense.com/licenses/mit/)
