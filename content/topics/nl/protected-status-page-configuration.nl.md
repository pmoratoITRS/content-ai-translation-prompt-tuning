{
  "hero": {
    "title": "Beveiligde statuspagina’s instellen"
  },
  "title": "Beveiligde statuspagina’s instellen",
  "summary": "In dit artikel wordt beschreven hoe u een nieuwe beveiligde statuspagina maakt en operators instelt.",
  "url": "/support/kb/dashboards-en-rapportages/statuspaginas/beveiligde-statuspagina-instellen",
  "translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/status-pages/protected-status-page-configuration"
}

Om een beveiligde statuspagina te creëren, moet u de pagina instellen en zorgen dat de benodigde gebruikersrechten zijn toegewezen aan de operator(s) die de pagina moet(en) kunnen bekijken. De gebruikersrechten van de nieuwe operator moeten worden beperkt, zodat die alleen toegang heeft tot de beveiligde statuspagina (en niet tot andere dingen, zoals controleregels). Houd er rekening mee dat u administratorrechten nodig heeft om operators en gebruikersrechten te beheren.

## Een beveiligde statuspagina maken

1. Maak een gewone publieke statuspagina aan de hand van de instucties in [Publieke statuspagina's instellen]({{< ref path="support/kb/dashboards-and-reporting/status-pages/public-status-page-configuration" lang="nl" >}}). 
2. Aangezien u een beveiligde statuspagina maakt, moet u ervoor zorgen dat het selectievakje **Publiceren** op het tabblad {{< AppElement type="tab" >}} Algemeen  {{< /AppElement >}} niet is aangevinkt. Publiceert u een statuspagina wel, dan wordt deze beschikbaar voor het grote publiek. 
3. Optioneel kunt u een logo toevoegen, het kleurschema en het onderwerp en onderschrift wijzigen. Dit wordt beschreven in [Uw publieke statuspagina aanpassen]({{< ref path="support/kb/dashboards-and-reporting/status-pages/public-status-page-configuration#customize" lang="nl" >}}).
4. Sla de statuspagina op.
5. In het overzicht Publieke statuspagina's ziet u de *Preview* link voor de nieuwe statuspagina. Deze link bevat de URL die geautoriseerde gebruikers moeten gebruiken om toegang te krijgen tot de statuspagina.

## Operators creëren met toegang tot de beveiligde statuspagina

U moet ten minste één operator maken en de gebruikersrechten zo instellen dat de operator alleen toegang heeft tot de beveiligde statuspagina. Houd er rekening mee dat u een administrator moet zijn om operators toe te voegen en gebruikersrechten te beheren. Daarnaast heeft u wat hulp van Uptrends nodig om het proces te voltooien:

1. Voeg een [nieuwe operator]({{< ref path="support/kb/account/users/operators/operator-groups" lang="nl" >}}) toe. We raden u ten zeerste aan om de nieuwe inloggegevens pas met derden te delen nadat de volgende stappen zijn voltooid. 
2. Verwijder het [gebruikersrecht]({{< ref path="support/kb/account/users/operators/permissions" lang="nl" >}}) *Standaard operator* bij de nieuwe operator door de operatorinstellingen te openen. Op het tabblad {{< AppElement type="tab" >}} Gebruikersrechten {{< /AppElement >}} in het gedeelte **Algemene systeemrechten** klikt u op de knop {{< AppElement type="deletebutton" >}} Uitzetten {{< /AppElement >}} naast het gebruikersrecht *Standaard operator*.
3. Bevestig uw keuze door op {{< AppElement type="deletebutton" >}} Uitzetten te klikken {{< /AppElement >}} in het pop-upvenster.
4. Klik op {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} onder aan het operatorscherm. 
5. Verleen de operator toegang tot de beveiligde statuspagina. Deze stap wordt uitgevoerd door Uptrends Support. [Dien een supportverzoek in]({{< ref path="contact" lang="nl" >}}) waarin u vraagt om een beveiligde statuspagina. Vermeld in uw verzoek de naam van de beveiligde statuspagina en de naam van de operator(s) die toegang moet(en) krijgen. Het Support-team zal de operator(s) toegang verlenen tot de nieuwe statuspagina en u op de hoogte stellen zodra het verzoek is verwerkt.
