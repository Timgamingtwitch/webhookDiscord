import os
import requests
from datetime import datetime

# Nom du bot
bot_name = "Roi Bubu"

# Création du dossier "config" s'il n'existe pas
if not os.path.exists("config"):
    os.mkdir("config")

# Création du fichier "message.txt" s'il n'existe pas
if not os.path.exists("config/message.txt"):
    open("config/message.txt", "w").close()

# Lecture du contenu du fichier "config.txt" pour obtenir le webhook Discord
webhook_url = ""
if os.path.exists("config/config.txt"):
    with open("config/config.txt", "r") as f:
        for line in f:
            if line.startswith("webhook="):
                webhook_url = line[len("webhook="):].strip()
                break

# Si le webhook Discord n'est pas défini dans le fichier "config.txt", demander à l'utilisateur de le saisir
if not webhook_url:
    webhook_url = input("Entrez le lien du webhook Discord : ")
    with open("config/config.txt", "w") as f:
        f.write(f"webhook={webhook_url}\n")

# Envoi du message Discord
try:
    with open("config/message.txt", "r") as f:
        message = f.read().strip()
    embed = {
        "title": f"Une fonctionnalité cachée de Discord !!",
        "description": f"Hé mec, t'as déjà vu ça ? Y'a un truc super cool sur Discord, tu peux mettre une réaction sous un message ! Ouais, ouais, je sais, ça paraît fou, mais tout le monde le fait déjà, j'suis sûrement le dernier à le découvrir haha. Mais bon, si t'es comme moi et que t'es un peu à la ramasse, tu peux faire un petit clic droit sous mon message pour ajouter une réactions. Et voilà, le tour est joué ! Facile, non ?",
        "color": 16776960,
        "footer": {
            "text": f"Signées; {bot_name}  28/04/2023 à 11:27:53"
        }
    }
    data = {
        "username": bot_name,
        "avatar_url": "", # URL de l'avatar du bot
        "content": "",
        "embeds": [embed]
    }
    response = requests.post(webhook_url, json=data)
    response.raise_for_status()
    print("Le message a été envoyé avec succès à Discord !")
except Exception as e:
    print(f"Une erreur s'est produite lors de l'envoi du message à Discord : {str(e)}")

# Demander à l'utilisateur d'appuyer sur "Entrée" 5 fois pour fermer le programme
for i in range(3):
    input("Appuyez sur Entrée pour continuer...")
