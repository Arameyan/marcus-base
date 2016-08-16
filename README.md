# Projet Marcus 3

## Prochaines t�ches

- Utiliser les bornes 7 et 8 plut�t que 5 et 6 sur le P9 pour mon 5V. Le SYS_5V est coup� lorsque le BBB est ferm�, ce qui va �viter de pr�senter une tension aux bornes. 250mA max, � tester;
- Cr�er de nouveaux tests pour le module de CMUCam2+;
- Remplacer certaines boucles par pyinotify pour r�duire le temps de r�action ainsi que la charge sur le CPU;
- Cr�er un module "m�moire" avec SQLite3;
- Cr�er un module de supervision de batterie. Je pourrais m'en servir dans le journal et peut-�tre m�me adapter le comportement du robot.

## Notes

Avec la batterie actuelle recharg�e le robot se prom�ne sans probl�me pendant plus de 10 minutes. J'ai fait un test et apr�s 14 minutes il s'est mis � h�siter �norm�ment � cause des GP2D12 qui d�tectaient constamment des obstacles l� o� il n'y en avait pas. C'est probablement d� � une baisse de tension.

J'ai arr�t� le test apr�s environ 17 minutes. �a fait maintenant une vingtaine de minutes au moins que la batterie alimente le BBB avec une connexion active sur eth0. L'autonomie semble donc suffisante pour les premiers combats.

## Installation

- Flasher le BBB avec l'image Debian;
- Configurer hostname, PermitRootLogin;
- Installer git, screen;
- D�sinstaller les programmes inutiles (Apache2, Xorg, lightdm, etc.);
- Configurer :

  - dpkg-reconfigure tzdata;
  - dpkg-reconfigure locales (voir la section Standard de https://wiki.debian.org/Locale pour modifier /etc/profile);
  - Samba;

            apt-get install samba
            mv /etc/samba/smb.conf /etc/samba/smb.conf.old
            cp /root/marcus/ressources/smb.conf /etc/samba/smb.conf
            testparm /etc/samba/smb.conf
            systemctl start samba
            systemctl enable samba

  - hosts;
  - vim;
  - bash;
  - marcus.service;
  - uEnv.txt.

