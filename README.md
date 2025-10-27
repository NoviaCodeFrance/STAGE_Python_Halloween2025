# 🎃 La chasse aux Bonbons Hantée (édition 2025)

Bienvenue dans ce projet spécial Halloween ! Cette application est conçue pour vous initier à la programmation en Python de manière amusante et créative.

## 📖 À propos du projet

Ce script Python est un **jeu d'aventure textuel** dans lequel vous explorez une maison hantée. Votre mission est simple : braver vos peurs, explorer les pièces sombres et **trouver tous les bonbons** cachés dans la maison.

Mais attention ! Un fantôme se déplace de pièce en pièce. Si vous le croisez trop souvent, la peur aura raison de vous !

Ce projet est une excellente occasion de découvrir des concepts clés de Python :
* L'utilisation de **dictionnaires** pour construire le monde du jeu (la maison et ses pièces).
* La gestion de **listes** pour l'inventaire du joueur et les objets dans les pièces.
* Le suivi de l'état du jeu avec des **variables** (`positionJoueur`, `peurJoueur`, etc.).
* La création d'une boucle de jeu principale avec `while`.
* L'interaction avec l'utilisateur grâce à la fonction `input()`.

## 🚀 Comment lancer l'application ?

Pour faire fonctionner le projet, c'est très simple !

1.  **Assurez-vous d'avoir Python installé** sur votre ordinateur.
2.  Clonez ou téléchargez ce dépôt sur votre machine.
3.  Ouvrez un terminal (ou une invite de commandes) dans le dossier du projet.
4.  Exécutez la commande suivante (en remplaçant `jeu_halloween.py` par le nom de votre fichier) :
    ```bash
    python jeu_halloween.py
    ```
5.  Et voilà ! Laissez-vous guider par les descriptions et tentez de survivre. 🦇

## 🛠️ Devoir à faire : Devenez de vrais sorciers du code !

Le jeu fonctionne, mais un vrai développeur ne s'arrête jamais là ! Voici 4 missions pour transformer notre jeu en une expérience encore plus terrifiante et professionnelle. À vous de jouer !

### Mission 1 : Pardonner les fautes de frappe

Parfois, on tape vite et on fait des erreurs comme "aler" au lieu de "aller". Pour l'instant, notre jeu ne comprend pas et affiche "Commande inconnue". On va lui apprendre à être plus malin !

**🎯 Objectif :** Utiliser une bibliothèque pour que le jeu devine la bonne commande même s'il y a une petite faute de frappe.

**Comment faire ?**

1.  **Installer une bibliothèque magique :** On va utiliser `thefuzz`, qui est super pour comparer des chaînes de caractères. Ouvre un terminal et tape cette commande :
    ```bash
    pip install thefuzz[python-Levenshtein]
    ```

2.  **Importer le sortilège :** Tout en haut de ton fichier Python, ajoute cette ligne pour pouvoir utiliser la bibliothèque :
    ```python
    from thefuzz import process
    ```

3.  **Modifier la boucle de jeu :** On va changer la façon dont le jeu lit tes commandes. Repère la boucle `while not partieTerminee:` et trouve la ligne `commande = mots[0]`. On va remplacer tout ce qui suit jusqu'au premier `if`.

    * **Le code AVANT :**
        ```python
        # ... dans la boucle while ...
        commande = mots[0]

        if commande == "quitter":
            # ...
        elif commande == "aller":
            # ...
        # etc.
        ```

    * **Le code APRÈS (à mettre à la place) :**
        ```python
        # ... dans la boucle while ...
        commandes_possibles = ["aller", "prendre", "inventaire", "quitter", "aide"]
        commande_brute = mots[0]
        
        # On cherche la commande la plus ressemblante !
        resultat = process.extractOne(commande_brute, commandes_possibles)
        
        if resultat: # On vérifie si on a trouvé une correspondance
            commande = resultat[0] # Le mot le plus proche
            score = resultat[1]   # Le score de ressemblance (de 0 à 100)
        else:
            score = 0

        # Si la ressemblance est assez bonne (plus de 70%), on accepte !
        if score < 70:
            print("Commande inconnue ! Tape 'aide' si tu es perdu.")
            continue # On passe au tour suivant sans rien faire

        # Maintenant, le reste du code fonctionne comme avant !
        if commande == "quitter":
            print("Merci d'avoir joué !")
            partieTerminee = True
        elif commande == "aller":
            # ... le reste du code pour "aller" ne change pas
        # etc.
        ```

---

### Mission 2 : Créer une ambiance avec un effet "machine à écrire"

Pour rendre l'histoire plus captivante, on va faire en sorte que le texte s'affiche lettre par lettre, comme si une vieille machine à écrire hantée l'imprimait.

**🎯 Objectif :** Créer une fonction qui affiche le texte progressivement.

**Comment faire ?**

