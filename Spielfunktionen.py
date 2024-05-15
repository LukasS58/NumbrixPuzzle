# -*- coding=utf-8 -*-

import numpy as np
from Fehler import Spielfehler,Aufbaufehler, Eingabefehler, Programmfehler


# Die Funktionen arbeiten alle auf einer angepassten Matrix aus Einlesen_Aufbau genannt Numbrix Matrix unter Angabe der Dimension von A

# get Funktionen (alle Funktionen, die wichtige Informationen für den Spielverlauf generieren)


def getPosition(A:np.ndarray,n:int,m:int,k:int) -> tuple:
    '''sucht den Integer k in einer Numbrix Matrix A und gibt dessen Index zurück'''

    for i in range(n):
        for j in range(m):
            if A[i][j] == k:
                return (i,j)

    raise Programmfehler("Dieser Fehler sollte bei korrekter Ausführung nicht auftreten")      


def getAllNeighbours(pos:tuple,n:int,m:int) -> list:
    '''Funktion gibt alle horizontalen/vertikalen Nachbarn von pos zurueck, die in einer Numbrix Matrix mit Dimension n x m liegen'''


    # initaliseren der Liste zum Ausgeben
    L = []

    # Option 1: links des Feldes pruefen
    if (pos[1] - 1 >= 0):
        L.append((pos[0] , pos[1] - 1))

    # Option 2: rechts des Feldes pruefen
    if (pos[1] + 1 <= m - 1):
        L.append((pos[0] , pos[1] + 1))

    # Option 3: ueber dem Feld pruefen
    if (pos[0] - 1 >= 0):
        L.append((pos[0] - 1 , pos[1]))

    # Option 4: unter dem Feld pruefen
    if (pos[0] + 1 <= n - 1):
        L.append((pos[0]+1 , pos[1]))

    return L


def getFreeNeighbours(A:np.ndarray,pos:tuple,n:int,m:int) -> list:
    '''Funktion gibt alle horizontalen/vertikalen Nachbarn von pos zurueck, die unbelegt sind in Numbrix Matrix von Dimension n x m'''

    # initaliseren der Liste zum Ausgeben
    F = []
    L = getAllNeighbours(pos,n,m)

    for position in L:
        if A[position[0]][position[1]] == 0:
            F.append(position)

    return F


def getHorizontalDistance(pos1:tuple, pos2:tuple) -> int:
    '''Gibt zurück wie viel Abstand zwischen pos1 und pos2 liegt in horizontaler Richtung'''
    return abs(pos1[0] - pos2[0])


def getVerticalDistance(pos1:tuple, pos2:tuple) -> int:
    '''Gibt zurueck wie viel Abstand zwischen pos1 und pos2 liegt in vertikaler Richtung'''
    return abs(pos1[1] - pos2[1])


def getTotalDistance(pos1:tuple, pos2:tuple) -> int:
    '''Addiert horizontalen und vertikalen Abstand von pos1 und pos2'''
    return getVerticalDistance(pos1,pos2) + getHorizontalDistance(pos1,pos2)


def getMinimalDistance(pos1:tuple, pos2:tuple) -> int:
    '''Gibt den minimalen Abstand in vertikaler und horizontaler Richtung zwischen pos1 und pos2 zurück'''
    return min(getHorizontalDistance(pos1,pos2),getVerticalDistance(pos1,pos2))


def getMaximalDistance(pos1:tuple, pos2:tuple) -> int:
    '''Gibt den maximalen Abstand in vertikaler und horizontaler Richtung zwischen pos1 und pos2 zurück'''
    return max(getHorizontalDistance(pos1,pos2),getVerticalDistance(pos1,pos2))


# check Funktionen (alle Funktionen, die wichtige Sachverhalte fuer den Spielverlauf pruefen)

def areNeighbours(pos1:tuple,pos2:tuple) -> bool:
    '''Prueft ob pos1 und pos 2 horizontal bzw. vertikal Nachbarn sind'''
    # prueft ob Nachbar ueberhaupt moeglich ist:
    if getMinimalDistance(pos1,pos2) < 2 and getMaximalDistance(pos1,pos2) < 2:
        # wenn es ein Nachbar ist, dann ist horizontaler oder vertikaler Abstand gleich 0
        if getMinimalDistance(pos1,pos2) == 0:
            return True

    return False

