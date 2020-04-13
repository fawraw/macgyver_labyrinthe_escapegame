#! /usr/bin/env python3
# coding: utf-8

"""
    Module Labyrinthe qui contient la classe Labyrinthe
"""

import pygame

class Labyrinthe:
    """Cette classe contient le labyrinthe, controle la strucutre et la positions des objets aléatoires"""

    def __init__(self):
        """Méthode init"""

    def generate(self):
        "chargement du fichier map.py"
        with open("map.py", "r") as file:
            for line in file:
                line_map = []
                structure_map = []
                for letter in line:
                    if letter !="\n":
                        line_map.append(letter)
                        structure_map.append(line_map)




    def display
        """Methode pour l'affichage de l'ecran qui va contenir la structure et la positions"""
