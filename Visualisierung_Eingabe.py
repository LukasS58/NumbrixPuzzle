# -*- coding=utf-8 -*-

import numpy as np
from Spielfunktionen import getPosition, getFreeNeighbours
from Fehler import Eingabefehler

# Zur uebersichtlichen Ausgabe der Matrix
def print_Matrix(A:np.ndarray,n:int,m:int,state:int) -> None:
    '''Durchlaeuft eine NumbrixMatrix A mit Dimension n x m und gibt diese in einer schoenen Form auf der Konsole aus, zusaetzlich werden 
    die moeglichen Nachbarn für den naechsten Zug angeben'''
    
    # Berechne die Laenge des Strings eines moeglichen Eingabetupels (+3 wegen () und ,)
    max_tuple = len(str(n)) + len(str(m)) + 3
    # Laenge der groessten Zahl, die im Spielverlauf eingegeben werden kann 
    max_width = len(str(n*m))
    # Maximum aus den beiden oberen Zeilen
    width = max(max_tuple,max_width)

    # suche die Position der letzten Zahl 
    pos = getPosition(A,n,m,state-1)
    # gebe die freien Nachbarn aus
    L = getFreeNeighbours(A,pos,n,m)
    
    for i in range(n):
        # initalisiere leeren String
        row_string = ""
        # Durchlaufe die aktuelle Zeile 
        for j in range(m):
            if A[i][j] == 0:
                # ist (i,j) ein beschreibbarer Nachbar?
                if (i, j) in L:
                    # ANSI Farbcode fuer gruene Schrift: \033[32m zum zuruecksetzen: \033[0m
                    row_string += "\033[32m" + f"{str((i, j)):>{width}}" + "\033[0m"
                else:  
                    # ansonsten ein Leerzeichen mit entsprechender Breite einfuegen  
                    row_string += " " * (width + 2)  # plus 2 für Abstand zwischen Zahlen
            else:
                # Ansonsten drucke das Element rechtsbuendig in der Breite von width
                row_string += f"{A[i][j]:>{width}}  "
        print(row_string)

# Funktionen zum ueberpruefen der Eingaben durch den Nutzer

def checkStringFormal(input:str) -> bool:
    '''ueberprueft, ob der Input von der Form int,int ist'''
    # Ueberpruefe ob ein , vorhanden ist
    if not "," in input:
        return False
    else:
        L = input.split(",")

    # pruefe richtige Laenge
    if not (len(L) == 2):
        return False
    
    # ueberpruefe ob zwei Integer uebergeben wurden
    try:
        int(L[0])
        int(L[1])
    except ValueError:
        return False
    
    
    return True    
        

def checkInput(string:str, n:int, m:int) -> None:
    '''Prueft ob ein String passendes Format, Verarbeitbar ist oder ob das Spiel beendet werden soll'''

    # prueft ob das Spiel beendet werden soll
    if string == "X" or string == "x":
        # Farbcode fuer lila Schrift: \033[35m
        print("\033[35m"+ "Spiel wurde vom Spieler beendet"+ "\033[0m")
        exit()

    # ueberpruefe ob richtige Form uebergeben wurde
    if not checkStringFormal(string):
        raise Eingabefehler("Richtiges Eingabeformat ist: int, int")

    L = input.split(",")

    # prueft ob die uebergebenen Indices eintragbar sind
    if not ( int(L[0]) >= 0 and int(L[0]) < n):
        raise Eingabefehler(f"Der Zeilenindex muss zwischen 0 und {n-1} liegen")
    if not ( int(L[1]) >= 0 and int(L[1]) < m):
        raise Eingabefehler(f"Der Spaltenindex muss zwischen 0 und {m-1} liegen")

    return None


        