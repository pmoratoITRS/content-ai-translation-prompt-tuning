{
  "title": "Nieuwe MSA-functie: Foutafhandeling",
  "date": "2024-12-18",
  "url": "/changelog/december-2024-msa-foutafhandeling-functie",
  "translationKey": "https://www.uptrends.com/changelog/december-2024-msa-error-handling-feature"
}

We hebben een nieuwe sectie `Foutafhandeling` toegevoegd in de gebruikersinterface van de MSA Visuele stap-editor. Deze functie geeft u meer flexibiliteit bij het afhandelen van MSA-stapfouten, wat zorgt voor betere controle en aanpasbaarheid aan dynamisch webservergedrag.

![Selectievakje MSA Foutafhandeling](/img/content/scr-error-handling-checkbox.min.png)

Als u het selectievakje **Doorgaan na een fout** selecteert, kunt u fouten negeren die zijn opgetreden in een MSA-controleregelstap. Dit betekent dat als een bepaalde stap fouten tegenkomt (zoals een ongeldige request, request time-out of een falende assertion), de controleregel de resterende stappen blijft controleren. Dergelijke fouten zijn alleen zichtbaar in de **Stapresultaten** en worden weergegeven als `Er is een fout opgetreden tijdens deze stap`. Deze worden niet weergegeven in een van uw **Foutenoverzicht**-dashboards of -rapporten.  

Dit gedrag voor foutafhandeling is vergelijkbaar met dat van de Transactiecontroleregels. Raadpleeg voor meer informatie het knowledgebase-artikel [Negeer fouten gebruiken bij optionele stappen en acties]({{< ref path="/support/kb/synthetic-monitoring/transactions/using-ignore-errors-for-optional-steps-and-actions#how-is-ignore-errors-like-making-a-conditional-statement" lang="nl" >}}).

