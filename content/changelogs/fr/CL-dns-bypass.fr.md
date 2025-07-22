{
"title": "Clarification des informations sur le contournement DNS dans les détails des vérifications",
"date": "2024-03-20",
"url": "/changelog/mars-2024-contournement-dns",
"translationKey": "https://www.uptrends.com/changelog/march-2024-dns-bypass"
}

Lors de la dernière mise à jour, nous avons apporté des modifications pour afficher clairement l'URL de contournement DNS et l'adresse IP résolue dans les [détails des vérifications]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/check-details" lang="fr" >}}) lorsqu'un contournement DNS est configuré. Auparavant, Uptrends montrait uniquement l'adresse IP résolue de façon séparée, ce qui pouvait manquer de clarté. Désormais, ces adresses sont plus faciles à distinguer. Vous pouvez ainsi mieux comprendre les situations et résoudre plus facilement les problèmes.

Lorsque vous créez ou que vous modifiez un moniteur Full Page Check ou un moniteur de transaction, vous pouvez ajouter un [contournement DNS]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="fr" >}}). Le contournement DNS permet de s'assurer que la résolution de la page web se fait dans une adresse IP spécifique, au lieu de celle utilisée par défaut. Cette option se situe dans la section _Connexion_ située dans l'onglet {{< AppElement type="tab" >}} Avancé {{< /AppElement >}} du moniteur.