# Drone Photogrammétrie

Ce projet vise à développer des scripts en Python pour contrôler un drone et effectuer des tâches de photogrammétrie, telles que la capture automatique de photos et la création de modèles 3D à partir d'images aériennes.

## Fonctionnalités

- **Contrôle manuel du drone** : Scripts permettant de piloter le drone manuellement à l'aide de la bibliothèque `pygame`.
- **Capture automatique de photos** : Script `photo.py` pour capturer des images à intervalles réguliers pendant le vol.
- **Mouvements automatisés** : Script `orbit_around.py` pour faire orbiter le drone autour d'un point d'intérêt.
- **Amélioration des photos** : Script `better_photo.py` pour optimiser la qualité des images capturées.

## Structure du projet

- `manual-control-pygame.py` : Contrôle manuel du drone avec `pygame`.
- `manual_control.py` : Autre script pour le contrôle manuel du drone.
- `photo.py` : Capture automatique de photos pendant le vol.
- `orbit_around.py` : Fait orbiter le drone autour d'un point spécifié.
- `better_photo.py` : Améliore la qualité des images capturées.
- `flow_chart.py` : Génère des diagrammes de flux pour les différentes opérations.
- `codetoflow.png`, `codetoflow_main.png`, `codetoflow_main_1.png`, `codetoflow_main_2.png` : Diagrammes de flux générés.
- Dossiers `.idea`, `drone-computer-vision`, `pythonProject1` : Contiennent des configurations de projet et du code supplémentaire.

## Prérequis

- Python 3.x
- Bibliothèques Python : `pygame`, `opencv`, etc.
- Drone compatible avec le SDK utilisé dans les scripts.

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/EagleOfFire/drone-photogrametrie.git
   ```
2. Installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```
3. Connectez votre drone et configurez les paramètres nécessaires dans les scripts.

## Utilisation

- Pour contrôler le drone manuellement avec `pygame` :
  ```bash
  python manual-control-pygame.py
  ```
- Pour capturer des photos automatiquement pendant le vol :
  ```bash
  python photo.py
  ```
- Pour faire orbiter le drone autour d'un point d'intérêt :
  ```bash
  python orbit_around.py
  ```
- Pour améliorer la qualité des photos capturées :
  ```bash
  python better_photo.py
  ```

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre une issue pour signaler un bug ou proposer une nouvelle fonctionnalité. Vous pouvez également créer une pull request avec vos modifications.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
