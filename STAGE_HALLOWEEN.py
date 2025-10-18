# VARIABLES DU JEU
positionJoueur = "Hall d'entrée"
inventaire = []
partieTerminee = False

maison = {
    # --- Rez-de-chaussée ---
    "Hall d'entrée": {
        "description": "Tu es dans le hall sombre et poussiéreux. Un grand escalier en bois monte vers le nord et une porte massive se trouve au sud (elle est fermée à clé derrière toi).",
        "sorties": {
            "nord": "Grand Escalier"
        }
    },
    "Grand Escalier": {
        "description": "Un escalier monumental qui craque sous tes pieds. Il monte vers le premier étage et descend vers le hall. Des portes se trouvent à l'est et à l'ouest.",
        "sorties": {
            "sud": "Hall d'entrée",
            "est": "Salon", 
            "ouest": "Salle à manger", 
            "haut": "Couloir de l'étage"
        }
    },
    "Salon": {
        "description": "Tu es dans un grand salon. Les meubles sont recouverts de draps blancs. Une cheminée éteinte est pleine de suie. Une porte est à l'ouest et une autre, plus petite, est à l'est.",
        "sorties": {
            "ouest": "Grand Escalier",
            "est": "Bibliothèque"
        }
    },
    "Bibliothèque": {
        "description": "Des milliers de livres aux reliures abîmées remplissent les étagères du sol au plafond. Une odeur de vieux papier flotte dans l'air.",
        "sorties": {
            "ouest": "Salon"
        }
    },
    "Salle à manger": {
        "description": "Une longue table en bois est dressée pour un repas qui n'a jamais eu lieu. La vaisselle est couverte de poussière. Il y a une porte à l'est et une autre au nord.",
        "sorties": {
            "est": "Grand Escalier",
            "nord": "Cuisine"
        }
    },
    "Cuisine": {
        "description": "La cuisine est en désordre. Une porte mène au sud, une trappe est dans le sol et une porte vitrée pleine de buée donne sur l'est.",
        "sorties": {
            "sud": "Salle à manger",
            "bas": "Cave",
            "est": "Jardin"
        }
    },
    "Jardin": {
        "description": "Un jardin laissé à l'abandon. Des ronces grimpent sur une vieille statue de pierre. La seule entrée semble être la porte de la cuisine à l'ouest.",
        "sorties": {
            "ouest": "Cuisine"
        }
    },
    
    # --- Sous-sol ---
    "Cave": {
        "description": "Une cave froide et humide. L'air sent la terre et le vin tourné. Des tonneaux sont alignés contre les murs.",
        "sorties": {
            "haut": "Cuisine"
        }
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
        }
    },
    "Chambre principale": {
        "description": "Une grande chambre avec un lit à baldaquin recouvert de toiles d'araignées. La fenêtre est brisée et laisse entrer un vent glacial.",
        "sorties": {
            "sud": "Couloir de l'étage"
    }
    },
    "Chambre d'enfant": {
        "description": "Une petite chambre avec un cheval à bascule qui grince tout seul dans un coin. Des jouets cassés jonchent le sol.",
        "sorties": {
            "ouest": "Couloir de l'étage"
        }
    },
    "Salle de bain": {
        "description": "Le miroir au-dessus du lavabo est fêlé. De l'eau goutte lentement d'un robinet rouillé, créant le seul bruit ambiant.",
        "sorties": {
            "est": "Couloir de l'étage"
        }
    },

    # --- Grenier ---
    "Grenier": {
        "description": "Un grenier étouffant rempli de vieux meubles recouverts de draps. Une petite lucarne laisse passer un rayon de lune. Une échelle descend vers le sud.",
        "sorties": {
            "sud": "Couloir de l'étage"
        }
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
    print("Tu es dans:", positionJoueur)
    print(piece["description"])

    sorties = piece["sorties"].keys()
    print("Sorties possibles:", ", ".join(sorties))
    print("\n-----------------\n")

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
            else:
                print("Tu ne peux pas aller là !")
        else:
            print("Tu dois dire où tu veux aller (ex: nord, sud, est, ouest, haut, bas).")


    elif commande == "aide":
        print("--- COMMANDES POSSIBLES ---")
        print("- aller [direction] : pour te déplacer (nord, sud, est, ouest, haut, bas).")
        print("- aide : pour afficher la liste des commandes.")
        print("- quitter : pour arrêter le jeu.")
        print("----------------------------")
    else:
        print("Commande inconnue ! Tape 'aide' si tu es perdu.")