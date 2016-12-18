# -*- coding: utf-8 -*-

# Librairies standards
#======================
import argparse, logging, sys
from time import sleep
from multiprocessing import Process, Pipe

# Librairies spéciales
#======================
from modules.pins import set_input
from comportements import collision, evasion, exploration
from modules import moteurs

class Marcus:

    # Initialisation et sous-routines
    #=================================
    def __init__(self, args):
        self.args = args

        # Initialisation du journal d'événements
        log_frmt = "%(asctime)s[%(levelname)s] %(message)s"
        date_frmt = "%Y-%m-%d %H:%M:%S "
        if self.args.verbose:
            log_lvl = logging.DEBUG
        else:
            log_lvl = logging.INFO

        logging.basicConfig(filename=self.args.logfile,
                            format=log_frmt,
                            datefmt=date_frmt,
                            level=log_lvl)

        logging.info("Logger initié : {}".format(self.args.logfile))
        logging.info("Programme lancé")

        # Initialisation des pare-chocs
        set_input('P8_7') # Avant droit
        set_input('P8_8') # Avant gauche
        set_input('P8_9') # Arrière droit
        set_input('P8_10') # Arrière gauche

        # Initialisation de la CMUCam2+
#        self.cmucam_parent_conn, self.cmucam_child_conn = Pipe()
#        self.cmucam_sub = Process(target=cmucam.cam, args=(self.cmucam_child_conn))
#        self.cmucam_sub.start()
#        message = self.cmucam_parent_conn.recv()

#        if 'Erreur' in message:
#            logging.error(message)
#        else:
#            logging.info("Sous-routine lancée : cmucam_sub")

        # Initialisation des arbitres
        self.arbitres = dict()

        # Arbitre moteurs
        m = moteurs.Moteurs()
        self.arbitres[m.nom] = m
        self.arbitres[m.nom].active(collision.Collision, 2)
        self.arbitres[m.nom].active(evasion.Evasion, 5)
        self.arbitres[m.nom].active(exploration.Exploration, 9)

    # Arrêt
    #=======
    def quit(self):
        for key in self.arbitres.keys():
            self.arbitres[key].arret()
        sys.exit()

    # Boucle principale
    #===================
    def loop(self):

        while True:
            sleep(0.1)
            for key in self.arbitres.keys():
                self.arbitres[key].evalue()

#======================================================================
# Fonction :    main
# Description : Routine principale
#======================================================================
def main():
    parser = argparse.ArgumentParser(description='Robot Marcus (BBB) - Michel')

    parser.add_argument('-v',
                        '--verbose',
                        action='store_true',
                        help='Imprime l\'aide sur l\'exécution du script.')

    parser.add_argument('-l',
                        '--logfile',
                        action='store',
                        default=None,
                        help='Spécifie le chemin du journal d\'événement.')

    parser.add_argument('-s',
                        '--stop',
                        action='store_true',
                        help="Arrête l'exécution lorsqu'un impact est détecté.")
    parser.add_argument('--scan',
                        action='store_true',
                        help="Scanne la couleur devant la caméra au démarrage. Sinon la dernière couleur sauvegardée est chargée.")

    marcus = Marcus(args=parser.parse_args())
    marcus.loop()

if __name__ == '__main__':
    main()

