# -*- coding=utf-8 -*-

from Spielfunktionen import get_check_Preallocation, isSolveable, placeNumber
from Visualisierung_Eingabe import checkInput, print_Matrix
from Fehler import Aufbaufehler, Spielfehler, Eingabefehler

import numpy as np


def beginGame(A:np.ndarray, n:int, m:int) -> tuple:
    '''Diese Funktion beginnt das Spiel im Hintergrund auf der NumbrixMatrix A mit Dimension n x m
    und gibt eine Liste mit der Vorbelegung zurück wie einen Startwert'''

    # Liste mit Vorbelegungen einscannen, falls Fehler so muss das Programm beendet werden, da Matrix nicht loesbar
    try:
        V = get_check_Preallocation(A,n,m)
    except Aufbaufehler as e:
        print(e)
        print("Das Programm muss beendet werden")
        exit()

    for i in range(1,n*m + 1):
        if not i in V:
            # Begruessung und erstmalige Ausgabe der Matrix auf der Konsole
            print("Herzlich Willkommen im Numbrixspiel!")
            print(f"Die Spielmatrix hat {n} Zeilen und {m} Spalten")
            print("Indices werden durch die Form int, int uebergeben")
            print("Die " +  "\033[32m" + "gruenen" + "\033[0m" + " Zahlen in der Matrix sind die sinnvollen Schreibmoeglichkeiten")
            print("Zum Beenden des Spiels kann jeder Zeit X + Eingabe gedrueckt werden")
            print("Hier ist deine Spielmatrix, viel Erfolg!")
            print_Matrix(A,n,m,i)
            return V, i    
            
def runGame(A:np.ndarray, n:int, m:int, V:list, Step:int) -> tuple:
    '''Funktion fuehrt jeweils einen Spielschritt durch, 
    A: NumbrixMatrix,
    n: Anzahl Zeilen von A
    m: Anzahl Spalten von A
    V: Liste mit allen Vorbelegungen,
    Step: Zahl bei der sich das Spiel befindet,
    '''        


    if Step == n * m + 1:
        print("Gratulation du hast gewonnen!")
        return None
    
    
    if Step in V:
        return runGame(A,n,m,V, Step + 1)
    else:

        # pruefe ob das Feld loesbar ist
        if isSolveable(A, V, n, m, Step - 1):

            # User soll Index eingeben:
            # Abfangen von KeyboardInterrupt mit KeyboardCatch
            # und Eingabefehler mit InputCatch
            # und fehlerhaften Index mit WrongNumberCatch
            KeyboardCatch = True
            InputCatch = True
            WrongNumberCatch = True
            while KeyboardCatch == True or InputCatch == True or WrongNumberCatch == True:
                try:
                    Index = input(f" Wir platzieren die Zahl {Step} bitte Index eingeben: ")
                    KeyboardCatch = False
                except KeyboardInterrupt:
                    print("Bitte keine komischen Tastenkombinationen druecken")
                    KeyboardCatch = True

                try:
                    checkInput(Index,n,m)
                    InputCatch = False
                except Eingabefehler as e:
                    print(e)
                    InputCatch = True
                    continue
                try:
                    A = placeNumber(A,Step,Index)
                    WrongNumberCatch = False
                except Eingabefehler as e:
                    print(e)
                    WrongNumberCatch = True

            # entscheide welche Matrix ausgeben werden soll        
            if Step + 1 in V:
                print_Matrix(A,n,m,Step+2)
            else:
                print_Matrix(A,n,m,Step+1)
        
            return runGame(A,n,m,V,Step+1)
        else:
            print(Spielfehler("Das Spielfeld ist nicht mehr loesbar, GAME OVER"))
            exit()

def start_and_run(A):
    '''Startet ein Spiel auf der NumbrixMatrix A'''
    n,m = A.shape
    V,i = beginGame(A,n,m)
    runGame(A,n,m,V,i)

