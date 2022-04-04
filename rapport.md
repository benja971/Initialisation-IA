# Projet TP: Intelligence Artificielle

![alt](./d1e47c37fa_119289_ia-intelligence-artificielle.jpg)

Auteur: Benjamin NIDDAM <br>
Année: 2022

## Introduction



## Présentation du projet

L'ojectif ici est de d'obtenir par le biais d'algorithmes d'IA un moyen de "noter" de 1 à 10 des vins en fonction de certaines de leurs caractéristiques. Les vins sont représentés par des données numériques, et les algorithmes d'IA sont des algorithmes de classification par "k plus proches voisins" et de "machine learning".

Ici, on étudiera ces différentes façons de "noter" les vins et on déterminera lequel est le plus efficace dans notre cas. Pour cela, on utilisera les données de l'étude :

    P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
    Modeling wine preferences by data mining from physicochemical properties.
    In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

Voici donc les caractéristiques des vins :

-   Acidité fixe
-   acidité volatile
-   acide citrique
-   sucre résiduel
-   chlorures
-   anhydride sulfureux libre
-   dioxyde de soufre total
-   densité
-   pH
-   sulfates
-   alcool

## Méthodes d'évaluation

Nous utiliserons le langage de programmation Python pour les deux méthodes.

### Régression par k plus proches voisins

Dans un premier temps nous avons mis en place un système de régression par "k plus proches voisins" (kNN). C'est un algorithme de régression qui permet de déterminer la classe d'un objet à partir de ses voisins. Il est basé sur la notion de distance.

### Machine learning

Dans un second temps, nous avons mis en place un système de machine learning. C'est un algorithme de classification qui permet de déterminer la classe d'un objet à partir de ses données. Il est basé sur la notion de probabilité.

Tout d'abord nous importerons les bibliothèques nécessaires :

-   `sklearn` pour les algorithmes de machine learning
-   `numpy` pour les opérations mathématiques
-   `pandas` pour les opérations sur les données
-   `matplotlib` pour les graphiques

Ensuite nous allons importer et séparer les données : <br>

À partir d’un échantillon de population qui représente nos données, on répartit les données en deux groupes, les données d’entraînement et les données de test. La première catégorie de données servira pendant la phase d’apprentissage du modèle alors que le second sera utilisé pour évaluer la qualité de prédiction du modèle. Le but n’est donc pas de construire une fonction qui prédira avec une précision optimale les valeurs des variables cibles mais une fonction qui se généralisera au mieux pour prédire des valeurs de données qui n’ont pas encore été observées.

#### Régression linéaire

Ici, pour déterminer la qualité du vin, nous allons mettre en place une régression. Il s'agit

#### Classification
