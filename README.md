# NumbrixPuzzle
Programmierkurs SoSe 24

Version 1.1<br/>
15.05.2024<br/>

-----------------------------------------------------------------------------------------------------------
Anleitung zum Spielen:

1. Schritt: Erstellen der Textdatei mit Spielfeld die Datei muss folgende Form haben:

\# Zeilen: 4 <br/>
\# Spalten: 4<br/>
 0 & 1 & 0 & 0<br/>
 0 & 2 & 3 & 0<br/>
 0 & 7 & 4 & 0<br/>
 0 & 0 & 0 & 0<br/>

In den ersten beiden Zeilen wird jeweils die Anzahl der Zeilen/Spalten uebergeben.<br/>
Die darauffolgenden Zeilen sind jeweils die Zeilen des Spielfelds. Die Eintraege in den Zeilen werden durch & getrennt.<br/>
Die 0 markiert dabei eine leere Stelle. <br/>

2. Schritt: start.py oeffnen und in Zeile 40 der Datei, das richtige Verzeichnis zur Textdatei uebergeben. Durch Ausfuehren der Datei startet das Spiel.<br/>

-----------------------------------------------------------------------------------------------------------
Folgende Dateien sind in diesem Ordner zu finden (Beschreibung Funktion der Datei):

Fehler.py (enthaelt eigene Fehlerklassen fuer Fehler, die waehrend der Durchfuehrung auftreten koennen)<br/>
Einlesen_Aufbau.py (enthaelt eine Funktion, die das Spielfeld aus einer Textdatei einliest und die Daten verarbeitet)<br/>
Spielfunktionen.py (enthaelt alle Funktionen, die im Spielverlauf gebraucht werden (laufen im Hintergrund))<br/>
Visualisierung_Eingabe.py (enthaelt Funktionen, die das Spielfeld ausgeben und den UserInput ueberpruefen)<br/>
Spielvorgang.py (enthaelt drei Funktionen, die Spielfunktionen.py und Visualisierung_Eingabe.py verbinden und das ganze Spiel steuern)<br/>
start.py (enthaelt die main Funktion, mit der das Spiel gestartet werden kann)<br/>

Felddaten.txt (Beispieldatei fuer eine richtige Uebergabe des Spielfelds)<br/>

-----------------------------------------------------------------------------------------------------------
