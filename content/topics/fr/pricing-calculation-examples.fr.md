{
"hero": {
"title": "Tarification pour la surveillance simultanée"
},
"title": "Tarification pour la surveillance simultanée",
"summary": "Dans cet article, vous trouverez les formules de calcul ainsi que des exemples pour connaître le prix que coûtera la surveillance simultanée.",
"url": "/support/kb/surveillance-synthetique/surveillance-simultanee/tarifs-calcul-exemples",
"translationKey": "https://www.uptrends.com/support/kb/concurrent-monitoring/pricing-calculation-examples"
}


## Tarification pour le Full Page Check (FPC) et les moniteurs de transactions

Le calcul du prix est basé sur un système de crédits, où les différents types de moniteurs ont des coûts de base différents, exprimés en crédits. Donc en général, le calcul est le suivant :

Prix = le prix de base du moniteur x le nombre de points de contrôle utilisé dans la vérification.

### Exemple avec comparaison

Dans le tableau suivant vous trouverez un exemple des tarifs, en comparant la surveillance simultanée et la surveillance standard.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Surveillance simultanée</th><th>Surveillance standard</th></tr></thead><tbody><tr class="odd"><td>Transaction (coût de 4 crédits), définie par l'utilisateur pour s'exécuter sur 3 points de contrôle<br />

4 crédits x 3 = <strong>12 crédits</strong></td><td>Transaction (coût de 4 crédits)<br />

4 crédits x 1 = <strong>4 crédits</strong></td></tr></tbody></table>

## Tarification pour les moniteurs de base et les moniteurs API multi-étapes (MSA)

Pour ces moniteurs, la tarification se fait par paliers avec un coût dégressif, le prix est donc calculé différemment des autres Full Page Check (FPC) et moniteurs de transactions. Les moniteurs de base comprennent les moniteurs Ping, Http(s), certificat SSL, etc. Gardez également à l'esprit que pour un moniteur MSA, le prix dépend du nombre d'étapes. Les formules de prix sont données ci-dessous.

**Moniteur de base**

Prix = le prix de base du moniteur x le coût dégressif du tableau du coût par palier ci-dessous.

**Moniteur MSA**

Prix = le nombre d'étapes du moniteur MSA x le coût dégressif du tableau du coût par palier ci-dessous.

### Tableau du coût par palier {id="tiered-pricing-table"}

<table>
<colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup>
<thead><tr class="header"><th>Nombre de points de contrôle</th><th>Coût dégressif</th></tr></thead>

<tbody>

<tr><td>1 à 2</td><td>N/A (voir note sous le tableau)</td></tr>
<tr><td>3 à 4</td><td>2</td></tr>
<tr><td>5 à 7</td><td>3</td></tr>
<tr><td>8 à 10</td><td>4</td></tr>
<tr><td>11 à 14</td><td>5</td></tr>
<tr><td>15 à 18</td><td>6</td></tr>
<tr><td>19 à 22</td><td>7</td></tr>
<tr><td>23 à 26</td><td>8</td></tr>
<tr><td>27 à 30</td><td>9</td></tr>
<tr><td>31 à 35</td><td>10</td></tr>
<tr><td>36 à 40</td><td>11</td></tr>
<tr><td>41 à 45</td><td>12</td></tr>
<tr><td>46 à 50</td><td>13</td></tr>
</tbody>

</table>

{{< callout >}} **Remarque** : Pour utiliser la surveillance simultanée vous devez choisir un nombre minimum de points de contrôle, trois pour la haute disponibilité ou cinq en tout. Pour une surveillance standard, vous devez également choisir un minimum de trois points de contrôle, mais un seul sera utilisé à la fois (et inclus dans le calcul du prix). {{< /callout >}}
### Exemples

Dans le tableau suivant vous trouverez un exemple des tarifs, en comparant la surveillance simultanée et la surveillance standard, ainsi que pour différents niveaux dans la tarification à paliers

**Moniteur de base**

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup>

<thead><tr class="header"><th>Surveillance simultanée (tarification à paliers)</th><th>Surveillance standard</th></tr></thead>

<tbody>

<tr><td>Moniteur HTTPS (prix de base de 1), défini par l'utilisateur pour s'exécuter sur 4 points de contrôle<br />1 crédit x 2 (coût dégressif) = <strong>2 crédits</strong></td>
<td>Moniteur HTTPS (prix de base de 1)<br />1 crédit x 1 = <strong>1 crédit</strong></td></tr>
<tr><td>Moniteur HTTPS (prix de base de 1), défini par l'utilisateur pour fonctionner sur 10 points de contrôle<br />1 crédit x 4 (coût dégressif) = <strong>4 crédits</strong></td><td>Moniteur HTTPS (prix de base de 1)<br />1 crédit x 1 = <strong>1 crédit</strong></td></tr>
</tbody>

</table>

**Moniteur API multi-étapes**

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup>

  <thead><tr class="header"><th>Surveillance simultanée (tarification à paliers)</th><th>Surveillance standard</th></tr></thead>

  <tbody>

<tr><td>Moniteur MSA avec 10 étapes, défini par l'utilisateur pour s'exécuter sur 4 points de contrôle<br />

10 crédits (nombre d'étapes) x 2 (coût dégressif) = <strong>20 crédits</strong></td>

<td>Moniteur MSA avec 10 étapes (prix de base de 10)<br />

10 crédits (nombre d'étapes) x 1 = <strong>10 crédits</strong></td></tr>

   <tr><td>Moniteur MSA avec 10 étapes, défini par l'utilisateur pour fonctionner sur 10 points de contrôle<br />

10 crédits (nombre d'étapes) x 4 (coût dégressif) = <strong>40 crédits</strong></td>

<td>Moniteur MSA avec 10 étapes (prix de base de 10)<br />

10 crédits (nombre d'étapes) x 1 = <strong>10 crédits</strong></td></tr> 

  </tbody>

</table>

{{< callout >}} **Remarque** : En général, vous devez garder à l'esprit qu'un type de moniteur avec un prix de base élevé (crédits par moniteur) entraînera une utilisation élevée de crédits lorsque vous utilisez de nombreux points de contrôle. {{< /callout >}}
