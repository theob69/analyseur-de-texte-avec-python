# analyseur-de-texte-avec-python
Code analyseur de texte python pour portfolio
C'est un outil automatisé construit avec Python capable de lire un fichier brut (format .txt) et d'en extraire des statistiques précises sans intervention humaine. Testé sur un terminal

Cela permet de transformer un texte brut en données exploitables. le script analyse_texte.py permet de :
Mesurer la complexité : En calculant la longueur moyenne des phrases.
Identifier les thèmes : En listant les mots les plus fréquents.
Vérifier la richesse du vocabulaire : En comptant les mots uniques.
Automatiser le résumé : En obtenant rapidement une vue d'ensemble du volume du document.
En rédigeant le code avec Python j'ai utilisé “re” pour le nettoyage, “Counter” pour le comptage rapide et “statistics” pour les calculs mathématiques. J’ai sécurisé le  code dans une structure de sécurité en utilisant les fonctions Try et Except pour éviter que le programme ne s'arrête brutalement si le fichier est manquant.
J’ai converti le texte en minuscules et utilisé des expressions régulières pour supprimer la ponctuation inutile afin que l'ordinateur ne confonde pas "Bonjour" et "bonjour!".
J’ai découpé en morceaux les mots et phrases dans le texte.



text-analyzer-with-python
Python text analyzer code for a portfolio This is an automated tool built with Python that can read a raw file (.txt format) and extract precise statistics from it without human intervention. Tested on a terminal

This allows you to transform raw text into actionable data. The analyse_texte.py script allows you to: Measure complexity: By calculating the average sentence length. Identify themes: By listing the most frequent words. Check vocabulary richness: By counting unique words. Automate summarization: By quickly obtaining an overview of the document’s volume. When writing the code in Python, I used “re” for cleaning, “Counter” for fast counting, and “statistics” for mathematical calculations. I secured the code within a safety structure using the Try and Except functions to prevent the program from crashing if a file is missing. I converted the text to lowercase and used regular expressions to remove unnecessary punctuation so that the computer wouldn’t confuse “Hello” and “hello!”. I split the words and phrases in the text into pieces.

