import random

# VARIABLES DU JEU
positionJoueur = "Hall d'entrée"
positionFantome = "Cave"
inventaire = []
partieTerminee = False
peurJoueur = 0
bonbonsGagnes = 0

LISTE_BONBONS = ["araignée en sucre", "nougat", "caramel", "chocolat", "sucette", "bonbon au citron"]

COULEURS = {
    "titre": "\033[95m",       # Rose/Violet
    "description": "\033[93m", # Jaune
    "objet": "\033[92m",       # Vert
    "sortie": "\033[94m",      # Bleu
    "danger": "\033[91m",      # Rouge
    "fin": "\033[0m"           # Remet la couleur par défaut
}

maison = {
    # --- Rez-de-chaussée ---
    "Hall d'entrée": {
        "description": "Tu es dans le hall sombre et poussiéreux. Un grand escalier en bois monte vers le nord et une porte massive se trouve au sud (elle est fermée à clé derrière toi).",
        "sorties": {
            "nord": "Grand Escalier"
        },
        "objets": ["araignée en sucre"]
    },
    "Grand Escalier": {
        "description": "Un escalier monumental qui craque sous tes pieds. Il monte vers le premier étage et descend vers le hall. Des portes se trouvent à l'est et à l'ouest.",
        "sorties": {
            "sud": "Hall d'entrée",
            "est": "Salon", 
            "ouest": "Salle à manger", 
            "haut": "Couloir de l'étage"
        },
        "objets": []
    },
    "Salon": {
        "description": "Tu es dans un grand salon. Les meubles sont recouverts de draps blancs. Une cheminée éteinte est pleine de suie. Une porte est à l'ouest et une autre, plus petite, est à l'est.",
        "sorties": {
            "ouest": "Grand Escalier",
            "est": "Bibliothèque"
        },
        "objets": ["nougat", "vieille clé"]
    },
    "Bibliothèque": {
        "description": "Des milliers de livres aux reliures abîmées remplissent les étagères du sol au plafond. Une odeur de vieux papier flotte dans l'air.",
        "sorties": {
            "ouest": "Salon"
        },
        "objets": ["lettre moisie"]
    },
    "Salle à manger": {
        "description": "Une longue table en bois est dressée pour un repas qui n'a jamais eu lieu. La vaisselle est couverte de poussière. Il y a une porte à l'est et une autre au nord.",
        "sorties": {
            "est": "Grand Escalier",
            "nord": "Cuisine"
        },
        "objets": ["caramel"]
    },
    "Cuisine": {
        "description": "La cuisine est en désordre. Une porte mène au sud, une trappe est dans le sol et une porte vitrée pleine de buée donne sur l'est.",
        "sorties": {
            "sud": "Salle à manger",
            "bas": "Cave",
            "est": "Jardin"
        },
        "objets": ["couteau de cuisine"]
    },
    "Jardin": {
        "description": "Un jardin laissé à l'abandon. Des ronces grimpent sur une vieille statue de pierre. La seule entrée semble être la porte de la cuisine à l'ouest.",
        "sorties": {
            "ouest": "Cuisine"
        },
        "objets": ["citrouille", "chocolat"]
    },
    
    # --- Sous-sol ---
    "Cave": {
        "description": "Une cave froide et humide. L'air sent la terre et le vin tourné. Des tonneaux sont alignés contre les murs.",
        "sorties": {
            "haut": "Cuisine"
        },
        "objets": ["bouteille vide"]
    },
    
    # --- Premier étage ---
    "Couloir de l'étage": {
        "description": "Tu es dans le couloir sombre de l'étage. Au plafond, tu remarques une trappe avec une corde qui pend. Des portes mènent au nord, à l'est et à l'ouest.",
        "sorties": {
            "sud": "Grand Escalier",
            "nord": "Chambre principale",
            "est": "Chambre d'enfant",
            "ouest": "Salle de bain",
            "haut": "Grenier"
        },
        "objets": []
    },
    "Chambre principale": {
        "description": "Une grande chambre avec un lit à baldaquin recouvert de toiles d'araignées. La fenêtre est brisée et laisse entrer un vent glacial.",
        "sorties": {
            "sud": "Couloir de l'étage"
        },
        "objets": ["sucette", "boîte à musique"]
    },
    "Chambre d'enfant": {
        "description": "Une petite chambre avec un cheval à bascule qui grince tout seul dans un coin. Des jouets cassés jonchent le sol.",
        "sorties": {
            "ouest": "Couloir de l'étage"
        },
        "objets": ["ours en peluche"]
    },
    "Salle de bain": {
        "description": "Le miroir au-dessus du lavabo est fêlé. De l'eau goutte lentement d'un robinet rouillé, créant le seul bruit ambiant.",
        "sorties": {
            "est": "Couloir de l'étage"
        },
        "objets": ["peigne en argent"]
    },

    # --- Grenier ---
    "Grenier": {
        "description": "Un grenier étouffant rempli de vieux meubles recouverts de draps. Une petite lucarne laisse passer un rayon de lune. Une échelle descend vers le sud.",
        "sorties": {
            "sud": "Couloir de l'étage"
        },
        "objets": ["bonbon au citron", "vieux journal"]
    }
}

