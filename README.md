# analyseur-de-texte-avec-python
Code analyseur de texte python pour portfolio
C'est un outil automatisé construit avec Python capable de lire un fichier brut (format .txt) et d'en extraire des statistiques précises sans intervention humaine. Testé sur un terminal

Cela permet de transformer un texte brut en données exploitables. le script analyse_texte.py permet de :
Mesurer la complexité : En calculant la longueur moyenne des phrases.
Identifier les thèmes : En listant les mots les plus fréquents.
Vérifier la richesse du vocabulaire : En comptant les mots uniques.
Automatiser le résumé : En obtenant rapidement une vue d'ensemble du volume du document.
En rédigeant le code avec Python j'ai utilisé “re” pour le nettoyage, “Counter” pour le comptage rapide et “statistics” pour les calculs mathématiques.
Sécurisation (Try/Except) : J’ai sécurisé le  code dans une structure de sécurité en utilisant les fonctions Try et Except pour éviter que le programme ne s'arrête brutalement si le fichier est manquant.
J’ai converti le texte en minuscules et utilisé des expressions régulières pour supprimer la ponctuation inutile afin que l'ordinateur ne confonde pas "Bonjour" et "bonjour!".
J’ai découpé en morceaux les mots et phrases dans le texte.