def littleSolveable(A,L,n,m,k,pos) -> bool:
    '''Behilfscode fuer die Funktion isSolveable, um uebersichtlicher zu arbeiten'''
    # alle freien Nachbarn suchen und pruefen, ob es noch freie Nachbarn gibt
    freeNeighbours = getFreeNeighbours(A,pos,n,m)
    if len(freeNeighbours) == 0:
        return False
            
    # finde den naechsten vorbelegten Nachbar
    index = -1
    for zahl in L:
        if zahl > k:
            index = L.index(zahl)
            break
            
    # falls dieser existiert, pruefe ob wir in den naechsten Schritten noch an den Nachbarn kommen
    if not index == -1:
        AbstandZahlen = L[index] - k
        if  getTotalDistance(getPosition(A,n,m,k),getPosition(A,n,m,int(L[index]))) > AbstandZahlen:
            return False

        # ueberpruefe ob der Nachbar sinnvoll platziert werden kann, falls Zahl nur noch eins entfernt ist
        if L[index] == k + 2:
            # bilde Sets aus den Nachbarslisten
            nextFreeNeighbours = set(getFreeNeighbours(A,getPosition(A,n,m,k+2),n,m))
            # Pruefe ob der Schnitt leer ist
            if len(nextFreeNeighbours.intersection(set(freeNeighbours))) == 0:
                return False

    return True

def isSolveable(A:np.ndarray, L:list, n:int, m:int, k:int) -> bool:
    '''Prueft ob die NumbrixMatrix A mit Dimension n x m im Schritt k noch loesbar ist, L die (sortierte) Liste der Vorbelegungen'''
    # Position von k bestimmen
    pos = getPosition(A,n,m,k)

    # sind wir im ersten Index, so pruefen wir folgendes
    if k == 1:
        return littleSolveable(A,L,n,m,k,pos)
    
    # bei allen anderen Schritten pruefen wir auch den vorherigen Nachbarn            
    
    else:
        # Position des Vorgaengers bestimmen
        prev_pos = getPosition(A,n,m, k - 1)

        # pruefe ob k-1 in den Nachbarn ist
        # pruefe ob es noch freie Nachbarn gibt (nicht bei Schritt n * m)
        if k == m * n:
            return areNeighbours(pos,prev_pos)
        else:
            if areNeighbours(pos,prev_pos) == False:
                return False
            else:
                return littleSolveable(A,L,n,m,k,pos)

# nachstehende Funktion funktioniert zuverlaessig falls pos bereits geprüft ist 
def isFree(A:np.ndarray, pos:tuple) -> bool:
    '''Prueft ob ein Platz in der Matrix 0 (also beschreibbar) ist'''
    if A[int(pos[0])][int(pos[2])] == 0:
        return True
    else:
        return False

# spezifische Spielfunktionen


# Zum Start des Spiels
### ACHTUNG SAGT NICHT IMMER VORAUS OB DIE MATRIX LOESBAR IST, WENN DIE FUNKTION ANSCHLAEGT, DANN IST DAS FELD SICHER NICHT LOESBAR
### Gegenbeispiel ist die Matrix A = np.array([[0,3,4,0],[1,2,0,0],[0,7,0,0],[0,15,9,0]])

def get_check_Preallocation(A:np.ndarray,n:int,m:int) -> list:
    '''Gibt eine Liste aller Zahlen zurueck die in einer Numbrix Matrix A mit Dimension n x m stehen und prueft ob diese Belegung loesbar ist'''
    
    # initalisieren der Liste L
    L = []
    
    # alle Eintraege ausser den 0 in L anhängen
    for i in range(n):
        for j in range(m):
            if not (A[i][j] == 0):
                L.append(A[i][j])
    
    # sortieren der Liste
    L.sort()
    # Durchlaufe die Vorbelegungen und pruefe ob ein grober Fehler vorliegt
    for b in L:
        pos = getPosition(A, n,m,b)
        if littleSolveable(A,L,n,m,b,pos) == False:
            raise Aufbaufehler()

    return L

# Funktion zum Platzieren einer Zahl in der Matrix, funktioniert nur sicher mit geprueftem Tupel pos
def placeNumber(A:np.ndarray,k:int,pos:tuple) -> np.ndarray:
    '''prueft ob der gewuenschte Platz pos beschreibbar ist und platziert die Nummer k in A falls moeglich'''
    if isFree(A,pos) == False:
        raise Eingabefehler("Dieser Index kann nicht beschrieben werden")
    else:
        A[int(pos[0])][int(pos[2])] = k
    return A

