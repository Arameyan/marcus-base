#!/usr/bin/python
#-*- coding: utf-8 -*-

# Librairies standard
#=====================
import time, logging

# Librairies spéciales
#======================
from pins import set_pwm, reset_pwm, set_duty_cycle, set_output, set_low, set_high

class Moteurs:
    """Pilote d'opération des moteurs.
    P9_14 - PWM moteur droit
    P9_16 - PWM moteur gauche
    """

    def __init__(self):

        set_pwm('P9_14')
        set_pwm('P9_16')
        self.droit_arret()
        self.gauche_arret()

    def arret(self):
        """Cette méthode est appelée pour tous les arbitres à l'arrêt du
        programme générale dans main.py.
        """
        self.droit_arret()
        self.gauche_arret()
        reset_pwm("P9_14")
        reset_pwm("P9_16")

    def execute(self, action):
        """Exécute l'action demandée (une étape de vecteur, sans
        considérer la durée) sur les 2 moteurs. Considère maintenant
        les PMW.
        Tuple: (vitesse_gauche, vitesse_droit, duree)
        """
        # Moteur gauche
        set_duty_cycle("P9_16", abs(action[0]))
        # Moteur droit
        set_duty_cycle('P9_14', abs(action[1]))
 

    # Fonctions par moteur
    #======================

    def gauche_arret(self):
        set_duty_cycle('P9_16', 75) 

    def gauche_freine(self):
        set_duty_cycle("P9_16", 75)

    def gauche_recule(self):
        set_duty_cycle("P9_16", 78)

    def gauche_avance(self):
        set_duty_cycle("P9_16", 72)

    def droit_arret(self):
        set_duty_cycle("P9_14", 75)

    def droit_freine(self):
        set_duty_cycle("P9_14", 75)
        
    def droit_recule(self):
        set_duty_cycle("P9_14", 78)

    def droit_avance(self):
        set_duty_cycle("P9_14", 72)

