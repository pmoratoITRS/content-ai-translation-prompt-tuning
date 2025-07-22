{
"title": "Introduction des captures d'écran successives pour les transactions",
"date": "2024-04-10",
"url": "/changelog/avril-2024-captures-ecran-successives-transactions",
"translationKey": "https://www.uptrends.com/changelog/april-2024-filmstrips-transactions"
}

La fonctionnalité des [captures d'écran successives]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="fr" >}}), aussi appelées pellicules, est désormais disponible pour les transactions. Cette fonctionnalité est pensée spécifiquement pour les [transactions avec des métriques supplémentaires]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="fr" >}}).

La case à cocher [Filmstrip]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="fr" >}}) remplace la case à cocher Capture d'écran. Les transactions pour lesquelles des captures d'écran ont été paramétrées ne seront pas modifiées, et la ou les captures d'écran resteront également inchangées. La possibilité de créer une capture d'écran pour une étape ou une action reste accessible via l'action de type *Contrôle* - **Capture d'écran**. Les pellicules utilisent un [crédit de transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="fr" >}}), à moins que l'étape contienne déjà une capture d'écran, auquel cas la pellicule n'utilise pas de crédit.