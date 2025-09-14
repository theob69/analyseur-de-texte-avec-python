import re
from collections import Counter
import statistics

def analyser_texte(fichier):
    try:
        # Lire le fichier texte
        with open(fichier, 'r', encoding='utf-8') as f:
            texte = f.read()
        
        # Nettoyer le texte
        # Convertir en minuscules et supprimer les caractères spéciaux
        texte_nettoye = re.sub(r'[^\w\s.]', '', texte.lower())
        
        # 1. Nombre total de mots
        mots = texte_nettoye.split()
        nombre_mots = len(mots)
        
        # 2. Fréquence des mots
        frequence_mots = Counter(mots)
        
        # 3. Mots les plus courants (top 5)
        mots_plus_courants = frequence_mots.most_common(5)
        
        # 4. Longueur moyenne des phrases
        # Séparer le texte en phrases (en utilisant le point comme séparateur)
        phrases = [phrase.strip() for phrase in texte.split('.') if phrase.strip()]
        nombre_phrases = len(phrases)
        
        # Calculer la longueur de chaque phrase (en nombre de mots)
        longueurs_phrases = [len(phrase.split()) for phrase in phrases]
        longueur_moyenne_phrase = statistics.mean(longueurs_phrases) if longueurs_phrases else 0
        
        # Afficher les résultats
        print(f"Analyse du fichier : {fichier}")
        print("-" * 50)
        print(f"Nombre total de mots : {nombre_mots}")
        print(f"Nombre total de phrases : {nombre_phrases}")
        print(f"Longueur moyenne des phrases (mots) : {longueur_moyenne_phrase:.2f}")
        print("\nMots les plus courants :")
        for mot, freq in mots_plus_courants:
            print(f"{mot}: {freq} fois")
        
        # Bonus : Nombre de mots uniques
        mots_uniques = len(set(mots))
        print(f"\nNombre de mots uniques : {mots_uniques}")
        
        return {
            'nombre_mots': nombre_mots,
            'nombre_phrases': nombre_phrases,
            'longueur_moyenne_phrase': longueur_moyenne_phrase,
            'mots_plus_courants': mots_plus_courants,
            'mots_uniques': mots_uniques
        }
    
    except FileNotFoundError:
        print(f"Erreur : Le fichier {MTRX_Présentation.txt} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Remplacer 'texte.txt' par le chemin de votre fichier
    fichier_texte = 'MTRX_Présentation.txt'
    analyser_texte(fichier_texte)