print("🎃 Bienvenue dans la chasse aux Bonbons Hantée !")
print("Ta mission: trouver tous les bonbons.")

pseudo = input("Quel est ton nom, jeune aventurier ? ")
print("Ravi de te rencontrer", pseudo, "!")

### ETHAN
### ICI

def pieceActuelle():
    piece = maison[positionJoueur]
    print("\n-----------------")
    print(f"Tu es dans: {COULEURS['titre']}{positionJoueur}{COULEURS['fin']}")
    print(piece["description"])

    print("\n")
    objets = piece["objets"]
    if objets:
        print("Tu vois ici:", ", ".join(objets))
        print("\n")

    print("Sorties possibles:")
    for direction, destination in piece["sorties"].items():
        print(f"- {direction} -> {COULEURS['sortie']}{destination}{COULEURS['fin']}")
    print("\n-----------------\n")

def tourDuFantome():
    global positionFantome, positionJoueur, partieTerminee, peurJoueur
    sortiesFantome = list(maison[positionFantome]["sorties"].values())
    positionFantome = random.choice(sortiesFantome)

    if positionFantome == positionJoueur:
        peurJoueur += 1
        print("\nBOO ! 👻 Le fantôme te traverse ! Ton corps se glace de peur.")

        if peurJoueur >= 3:
            print("GAME OVER")
            print("La peur a eu raison de toi. Tu t'effondres, incapable de continuer...")
            partieTerminee = True
        else:
            print(f"Niveau de peur: {peurJoueur}/3. Fais attention !")

pieceActuelle()

while not partieTerminee:
    # Demander au joueur ce qu'il veut faire
    action = input("> ").lower()
    mots = action.split()

    if not mots:
        print("Tu dois dire quelque chose !")
        continue

    commande = mots[0]

    # Gérer les actions du joueur
    if commande == "quitter":
        print("Merci d'avoir joué !")
        partieTerminee = True
    elif commande == "aller":
        if len(mots) > 1:
            direction = mots[1]

            if direction in maison[positionJoueur]["sorties"]:
                positionJoueur = maison[positionJoueur]["sorties"][direction]
                pieceActuelle()
                tourDuFantome()
            else:
                print("Tu ne peux pas aller là !")
        else:
            print("Tu dois dire où tu veux aller (ex: nord, sud, est, ouest, haut, bas).")
    elif commande == "prendre":
        objet = " ".join(mots[1:])
        if objet in maison[positionJoueur]["objets"]:
            inventaire.append(objet)
            maison[positionJoueur]["objets"].remove(objet)
            print("Tu as pris:", objet)

            if objet in LISTE_BONBONS:
                bonbonsGagnes += 1
                print(f"C'est un bonbon ! Tu en as maintenant {bonbonsGagnes}/5.")
                if bonbonsGagnes >= 5:
                   print(f"\n🏆 FÉLICITATIONS, {pseudo} !") 
                   print("Tu as collecté assez de bonbons et tu t'échappes de la maison hantée !")
                   partieTerminee = True
        else:
            print("Cet objet n'est pas ici !")
    elif commande == "inventaire":
        if inventaire:
            print("Ton inventaire contient:", ", ".join(inventaire))
        else:
            print("Ton inventaire est vide.")
    elif commande == "aide":
        print("--- COMMANDES POSSIBLES ---")
        print("- aller [direction] : pour te déplacer (nord, sud, est, ouest, haut, bas).")
        print("- prendre [objet] : prendre un objet dans la pièce.")
        print("- inventaire : pour regarder ton inventaire.")
        print("- aide : pour afficher la liste des commandes.")
        print("- quitter : pour arrêter le jeu.")
        print("----------------------------")
    else:
        print("Commande inconnue ! Tape 'aide' si tu es perdu.")