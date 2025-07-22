{
  "hero": {
    "title": "Niet-primaire controlestations"
  },
  "title": "Niet-primaire controlestations",
  "summary": "Lees waarom Uptrends sommige controlestations als niet-primair aanduidt, en wat u moet weten voordat u ervoor kiest ze te gebruiken.",
  "url": "/support/kb/synthetic-monitoring/controlestations/niet-primaire-controlestations",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/non-primary-checkpoints"
}

Het is u misschien bij het selecteren van uw controlestations opgevallen dat we sommige controlestations aanduiden als *niet-primair*. Niet-primaire controlestations zijn controlestations die onderhevig zijn aan onregelmatige beschikbaarheid en mogelijk verminderde bandbreedte vanwege de lokale internetinfrastructuur en overheidscontrole.

We hebben ervoor gekozen om de niet-primaire controlestations standaard uit te sluiten wanneer u een regio selecteert waarin deze zijn opgenomen (zie hieronder). Dat betekent echter niet dat we niet willen dat u ze gebruikt. We hebben ze uitgesloten om er zeker van te zijn dat u weet dat deze controlestations onderhevig zijn aan instabiele omstandigheden en dat ze uw uptime- en performancerapportage negatief kunnen beïnvloeden wanneer u ervoor kiest ze te gebruiken. Als u de niet-primaire controlestations wilt gebruiken, schakelt u het selectievakje **Alleen primaire controlestations gebruiken** uit.

![](/img/content/4aa73fc7-1929-4442-a462-25bbbb9ad007.png)

## Ik test alleen in gebieden met niet-primaire controlestations, maar ik zie testen van andere controlestations. Waarom?

Hoewel het belangrijk is om te testen vanaf de locatie van uw gebruiker, wilt u toch de status van uw website of dienst weten als die locatie niet meer beschikbaar is om te testen. In plaats van uw site of dienst niet te testen tijdens periodes van beperkte of ontbrekende verbinding met niet-primaire controlestations, gebruikt Uptrends andere controlestations voor het testen, zodat u uitval en performanceproblemen die zich intussen kunnen voordoen, kunt vastleggen.
