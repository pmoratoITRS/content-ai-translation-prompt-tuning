{
  "hero": {
    "title": "Surveillance de sites Web autres que le serveur de production"
  },
  "title": "Surveillance de sites Web autres que le serveur de production",
  "summary": "Avez-vous besoin de surveiller un site Web autre que le serveur de production, mais les deux partagent le même nom de domaine ? Vous pouvez le faire avec une configuration appropriée en utilisant les en-têtes d'hôte (host headers).",
  "url": "/support/kb/surveillance-synthetique/uptime-monitoring/http-et-https/surveillance-de-sites-web-autres-que-le-serveur-de-production",
  "translationKey": "https://www.uptrends.com/support/kb/http-and-https/monitoring-websites-other-than-the-production-server"
}

Si vous avez besoin de surveiller un site Web sur un domaine qui n'est pas votre serveur de production, tel qu'un site de sauvegarde ou de test, vous pouvez le faire avec une configuration du moniteur appropriée qui utilise les en-têtes d'hôte.

## Avec quels types de moniteurs cela fonctionne ?

Vous pouvez configurer ce type de surveillance à l'aide de moniteurs HTTP, HTTPS et de service Web. Malheureusement, cela ne fonctionne pas avec le Full Page Check ou Transaction Monitoring.

## Ce dont vous avez besoin

Pour configurer des moniteurs avec des en-têtes d'hôte, il vous faut :

-   L'URL du serveur Web à surveiller, et
-   L'adresse IP du serveur auquel il faut accéder en directe.

## Configuration du moniteur

Pour configurer un moniteur :

1.  Ouvrir un moniteur existant ou nouveau
2.  Sur l'onglet {{< AppElement type="tab" >}}Principal{{< /AppElement >}} , entrez l'adresse IP dans le champ  **URL**.  
    ![](/img/content/f2fe984f-d945-40d0-9d11-8c0f12e91625.png)
3.  Passer à l'onglet {{< AppElement type="tab" >}}Avancé{{< /AppElement >}}.
4.  Tapez "Host:" suivi du nom de domaine (voir ci-dessous)  
    ![](/img/content/d95e932f-0023-47c1-ba0d-bf10feada5c7.png)
5.  Ajoutez un **Page content check** (onglet {{< AppElement type="tab" >}}Conditions d'erreur{{< /AppElement >}}) qui contient un contenu unique sur le site à surveiller et qui n'est pas sur le site en direct pour vous assurer que vous accédez au bon site (facultatif).
6.  Cliquez sur {{< AppElement type="savebutton" >}}Enregistrer{{< /AppElement >}} pour terminer votre configuration SSO.
