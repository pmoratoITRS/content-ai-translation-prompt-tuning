{
  "title": "Nieuwe MSA-functie: Foutafhandeling",
  "date": "2024-12-18",
  "url": "[URL_BASE_CHANGELOG]december-2024-msa-foutafhandeling-functie",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

We hebben een nieuwe sectie [INLINE_CODE_1] toegevoegd in de gebruikersinterface van de MSA Visuele stap-editor. Deze functie geeft u meer flexibiliteit bij het afhandelen van MSA-stapfouten, wat zorgt voor betere controle en aanpasbaarheid aan dynamisch webservergedrag.

![Selectievakje MSA Foutafhandeling]([LINK_URL_1])

Als u het selectievakje **Doorgaan na een fout** selecteert, kunt u fouten negeren die zijn opgetreden in een MSA-controleregelstap. Dit betekent dat als een bepaalde stap fouten tegenkomt (zoals een ongeldige request, request time-out of een falende assertion), de controleregel de resterende stappen blijft controleren. Dergelijke fouten zijn alleen zichtbaar in de **Stapresultaten** en worden weergegeven als [INLINE_CODE_2]. Deze worden niet weergegeven in een van uw **Foutenoverzicht**-dashboards of -rapporten.  

Dit gedrag voor foutafhandeling is vergelijkbaar met dat van de Transactiecontroleregels. Raadpleeg voor meer informatie het knowledgebase-artikel [Negeer fouten gebruiken bij optionele stappen en acties]([LINK_URL_2]).

