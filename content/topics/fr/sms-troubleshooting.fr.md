{
"hero": {
"title": "Dépannage des SMS d'alerte"
},
"title": "Dépannage des SMS d'alerte",
"summary": "Les SMS d'alerte sont l'un des meilleurs moyens de rester au courant de l'état de votre site web, de vos serveurs et des services web.",
"url": "/support/kb/alerter/depannage-sms",
"translationKey": "https://www.uptrends.com/support/kb/alerting/sms-troubleshooting"
}

**Les alertes SMS** sont l'un des meilleurs moyens de rester au courant de l'état de votre site web, de vos serveurs et de vos services web. Si vos alertes SMS ne vous parviennent pas, ce problème doit être corrigé.

Vous trouverez ci-dessous une série d'options de dépannage des SMS d'alerte :

## Utiliser d'autres expéditeurs

Si vous ne parvenez pas à tester les messages SMS, vous pouvez essayer d’effectuer la manipulation suivante dans l’application web d’Uptrends. Pour cela, suivez les étapes suivantes :

1. Dans la partie inférieure gauche de l’écran, cliquez sur {{< AppElement type="menuitem" >}} Votre nom > Paramètres utilisateur {{< /AppElement >}}.
2. Dans l’onglet {{< AppElement type="tab" >}} Principal {{< /AppElement >}}, faites défiler vers le bas jusqu’à {{< AppElement type="menuitem" >}} Paramètres téléphone > Opérateur SMS {{< /AppElement >}}.
3. Choisissez l’option **Remplacer les paramètres d'intégration de SMS** pour pouvoir modifier les champs au-dessous.
4. Sélectionnez un fournisseur de passerelle dans le menu déroulant. Actuellement, vous avez le choix entre quatre fournisseurs différents :

- Passerelle SMS basée en Europe
- Passerelle SMS basée en Europe 2
- Passerelle SMS basée aux USA
- Passerelle SMS internationale

5. Cochez la case **Utiliser un expéditeur numérique**.

Certains fournisseurs rencontrent des difficultés pour recevoir les messages de la part des expéditeurs numériques, et d'autres de la part des expéditeurs alphabétiques. Par défaut, nous utilisons un expéditeur alphabétique.

## Déblocage via votre fournisseur

### SPRINT

Par défaut, certains numéros de téléphone des utilisateurs de l'opérateur SPRINT peuvent être bloqués. Nous avons la solution. Pour débloquer votre numéro, envoyez un message texte contenant **UPTRENDS** à **46786**.

En cas de *réussite*, vous devriez commencer à recevoir des messages SMS conformément à la configuration de votre compte.

En cas d'*échec*, vous devrez contacter directement votre opérateur pour débloquer votre compte.

### AT&T

Certains utilisateurs de l'opérateur AT&T peuvent rencontrer des difficultés pour recevoir des messages SMS par défaut, mais peuvent débloquer leur numéro en envoyant un message texte contenant **UPTRENDS** au **64085**.

En cas d'*échec*, vous devrez contacter directement votre opérateur pour débloquer votre compte.

## Problèmes de SMS pour les opérateurs

### Chine et Inde

En raison des filtres antispam en Chine et des listes de numéros de téléphone exclus en Inde, les alertes SMS peuvent ne pas fonctionner pour les opérateurs situés dans ces pays. [Cliquez ici pour en savoir plus]({{< ref path="/support/kb/alerting/china-india-sms-voice-alert-issues" lang="fr">}}).

## Liste des pays pris en charge et des fournisseurs ayant un identifiant d’expédition

Vous trouverez ci-dessous la liste des pays pris en charge par Uptrends, ainsi que les fournisseurs de passerelle. La colonne *Expéditeur numérique* indique si la case *Utiliser un expéditeur numérique* peut être activée ou désactivée dans l’application Web d’Uptrends.

Si la colonne indique *Oui*, vous pouvez cocher la case *Utiliser un expéditeur numérique* pour recevoir le SMS depuis un numéro de téléphone mobile. Autrement, le SMS sera envoyé au nom d’**UPTRENDS**. Si la colonne indique *Oui* et *Non*, choisissez l’option qui vous convient le mieux.

| Indicatif téléphonique | Pays | Passerelle | Expéditeur numérique |
|--|--|--|--|
| +1 | États-Unis | Passerelle basée aux États-Unis ou internationale | Oui et Non |
| +33 | France | Passerelle basée en Europe 2 | Oui et Non |
| +40 | Roumanie | Passerelle basée en Europe 2 | Oui |
| +44	| Royaume-Uni | Passerelle basée en Europe 2 | Non |
| +45	| Danemark | Passerelle basée en Europe 2 | Non |
| +46 | Suède | Passerelle basée en Europe 2 | Non |
| +47 | Norvège | Passerelle basée en Europe 2 | Non |
| +65 |	Singapour | Passerelle basée en Europe 2 | Non |
| +90 |	Turquie | Passerelle basée en Europe 2 | Non |
| +91	| Inde	| Passerelle basée en Europe 2 | Non |
| +358 | Finlande	| Passerelle basée en Europe 2	| Non |
| +381 |Serbie | Passerelle basée en Europe 2	| Non |
| +421 | Slovaquie | Passerelle basée en Europe 2	| Non |
| +998 | Ouzbékistan | Passerelle basée en Europe 2	| Non |

#### Vous rencontrez des difficultés ?

Si vous avez essayé ces options de dépannage mais que vous ne recevez toujours pas les alertes, veuillez contacter le support en créant [un ticket](/contact).
