# -*- coding=utf-8 -*-

from Einlesen_Aufbau import Einlesen_der_Datei
from Fehler import Dateifehler
from Spielvorgang import start_and_run

def main(file:str) -> None:
    '''Funktion startet das Spiel'''
    try:
       A = Einlesen_der_Datei(file)
       start_and_run(A)
    except Dateifehler  as e:
        print(e)
        exit()
    except FileNotFoundError:
        # endlos Schleife, falls der User den Dateipfad ausversehen falsch eingegeben hat
        # Farbcode fuer rote Ausgabe: \033[31m
        print("\033[31m " + "Diese Datei gibt es nicht" + "\033[0m")
        print("X + Eingabe zum beenden")
        test = True
        while test == True:
            data = input("Richtiger Dateipfad: ")
            if data == "X" or data == "x":
                exit()
            else:
                try:
                    A = Einlesen_der_Datei(data)
                    start_and_run(A)
                    test = False    
                except FileNotFoundError:
                    test = True
                    print("\033[31m " + "Diese Datei gibt es nicht" + "\033[0m")
                    print("X + Eingabe zum beenden")

    return None

    


if  ( __name__ == '__main__' ) :
    main("Felddaten.txt")