1.  **Importer le temps :** On a besoin de la bibliothèque `time` pour faire des petites pauses. Ajoute-la en haut de ton fichier :
    ```python
    import time
    ```

2.  **Créer la fonction "machine à écrire" :** Juste après tes variables du début (par exemple, après la section `COULEURS`), ajoute cette nouvelle fonction. Elle va prendre un texte en entrée et l'afficher caractère par caractère.
    ```python
    def machine_a_ecrire(texte):
        for char in texte:
            print(char, end='', flush=True)
            time.sleep(0.03) # Petite pause de 0.03 secondes
        print() # Pour passer à la ligne à la fin
    ```

3.  **Remplacer les `print()` :** Maintenant, cherche dans ton code les `print()` qui affichent les descriptions des pièces ou les messages importants, et remplace-les par `machine_a_ecrire()`.
    * **Exemple AVANT :**
        ```python
        def pieceActuelle():
            # ...
            print(piece["description"])
            # ...
        ```
    * **Exemple APRÈS :**
        ```python
        def pieceActuelle():
            # ...
            machine_a_ecrire(piece["description"])
            # ...
        ```

---

### Mission 3 : Le "Screamer" du Game Over ! 😱

Quand le joueur perd, il faut le surprendre ! On va vider la console et afficher un gros message effrayant pour un final mémorable.

**🎯 Objectif :** Nettoyer l'écran et afficher un message de Game Over en grand.

**Comment faire ?**

1.  **Importer le système d'exploitation :** On a besoin de la bibliothèque `os` pour interagir avec le terminal. Ajoute-la en haut du fichier.
    ```python
    import os
    ```

2.  **Modifier le Game Over :** Trouve la fonction `tourDuFantome()`. À l'intérieur, repère le bloc de code qui s'active quand le joueur a trop peur (`if peurJoueur >= 3:`).
    ```python
    # ... dans tourDuFantome() ...
    if peurJoueur >= 3:
        # ---- C'EST ICI QU'ON MET LE SCREAMER ! ----
        
        # 1. On nettoie l'écran (cls pour Windows, clear pour Mac/Linux)
        os.system('cls' if os.name == 'nt' else 'clear')

        # 2. On affiche un message terrifiant ! Tu peux même le dessiner.
        message_game_over = """
             ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
            ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
            ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
            ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
            ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
             ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
        ... LE FANTÔME T'A EU ...
        """
        print(f"{COULEURS['danger']}{message_game_over}{COULEURS['fin']}")
        
        # Le reste du code ne change pas
        partieTerminee = True
    ```

---

### Mission 4 : Une maison haute en couleurs ! 🎨

Seuls certains textes sont colorés. Pourquoi ne pas tout colorer pour rendre le jeu plus lisible et plus joli ?

**🎯 Objectif :** Utiliser le dictionnaire `COULEURS` pour colorer tous les textes affichés au joueur.

**Comment faire ?**

1.  **Ajouter des couleurs :** Tu peux enrichir le dictionnaire `COULEURS` avec de nouvelles teintes si tu veux ! Par exemple, une couleur pour les messages d'aide.
    ```python
    COULEURS = {
        "titre": "\033[95m",
        "description": "\033[93m",
        "objet": "\033[92m",
        "sortie": "\033[94m",
        "danger": "\033[91m",
        "aide": "\033[96m", # Cyan pour l'aide
        "fin": "\033[0m"
    }
    ```

2.  **Colorer les `print()` restants :** Passe en revue tout ton code. Chaque fois que tu vois un `print()` qui parle au joueur, utilise une f-string pour y ajouter de la couleur.
    * **Exemple AVANT (dans la commande "aide") :**
        ```python
        elif commande == "aide":
            print("--- COMMANDES POSSIBLES ---")
            print("- aller [direction] : pour te déplacer...")
        ```
    * **Exemple APRÈS :**
        ```python
        elif commande == "aide":
            print(f"{COULEURS['aide']}--- COMMANDES POSSIBLES ---{COULEURS['fin']}")
            print(f"- {COULEURS['titre']}aller [direction]{COULEURS['fin']} : pour te déplacer...")
            # Et ainsi de suite pour chaque ligne !
        ```
    N'oublie pas les messages comme "Tu as pris : ..." ou "Ton inventaire est vide.".

---

### 🏆 Récompense Spéciale ! 🏆

Pour tous les courageux développeurs qui réussiront **au moins 3 de ces 4 missions**, vous recevrez :

1.  Le **Diplôme Officiel du Développeur le plus Horrifique** d'Halloween 2025 !
2.  Une **heure d'atelier particulier de programmation** avec moi, pour créer ce que vous voulez. Ce trésor est valable jusqu'en **juillet 2026**.

Bon courage, et que le code soit avec vous ! 🎃💻

Amusez-vous bien et joyeux Halloween ! 🎃🧛‍♂️
