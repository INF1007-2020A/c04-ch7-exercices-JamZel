#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys
sys.path.insert(1, 'C:\Users\Jamy\Documents\GitHub\c04-ch6-exercices-JamZel')
import c04-ch6-exercices-JamZel._exercice_version_prof.py

# TODO: Définissez vos fonction ici
def Masse_Volume(a = 5, b = 6, c = 7, masse_volumique = 2.85):
    volume = (4/3) * math.pi * a * b * c
    masse = volume * masse_volumique
    print(f"La masse est {masse:.2f} unité(s), et le volume est de {volume:.2f} unité(s)")
    return volume, masse

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    Masse_Volume()

    pass
