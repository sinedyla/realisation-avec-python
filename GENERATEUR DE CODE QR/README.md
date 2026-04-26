# 📱 Générateur de Code QR

Un projet Python simple et efficace pour générer des codes QR à partir d'URLs ou de texte.

## 📋 Table des matières

- [Description](#description)
- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du projet](#structure-du-projet)
- [Exemples](#exemples)
- [Troubleshooting](#troubleshooting)
- [Améliorations futures](#améliorations-futures)

## 📝 Description

Ce projet permet de générer des codes QR (Quick Response) à partir de liens ou de texte fourni par l'utilisateur. Le code QR généré est sauvegardé sous forme d'image PNG sur le disque dur.

### À propos des codes QR

Les codes QR sont des codes-barres bidimensionnels qui peuvent stocker des informations lisibles par les appareils mobiles. Ils sont largement utilisés pour :

- Partager des URLs
- Partager des données de contact
- Stocker du texte
- Créer des raccourcis vers des applications

## ✨ Fonctionnalités

✅ **Génération simple** - Interface interactive en ligne de commande  
✅ **Flexibilité** - Accepte toute chaîne de caractères (URLs, texte, etc.)  
✅ **Format PNG** - Sauvegarde en format image standard  
✅ **Code optimisé** - Utilisation de la libraire `qrcode` Python  
✅ **Chemin personnalisable** - Possibilité de modifier le chemin de sauvegarde

## 🔧 Prérequis

- **Python** : Version 3.6 ou supérieure
- **Système d'exploitation** : Windows, macOS ou Linux
- **Bibliothèque qrcode** : Pour la génération des codes QR
- **Bibliothèque Pillow** : Dépendance de qrcode pour la manipulation d'images

## 📦 Installation

### 1. Cloner ou télécharger le projet

```bash
# Si vous utilisez Git
git clone <url-du-repository>
cd "GENERATEUR DE CODE QR"

# Sinon, téléchargez directement les fichiers
```

### 2. Installer les dépendances

```bash
# Windows
pip install qrcode[pil]

# macOS / Linux
pip3 install qrcode[pil]
```

Cela installera automatiquement :

- `qrcode` : Bibliothèque de génération de codes QR
- `Pillow` : Bibliothèque de manipulation d'images

### 3. Vérifier l'installation

```bash
python -c "import qrcode; print('Installation réussie!')"
```

## 🚀 Utilisation

### Lancer le programme

```bash
python main.py
```

### Étapes d'utilisation

1. Exécutez le script
2. Entrez le lien ou le texte à encoder
3. Le programme génère le code QR
4. L'image est sauvegardée à l'emplacement spécifié
5. Un message de confirmation s'affiche

### Exemple d'exécution

```
Veuillez entrer le lien : https://www.google.com
Votre QR Code a été généré dans le chemin fourni : C:\Users\sined\OneDrive - Université Cheikh Anta DIOP de DAKAR\Bureau\Mes Projets\QR Code\votre_qrcode.png
```

## 📂 Structure du projet

```
GENERATEUR DE CODE QR/
├── main.py              # Script principal
└── README.md            # Documentation (ce fichier)
```

## 💡 Exemples

### Exemple 1 : Encoder une URL

```
Input:  https://github.com
Output: Code QR contenant le lien GitHub
```

### Exemple 2 : Encoder du texte simple

```
Input:  Bonjour le monde!
Output: Code QR contenant ce message
```

### Exemple 3 : Encoder une adresse email

```
Input:  mailto:contact@example.com
Output: Code QR que vous pouvez scanner pour envoyer un email
```

## 🔍 Détails techniques

### Code source expliqué

```python
import qrcode

# Demander l'entrée utilisateur
lien = input("Veuillez entrer le lien : ").strip()

# Chemin où sauvegarder le code QR
chemin = "C:\\Users\\sined\\...\\votre_qrcode.png"

# Créer une instance de QRCode
qr = qrcode.QRCode()

# Ajouter les données à encoder
qr.add_data(lien)

# Générer l'image
image = qr.make_image()

# Sauvegarder l'image
image.save(chemin)

# Afficher un message de confirmation
print(f"Votre QR Code a été généré dans le chemin fourni : {chemin}")
```

### Paramètres modifiables

Vous pouvez personnaliser le comportement en modifiant :

```python
# Ajouter des paramètres à QRCode() pour personnaliser :
qr = qrcode.QRCode(
    version=1,              # Taille du code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,            # Taille des boîtes en pixels
    border=4                # Bordure (en boîtes)
)
```

## ⚠️ Troubleshooting

### Erreur : "ModuleNotFoundError: No module named 'qrcode'"

**Solution** : Installez la dépendance

```bash
pip install qrcode[pil]
```

### Erreur : "FileNotFoundError" ou "PermissionError"

**Cause** : Le chemin de sauvegarde n'existe pas ou n'est pas accessible  
**Solution** :

1. Vérifiez que le dossier existe
2. Modifiez le chemin dans le code
3. Assurez-vous d'avoir les permissions d'accès

```python
# Exemple : Sauvegarde dans le répertoire courant
chemin = "votre_qrcode.png"
```

### Erreur : "UnicodeDecodeError"

**Cause** : Problème d'encodage des caractères  
**Solution** : Vérifiez que votre fichier est en UTF-8

### Le fichier image est vide ou corrompu

**Solution** :

- Assurez-vous que le chemin est valide
- Vérifiez l'espace disque disponible
- Réessayez avec un chemin plus simple

## 🔐 Limitations actuelles

- ⚠️ Le chemin est codé en dur dans le script
- ⚠️ Pas de gestion d'erreurs avancée
- ⚠️ Interface minimaliste (ligne de commande uniquement)
- ⚠️ Pas de validation de l'entrée utilisateur

## 🎯 Améliorations futures

Les améliorations suivantes pourraient être apportées :

1. **Interface graphique (GUI)**
   - Utiliser tkinter ou PyQt pour une meilleure UX
   - Ajouter un bouton de sélection de dossier

2. **Configuration personnalisée**
   - Fichier de configuration pour les paramètres
   - Choix du chemin de sauvegarde interactif
   - Options de taille et de bordure

3. **Validation avancée**
   - Vérifier que l'URL est valide
   - Gérer les caractères spéciaux
   - Limiter la longueur du texte

4. **Fonctionnalités additionnelles**
   - Support du logo au centre du code QR
   - Génération en batch (plusieurs codes QR)
   - Export en formats multiples (SVG, PDF)
   - Historique des codes générés

5. **Robustesse**
   - Gestion complète des erreurs
   - Messages d'erreur clairs
   - Logs d'exécution

## 📞 Support et contribution

Si vous rencontrez des problèmes ou avez des suggestions :

1. Vérifiez la section [Troubleshooting](#troubleshooting)
2. Consultez la [documentation qrcode](https://github.com/lincolnloop/python-qrcode)
3. Créez une issue si le problème persiste

## 📄 Licence

Ce projet est fourni à titre d'exemple éducatif.

---

**Dernière mise à jour** : Avril 2026  
**Auteur** : FARA  
**Langage** : Python 3.6+
