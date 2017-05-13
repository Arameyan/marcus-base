#-*- coding:utf-8 -*-

# Librairies standard
#=====================
import logging
from random import random

# Librairies spéciales
#======================
from base import Comportement
from peripheriques.gp2d12 import get_dist

# Vecteur moteur
#================
"""Le comportement doit retourner un vecteur (une liste) décrivant les
actions à prendre par le moteur. La liste est une série de tuples avec
la vitesse du moteur droit, la vitesse du moteur gauche et la durée de
l'événement.

Le module de moteurs doit ensuite interpréter cette commande et la
traduire en consigne de moteurs.

Une nouvelle commande doit interrompre une manoeuvre en cours.

[(vitesse_gauche, vitesse_droite, duree), ...]
"""

class EvasionDouce(Comportement):

    def variables(self):

        self.seuil = 70 # En cm

    def decision(self):
        av_ga = get_dist('AIN0') # Avant gauche
        av_dr = get_dist('AIN1') # Avant droit

        # Obstacle à gauche mais pas à droite
        if av_ga < self.seuil and av_dr > self.seuil:

            logging.info("Comportement {} : Obstacle a gauche, evite a droite".format(self.nom))
            return [(71, 73, 0)]

        # Obstacle à droite mais pas à gauche
        if av_dr < self.seuil and av_ga > self.seuil:

            logging.info("Comportement {} : Obstacle a droite, evite a droite".format(self.nom))
            return [(73, 71, 0)]

        return None
