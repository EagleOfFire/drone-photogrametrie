# Projet 2 : Reconstruction 3D d'objets avec un drone Tello

## Description
Ce projet vise à réaliser une reconstruction 3D d'un objet à partir des images capturées par un drone Tello. L'objectif est de prendre plusieurs photos sous différents angles et d'utiliser des techniques de photogrammétrie pour générer un modèle 3D précis de l'objet.

## Objectifs
- Capturer des images de l'objet sous différents angles à l'aide du drone Tello.
- Utiliser des algorithmes de photogrammétrie pour reconstruire un modèle 3D.
- Générer un maillage 3D et appliquer des textures basées sur les images capturées.
- Utiliser des outils de modélisation pour affiner le modèle 3D si nécessaire.

## Étapes de mise en œuvre
### 1. Capture d'images sous différents angles
- Faire voler le drone Tello autour de l'objet en prenant des images à plusieurs hauteurs et angles.
- Assurer une couverture complète de l'objet pour minimiser les zones non visibles.

### 2. Préparation des images
- Utiliser des logiciels de photogrammétrie comme Agisoft Metashape, Pix4D, Meshroom ou VisualSFM pour traiter les images.
- Identifier les points communs entre les images afin de créer un nuage de points 3D.

### 3. Génération du modèle 3D
- Convertir le nuage de points en un maillage 3D.
- Appliquer des textures aux surfaces du modèle en utilisant les images capturées.

### 4. Affinement du modèle
- Exporter le modèle vers un logiciel de modélisation 3D comme Blender ou MeshLab.
- Nettoyer les imperfections et ajuster les détails du modèle si nécessaire.

## Technologies et outils utilisés
- **Drone Tello** : Capture d'images sous différents angles.
- **OpenCV** : Traitement des images et calibration de la caméra.
- **Agisoft Metashape, Pix4D, Meshroom, VisualSFM** : Reconstruction 3D.
- **Blender, MeshLab** : Affinage et visualisation du modèle 3D.

## Conclusion
Ce projet démontre qu'il est possible de réaliser une reconstruction 3D d'un objet à partir d'un drone Tello en utilisant des techniques de photogrammétrie. Bien que la résolution de la caméra du Tello soit modeste, elle permet d'obtenir un modèle 3D simple. Pour des projets plus complexes, l'utilisation d'un drone équipé d'une caméra à haute résolution est recommandée.

