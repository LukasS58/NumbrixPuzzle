# -*- coding=utf-8 -*-

# Modul fuer eigene Fehlerklassen, um die Fehler genauer nachvollziehen zu können


class Dateifehler(Exception):
    ''' Falls in der Datei fehlerhafte Daten uebergeben wurden'''
    def __init__(self, argument):  
      self.arguments = argument
      super().__init__(f"Fehler in Textdatei: {argument}, bitte die Textdatei verbessern!")


class Spielfehler(Exception):
   '''Falls der Spieler einen Fehler im Spielverlauf macht'''
   def __init__(self, argument):
      self.arguments = argument
      super().__init__(f"Oh Oh: {argument}")


class Aufbaufehler(Dateifehler):
   '''Falls die Matrix gar nicht bespielbar war/ist'''
   def __init__(self):
      super().__init__("Dieses Spielfeld ist gar nicht loesbar") 


class Eingabefehler(Spielfehler):
   '''Falls der Spieler einen ungueltigen Zug macht'''
   def __init__(self, argument):
      self.arguments = argument
      super().__init__(f"Falsche Eingabe: {argument}")


class Programmfehler(Exception):
   '''Falls das Programm falsche Sachen macht'''
   def __init__(self, *args: object) -> None:
      super().__init__(*args)      