# Game of Brain

> Inspiré du jeu de simulation *Game of Life*, **Game of Brain** organise différentes entités "intelligentes" ayant accès à différentes ressources.

> Simulation ou travail effectif ?
C'est l'agencement de ces entités, leurs connexions et les ressources auxquelles elles on accès qui détermine l'évolution du système.






! Prévu avec un système de STOP d'urgence, en cas d'emballement, ou de mauvaise configuration.
-> coupure réseau, kill process hard, ou arrêt soft (avec sauvegarde/ reprise) (avec attente de fin de process) 









# install

- requirements : Python (tested with 3.10.12)

```bash
# clone
git clone https://github.com/scenaristeur/gob.git
cd gob

# make .venv
python -m venv .venv

# activate .venv
source .venv/bin/activate
pip install -r requirements.txt
# complete config/first.yaml
```


# start services
```bash
# MemGPT server
# git clone MemGPT
# memgpt configure

export MEMGPT_SERVER_PASS=ilovellms
memgpt server

```


# run 
```bash 
python main.py
```






# todo

multiple config

- dossier de config par ordre de recherche, cumulatif, paramétrisable par cli avec parametre -c config_file.yaml, en config.d à chaque fois

- ./config -> config dans le dossier courant
- ~.gob/config -> config dans le /home/user/.gob
- /etc/gob/config -> config pour le système 