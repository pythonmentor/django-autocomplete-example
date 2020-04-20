# Exemple d'utilisation de l'autocomplétion de jquery-ui dans un projet django

Ce dépôt de code montre comment utiliser la méthode autocomplete de la 
bibliothèque jquery dans sein d'un projet django. L'autocomplétion est ici
implémentée à l'aide d'une vue d'autocomplétion implémentée dans 
autocomplete.views.complete(). Cette vue prend en entrée un paramètre GET
nommé `term`. On récupère donc ce terme et on l'utilise pour chercher les 
objets correspondant en base et en faire une liste à revoyer dans une 
JsonResponse,

## Installation

Pour tester ce projet de démonstration, je suppose ici que vous avez Python
d'installer ainsi que pipenv. Si ce n'est pas le cas, pipenv peut être 
installé à l'aide de pip ou de pip3 selon votre système d'exploitation. 

1. Cloner ce repo avec `git clone https://github.com/pythonmentor/django-autocomplete-example.git`
2. Se rendre à la racine avec `cd django_autocomplete-example`
3. Installer les dépendances avec `pipenv install`
4. Activer l'environnement virtuel avec `pipenv shell`
5. Exécuter les migrations avec `python manage.py migrate`
6. Lancer le server de développement avec `python manage.py runserver`