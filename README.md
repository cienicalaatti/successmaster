# successmaster
# Täällä on sitä sähköpajaprojektin hyvää koodia.

Kommentointi ja dokumentaatio on ehkä vähän puutteellista, work in progress


Ohjelmisto koostuu kahdesta osasta: Arduino-scriptistä ja Python-ohjelmasta. USB:llä tietokoneeseen kytketty Arduino Uno kuuntelee sarjaporttia, johon käyttäjä syöttää graafisen Python-käyttöliittymän kautta haluamansa keitettävien kuppien määrän ja käynnistää prosessin. Arduino-ohjelma saa parametrina kuppien määrän, ajaa mittausprosessin ja lopulta odottaa, kunnes käyttäjä sammuttaa keittimen Python-ohjelmasta ja Arduino initialisoi ohjelman ja sen parametrit.

Arduino-scripti ajetaan sisään mikro-ohjaimelle, ohjelma käynnistyy ajamalla main.py - tiedosto.
Arduinon on oltava kytkettynä! 

Ohjelmistovaatimukset:

Python 3.x (kaikki pitäisi toimia, käytössä ollut 3.7)

PySerial- kirjasto: https://pypi.org/project/pyserial/

PyQt5: https://pypi.org/project/PyQt5/

Aduinon kirjastot: 

https://www.arduinolibraries.info/libraries/hx711-arduino-library

https://www.arduino.cc/en/reference/servo
