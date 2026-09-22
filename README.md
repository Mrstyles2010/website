# STYLES_MR — site web 3D

## Stack
- HTML5
- CSS3 (glassmorphism + animations + CSS 3D)
- JavaScript (interactions, tilt, reveal, parallax, orbite sociale)
- Python Flask

## Installation Windows
1. Installe Python 3.11+.
2. Ouvre PowerShell dans ce dossier.
3. Lance :
   `py -m pip install flask`
4. Puis :
   `py app.py`
5. Ouvre : http://127.0.0.1:5000

## Personnalisation
- Photo principale : `static/assets/hero.jpg`
- 3 autres photos : ajoute `photo-1.jpg`, `photo-2.jpg`, `photo-3.jpg` dans `static/assets`, puis remplace les blocs placeholder dans `templates/index.html`.
- Réseaux sociaux : modifie `SOCIALS` dans `app.py` et les href dans `templates/index.html`.
- Texte des politiques : section `POLICIES` dans `templates/index.html`.

Le texte de l'histoire est basé uniquement sur les éléments du projet fournis : passion gaming, streaming, FiveM/GTA RP, Call of Duty, Rage Plugin Hook, simulation police et développement d'un shop online. Les politiques affichées sont un modèle de départ et doivent être adaptées aux règles et obligations réelles du shop.
