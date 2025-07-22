{
"hero": {
"title": "Fuseau horaire"
},
"title": "Fuseau horaire",
"summary": "Le paramètre de fuseau horaire indique selon quel fuseau horaire les périodes de surveillance doivent être affichées.",
"url": "/support/kb/compte/parametres/fuseaux-horaires",
"translationKey": "https://www.uptrends.com/support/kb/account/timezones"
}

Le paramètre **Fuseau horaire** détermine selon quel fuseau horaire les périodes de surveillance doivent être affichées.

Ce paramètre est défini lors de la configuration du compte Uptrends. Pour y accéder, ouvrez le menu {{< AppElement type="menuitem" >}} Configuration de compte > Paramètres de compte {{< /AppElement >}}, puis l'onglet {{< AppElement type="tab" >}} Paramètres {{< /AppElement >}}.

Vous pouvez modifier le fuseau horaire vous-même, sauf si des données ont déjà été collectées dans votre compte Uptrends au moyen du Real User Monitoring. Dans ce cas, le paramètre ne peut pas être modifié et vous devrez contacter le [support]({{< ref path="contact" lang="fr" >}}) pour examiner les options possibles.

{{< callout >}}
**Remarque :** La modification de ce paramètre introduit une absence ou un chevauchement dans les données existantes, car l'application ne recalcule pas ces données après le changement.
{{< /callout >}}

## Heure d'été

Dans l'application Uptrends, certains fuseaux horaires sont marqués d'un astérisque (\*), ou du signe dièse (\#), pour indiquer que le fuseau horaire applique l'heure d'été.

- \* - Ce fuseau horaire concerne l'hémisphère nord et applique l'heure d'été.
- \# - Ce fuseau horaire concerne l'hémisphère sud et applique l'heure d'été.
- Les fuseaux horaires qui n'appliquent pas l'heure d'été ne sont pas marqués des signes \* ou \#.

Si vous voulez afficher les heures en temps universel coordonné ou UTC, utilisez le fuseau horaire **UTC** (sans le signe \*). Ce paramètre de fuseau horaire ne tient pas compte de l'heure d'été. Il est à distinguer du fuseau horaire **UTC\* Angleterre, Irlande** qui tient compte de l'heure d'été.

## Fuseaux horaires pour les opérateurs

Le paramètre de fuseau horaire défini par défaut pour le compte Uptrends peut être ajusté en indiquant un [fuseau horaire supplémentaire]({{< ref path="support/kb/account/users/operators/main-settings#timezone" lang="fr" >}}) pour les opérateurs individuels. Cette fonctionnalité est toutefois réservée aux [comptes Enterprise]({{< ref path="/pricing#plans" lang="fr" >}}).
