{
"title": "Mises à jour de l'enregistreur de transaction",
"date": "2024-06-12",
"url": "/changelog/juin-2024-mises-a-jour-enregistreur-transaction",
"translationKey": "https://www.uptrends.com/changelog/june-2024-transaction-recorder-updates"
}

Dans le cadre de la mise à jour de notre [enregistreur de transaction]({{< ref path="/features/transaction-recorder" lang="fr" >}}), nous avons procédé à une refonte graphique et ajouté les fonctionnalités suivantes :

- Le navigateur de l'enregistreur de transaction dispose désormais d'un nouveau menu sensible au contexte, accessible par un clic droit, qui permet aux utilisateurs d'ajouter les actions [Survol]({{< ref path="/support/kb/synthetic-monitoring/transactions/page-interactions#hover" lang="fr" >}}), [Attendre l'élément]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks#wait-for-element" lang="fr" >}}) et [Tester le contenu du document]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks#test-document-content" lang="fr" >}}) (lorsque le texte sur la page est en surbrillance) tout en effectuant l'enregistrement. Ces actions ne doivent plus être ajoutées dans un second temps !
- Il est désormais possible d'ajouter les actions [Évènement clé]({{< ref path="/support/kb/synthetic-monitoring/transactions/page-interactions#key-event" lang="fr" >}}) directement depuis l'interface de l'enregistreur. L'enregistreur ne peut pas enregistrer des actions comme la pression de la touche Entrée après la saisie des identifiants, mais cette action peut maintenant être ajoutée au moyen du bouton **"+ Add keyboard action"** (+ Ajouter une action clavier) dans l'enregistreur.

![Menu de l'enregistreur accessible au moyen d'un clic droit](/img/content/scr-recorder-context-menu.min.png)