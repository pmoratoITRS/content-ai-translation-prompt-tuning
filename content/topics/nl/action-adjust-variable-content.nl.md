{
  "hero": {
    "title": "Een transactievariabele aanpassen"
  },
  "title": "Een transactievariabele aanpassen",
  "summary": "Bij het instellen van transactiecontroleregels wilt u mogelijk waarden extraheren en aanpassen. Met de bedieningactie *Een variabele aanpassen* kunt u eerder geëxtraheerde inhoud wijzigen. ",
  "url": "/support/kb/synthetic-monitoring/transacties/actie-inhoud-variabele-aanpassen",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/action-adjust-variable-content"
}

Met de transactie-actie van het type **Inhoud variabele aanpassen** kunt u de waarde wijzigen van een variabele die is ingesteld in een actie [**Test de inhoud van een element**]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks#test-element-content" lang="nl" >}}) binnen de stap van een transactiecontroleregel. De aanpassing wordt uitgevoerd met behulp van reguliere expressies (RegEx). Het wijzigen van een variabelewaarde kan handig zijn als u slechts een deel of een aangepast deel van de waarde die is afgeleid van een pagina-element wilt gebruiken. 

{{< callout >}} **Opmerking**: De aanpassing van een variabele vervangt de oorspronkelijke waarde van de variabele. Een (aangepaste) variabele is beschikbaar vanaf de actie waar deze is gedefinieerd/aangepast, in alle volgende acties en stappen tot het einde van de transactie. {{< /callout >}}

## De variabele definiëren {id="defining-the-variable"}

Meer informatie over het instellen van een transactievariabele vindt u in ons Knowledge Base-artikel [Transactievariabelen gebruiken]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-variables" lang="nl" >}}).

## De variabele aanpassen {id="adjust-variable"}

Het tweede deel bestaat uit het toevoegen van een *Inhoud van de variabele aanpassen*-actie aan de stap:

1. Open de transactiecontroleregel die u wilt wijzigen.
2. Ga naar het tabblad {{< AppElement type="tab" >}} Stappen {{< /AppElement >}}.
3. Open de stap waarin u een variabele wilt wijzigen.
4. Klik op de knop {{< AppElement type="buttonPrimary" >}} Actie toevoegen {{< /AppElement >}}. 
5. Kies uit de lijst met **Bediening**-acties de actie *Inhoud variabele aanpassen* en klik op de knop {{< AppElement type="button" >}} Selecteren {{< /AppElement >}} om de actie aan de stap toe te voegen.

   ![screenshot transactie-actie een variabele aanpassen](/img/content/scr_transaction-action-transform-variable.min.png)

   De waarden voor *Variabele*, *Type aanpassing* en *Regular expression patroon* zijn verplicht. De andere instellingen zijn optioneel.

6. Vul de naam van de variabele in in het formaat `{{name}}`. De naam moet precies hetzelfde worden gespeld als bij het [Definiëren van de variabele](#defining-the-variable). De naam is hoofdlettergevoelig.
7. Kies het *Type aanpassing*, dit kan zijn  
   \- **Behoud alles dat overeenkomt met een patroon** – om een waarde te extraheren uit de variabele die overeenkomt met de waarde van het *Regular expression patroon*  
   \- **Verwijder alles dat overeenkomt met een patroon** – om alles te extraheren behalve het deel dat overeenkomt met de waarde van het *Regular expression patroon*
8. Voer de reguliere expressie (RegEx) in die moet worden gebruikt om de variabele aan te passen.
   Als de waarde van de variabele bijvoorbeeld oorspronkelijk "Uw ordernummer is 12345" is en gezien het feit dat uw ordernummer altijd uit vijf cijfers bestaat, kunt u de variabele in het ordernummer alleen wijzigen met de instelling *Behoud alles dat overeenkomt met een patroon* in combinatie met de reguliere uitdrukking `\d{5}` als het *Regular expression patroon* dat vijf cijfers achter elkaar zal vinden. 
9. Zorg ervoor dat de aanpassing van de variabele gebeurt na het instellen van de variabele. U kunt de acties binnen een stap slepen en neerzetten, mocht dit nodig zijn. 
10. Klik op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om alle wijzigingen op te slaan.

 De aangepaste variabelewaarde is nu beschikbaar in alle opeenvolgende acties en stappen tot het einde van de transactie. Om naar de variabele te verwijzen gebruikt u de oorspronkelijke naam ({{name}}) die u heeft opgegeven bij het definiëren van de variabele. Bekijk de informatie over de [actie Instellen]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#set" lang="nl" >}}) om te leren hoe u de variabele gebruikt voor het instellen van een waarde in een andere stap of actie.
