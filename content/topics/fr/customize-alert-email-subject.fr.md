{
"hero": {
"title": "Personnalisation de l'objet et de la mise en forme des e-mails d'alerte"
},
"title": "Personnalisation de l'objet et de la mise en forme des e-mails d'alerte",
"summary": "Cet article vous explique comment personnaliser l'objet des e-mails d'alerte et activer le format HTML.",
"url": "/support/kb/alerter/personnalisation-objet-email-alerte",
"translationKey": "https://www.uptrends.com/support/kb/alerting/customize-alert-email-subject",
"tableofcontents": true,
"sectionlist": true
}

Pour suivre et catégoriser facilement par e-mail le statut de vos moniteurs, Uptrends vous permet de personnaliser les objets des e-mails d'alerte au moyen de l'intégration **Alertes par e-mail**. Vous pouvez recevoir des alertes pour des moniteurs individuels et des groupes de moniteurs, selon les erreurs générées au cours d'une période donnée. Tout objet que vous configurez sera appliqué à tous les e-mails d'alerte sortants.

Pour personnaliser l'objet de l'e-mail :

1. Ouvrez le menu {{< AppElement type="menuitem" >}} Alertes > Intégrations {{< /AppElement >}}, puis l'intégration **Alertes par e-mail**.
2. Cochez la case **Personnaliser l'intégration** pour afficher l'onglet {{< AppElement type="tab" >}} Personnalisations {{< /AppElement >}}.
3. Ouvrez l'onglet {{< AppElement type="tab" >}} Personnalisations {{< /AppElement >}}.
4. Pour recevoir des e-mails au format HTML, reportez-vous aux instructions concernant le [format HTML]({{< ref path="/support/kb/alerting/customize-alert-email-subject#html-formatting" lang="fr" >}}). Autrement, passez à l'étape suivante.
5. Cochez les cases correspondant aux [types d'alerte]({{< ref path="/support/kb/alerting/integrations/custom-integrations/message-types" lang="fr" >}}) (Erreur, Rappel, OK) pour personnaliser l'objet de l'alerte envoyé pour un ou plusieurs moniteurs.
6. Saisissez le nouvel objet. Vous pouvez utiliser de nombreuses variables, comme les [variables automatiques]({{< ref path="/support/kb/synthetic-monitoring/transactions/automatic-variables" lang="fr" >}}) et les [variables système d'alerte]({{< ref path="/support/kb/alerting/integrations/custom-integrations/alerting-system-variables" lang="fr" >}}) dans l'objet de l'e-mail. Par exemple, utilisez les variables `{{@monitor.name}}` et `{{@alert.timestamp}}` pour faire référence au nom du moniteur et à la date et à l'heure de l'alerte.

7. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} pour confirmer les changements.


![Personnalisation de l'objet des e-mails d'alerte](/img/content/scr-customizing-email-subjects_020624.min.png)

## E-mail au format HTML

Vous pouvez adapter les e-mails d'alerte au format HTML afin de recevoir des e-mails avec du contenu mis en forme (avec des bannières, des couleurs, des images et des hyperliens), plutôt que sous forme de texte brut. Notez que le passage d'e-mails par défaut sous forme de texte brut à des e-mails au format HTML peut causer certains problèmes avec les systèmes automatisés qui effectuent la mise en forme. Par défaut, le format HTML est uniquement disponible pour les nouveaux comptes. Si vous voulez activer ou désactiver ce paramètre, consultez les instructions ci-dessous.

Pour activer la mise en forme HTML :

1. Ouvrez l'onglet {{< AppElement type="tab" >}} Personnalisations {{< /AppElement >}} et cochez la case **Utiliser un e-mail HTML**.
2. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} pour confirmer les changements.

Pour désactiver le format HTML :

1. Ouvrez l'onglet {{< AppElement type="tab" >}} Personnalisations {{< /AppElement >}} et décochez la case **Utiliser un e-mail HTML**.
2. Cliquez sur {{< AppElement type="savebutton" >}} Enregistrer {{< /AppElement >}} pour confirmer les changements.
