{
  "hero": {
    "title": "Explication des mesures de temps"
  },
  "title": "Explication des mesures de temps",
  "summary": "Explication des mesures de temps de la surveillance de site web Uptrends",
  "url": "/support/kb/dashboards-et-rapports/dashboards/explication-mesure-de-temps",
  "translationKey": "https://www.uptrends.com/support/kb/reporting/explanation-total-time-metrics"
}

L'une des fonctions les plus utiles du service Uptrends est sa capacité à examiner en détail les données de disponibilité et de performance de vos sites web, serveurs et applications Web. Mais parfois il peut être difficile de savoir exactement ce que ces données représentent en fait !

Ci-dessous vous allez prendre connaissance des différents "*Mesures de Temps total*" et ce qu'ils signifient réellement :

## Résolution

Le **temps de résolution** est le temps qu'il faut pour traduire un nom de domaine ou une URL vers l'adresse IP correspondante.

Pour chaque moniteur, là où un URL ou un nom de domaine a été spécifié pour la connexion à une page Web ou un serveur, nous aurons besoin d'effectuer une traduction par le biais d'une requête DNS. (Exactement comme fait votre navigateur lorsqu'il charge une page web !)

## Temps de connexion

Le **temps de connexion** représente le temps qu'il faut pour se connecter à l'adresse IP de votre page Web ou de votre serveur.

## Le temps de téléchargement

Le **temps de téléchargement** débute après la connexion à votre page Web ou un serveur, au moment où la demande de téléchargement est effectuée. Il indique le temps écoulé entre le début de la demande effective et le moment où le téléchargement est terminé.

## Temps total

Le **temps total** est le temps qu'il faut pour effectuer une vérification du moniteur. (C'est la somme du temps de résolution, du temps de connexion et du temps de téléchargement.)
