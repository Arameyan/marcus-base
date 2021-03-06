#-*- coding:utf-8 -*-

# Librairies standard
#=====================
import logging
from random import random, randint, choice

# Librairies spéciales
#======================
from base import Comportement
from peripheriques.pins import get_input

# Vecteur moteur
#================
"""Le comportement doit retourner un vecteur (une liste) décrivant les
actions à prendre par le moteur. La liste est une série de tuples avec
la vitesse du moteur droit, la vitesse du moteur gauche et la durée de
l'événement.

Le module de moteurs doit ensuite interpréter cette commande et la
traduire en consigne de moteurs.

Une nouvelle commande doit interrompre une manoeuvre en cours.

[(vitesse_gauche, vitesse_droit, duree), ...]
"""

class Collision(Comportement):
    """Comportement qui gère les collisions du robot détectés par les
    pare-chocs.
    """

    def variables(self):

        self.duree_rotation_min = 0.4 # en secondes
        self.duree_recul = 0.6 # sec

    def decision(self):

        impact_av_dr = not get_input("P8_7")
        impact_av_ga = not get_input("P8_8")

        # Impact avant droit
        if impact_av_dr and not impact_av_ga:
            logging.info("Comportement {} : Impact avant droit, recule et tourne à gauche".format(self.nom))
            duree_rotation = self.duree_rotation_min + random()/2
            return [(75, 75, 0.1),
                    (80, 80, self.duree_recul),
                    (79, 71, duree_rotation)]

        # Impact avant droit et gauche
        elif impact_av_dr and impact_av_ga:
            duree_rotation = self.duree_rotation_min + random()
            tourne_gauche = choice((True, False))
            if tourne_gauche:
                logging.info("Comportement {} : Impact avant droit et gauche, recule et tourne à gauche".format(self.nom))
                return [(75, 75, 0.1),
                        (80, 80, self.duree_recul),
                        (79, 71, duree_rotation)]
            else:
                logging.info("Comportement {} : Impact avant droit et gauche, recule et tourne à droite".format(self.nom))
                return [(75, 75, 0.1),
                        (80, 80, self.duree_recul),
                        (71, 79, duree_rotation)]

        # Impact avant gauche
        elif not impact_av_dr and impact_av_ga:
            logging.info("Comportement {} : Impact avant gauche, recule et tourne à droite".format(self.nom))
            duree_rotation = self.duree_rotation_min + random()/2
            return [(75, 75, 0.1),
                    (80, 80, self.duree_recul),
                    (71, 79, duree_rotation)]

##         # Impact arrière
##         elif impact_ar_dr or impact_ar_ga:
##             logging.info("Comportement {} : Impact arrière, arrêt".format(self.nom))
##             return [(0, 0, 0)]

        return None
