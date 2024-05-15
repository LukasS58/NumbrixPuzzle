# NumbrixPuzzle
Programmierkurs SoSe 24

Lukas Sieber
Version 1.1
15.05.2024

-----------------------------------------------------------------------------------------------------------
Anleitung zum Spielen:

1. Schritt: Erstellen der Textdatei mit Spielfeld die Datei muss folgende Form haben:

\# Zeilen: 4\\
\# Spalten: 4\\
 0 & 1 & 0 & 0
 0 & 2 & 3 & 0
 0 & 7 & 4 & 0 
 0 & 0 & 0 & 0

In den ersten beiden Zeilen wird jeweils die Anzahl der Zeilen/Spalten uebergeben.
Die darauffolgenden Zeilen sind jeweils die Zeilen des Spielfelds. Die Eintraege in den Zeilen werden durch & getrennt.

2. Schritt: start.py oeffnen und in Zeile 40 der Datei, das richtige Verzeichnis zur Textdatei uebergeben. Durch Ausfuehren der Datei startet das Spiel.

-----------------------------------------------------------------------------------------------------------
Folgende Dateien sind in diesem Ordner zu finden (Beschreibung Funktion der Datei):

Fehler.py (enthaelt eigene Fehlerklassen fuer Fehler, die waehrend der Durchfuehrung auftreten koennen)
Einlesen_Aufbau.py (enthaelt eine Funktion, die das Spielfeld aus einer Textdatei einliest und die Daten verarbeitet)
Spielfunktionen.py (enthaelt alle Funktionen, die im Spielverlauf gebraucht werden (laufen im Hintergrund))
Visualisierung_Eingabe.py (enthaelt Funktionen, die das Spielfeld ausgeben und den UserInput ueberpruefen)
Spielvorgang.py (enthaelt drei Funktionen, die Spielfunktionen.py und Visualisierung_Eingabe.py verbinden und das ganze Spiel steuern)
start.py (enthaelt die main Funktion, mit der das Spiel gestartet werden kann)

Felddaten.txt (Beispieldatei fuer eine richtige Uebergabe des Spielfelds)

-----------------------------------------------------------------------------------------------------------
