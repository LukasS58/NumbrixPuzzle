# -*- coding=utf-8 -*-

# Fehler importieren
from Fehler import Dateifehler

# für Matrizen 
import numpy as np

# einlesen der Daten in eine Matrix ohne auf die Bespielbarkeit der Matrix zu achten

def Einlesen_der_Datei(file:str) -> np.ndarray:
    ''' Die Funktion nimmt als Argument file das Verzeichnis der auszulesenden Textdatei, erstellt nach Kontrolle von
    Dimension und Einträgen im Spielfeld eine Numbrix Matrix A '''
         
    with open(file,"r") as file:
            L1 = file.readlines()

    # zur Sicherheit auf Kopie arbeiten (to be removed?)

    L = L1.copy()

    # Auslesen der wichtigen Informationen aus der Liste L:

    # Laenge der Liste
    k = len(L)
    # Dimension der Matrix auslesen
    # Anzahl Zeilen
    n = int(L[0].split(":")[1])
    # Anzahl Spalten
    m = int(L[1].split(":")[1])

    # ueberpruefe ob Dimensionen richtig sein koennen
    if not (k - 2 == n):
        raise Dateifehler("Es wurde nicht die richtige Anzahl an Zeilen in der Textdatei uebergeben")


    # initalisiere Matrix mit ganzzahligen Eintraegen
    A = np.zeros((n,m), dtype=int)
    # initalisieren einer Liste zum ueberpruefen der uebergebenen Zahlen
    checkList = []
    # Speichere die Werte in einer Matrix ab und bricht ab, falls Dimensionsfehler, keine 1 in Startmatrix oder Buchstabe statt int in Matrix
    for i in range(2, k):
        tempZeile = L[i].split("&")
        # Prüfung ob eine Zeile zu lang ist
        if not (len(tempZeile) == m):
            raise Dateifehler(f"in Zeile {i-1} der Matrix wurde nicht die richtige Anzahl an Argumenten uebergeben")
        else:
            # Iteration ueber die einzelnen Eintraege der aktuellen Zeile
            for p in range(m):
                try:
                    tempEintrag = int(tempZeile[p])
                except ValueError:
                        raise Dateifehler(f"Der Matrixeintrag an Stelle {i-1}{p+1} ist kein Integer")
                # ueberpruefe die Werte der Eintraege, leere Eintraege bzw. 0 werden übersprungen
                if not (tempEintrag == 0):
                    if tempEintrag < 0:
                        raise Dateifehler(f"Der Matrixeintrag an Stelle {i-1}{p+1} ist negativ")
                    else:
                        checkList.append(tempEintrag)
                        if checkList.count(tempEintrag) > 1:
                            raise Dateifehler(f"Der Wert {tempEintrag} wurde an Stelle {i-1}{p+1} doppelt uebergeben")
                        else:
                            A[i-2][p] = tempEintrag

    # Ueberpruefe ob der groesste Wert der Matrix ueberhaupt zulaessig ist
    if (A.max() > (m * n)):
        raise Dateifehler(f"Der groeßte Wert {A.max()} der Matrix ueberschreitet das zulaessige Maximum: {m * n}")

    # Ueberpruefe ob die Eins enthalten ist + SORTIERUNG DER LISTE ALLER ZAHLEN
    if not (np.sort(checkList)[0] == 1):
        raise Dateifehler("Es muss die Eins in der Matrix initalisert werden")
    
    return A
