{
  "hero": {
    "title": "Mailservers"
  },
  "title": "Mailserver",
  "summary": "Met Uptrends' SMTP en POP3 monitors bent u als eerste op de hoogte van eventuele problemen met uw e-mail servers.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/uptime-monitoring/mailservers",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

Post is belangrijk voor u en voor uw onderneming, en dat geldt ook voor de gezondheid en beschikbaarheid van uw e-mailservers. Ook als uw e-mailserver maar heel even down is, kan dit kosten met zich mee brengen in productiviteit, reputatie en omzet. Met Uptrends kunt u SMTP-, POP3- en IMAP-mailservers monitoren om er zeker van te zijn dat uw team onmiddellijk op de hoogte is als er problemen zijn met uw mailservers.

## Beschikbaarheid monitoren

Naast servercrashes kunnen DNS- of andere configuratieproblemen er de oorzaak van zijn dat uw mailservers niet naar behoren functioneren. Met controleregels voor mailservers zult u het onmiddellijk weten wanneer er een probleem optreedt.

## Performance monitoren

De performance kan door veel factoren worden beïnvloed, waaronder netwerkverkeer en falende hardware. Door alerts voor responstijden te configureren weet u precies wanneer uw mailservers in de problemen dreigen te komen.

## Een controleregel voor een mailserver instellen

Het instellen van uw controleregel voor een mailserver is bijna hetzelfde als bij andere types controleregels. Een overzicht van het instellen van een nieuwe controleregel is te vinden in het artikel [Controleregels toevoegen]([LINK_URL_1]). Om een mailserver-controleregel in te stellen:

1.  Selecteer [SHORTCODE_1]\+Controleregel toevoegen[SHORTCODE_2] in het menu **Monitoring** op het [SHORTCODE_3]Hoofdmenu[SHORTCODE_4].
2.  Selecteer SMTP, IMAP of POP3 in het menu **Type**.
3.  Geef uw controleregel een **Naam**.
4.  Stel het **controle-interval** in.
5.  Selecteer de selectievakjes **Actief** en **Alerts genereren** als deze nog niet zijn geselecteerd.
6.  Specificeer het IP-adres of de domeinnaam van uw mailserver in het vak **Netwerkadres**.
7.  Controleer of het **Poort**-nummer correct is.
8.  Klik op [SHORTCODE_5]Opslaan[SHORTCODE_6].

Met deze basisconfiguratie zal Uptrends u alerts sturen als uw server ooit niet beschikbaar is. U kunt ook het tabblad [SHORTCODE_7]Foutcondities[SHORTCODE_8] gebruiken om alerts voor responstijden te configureren. Op het tabblad [SHORTCODE_9]Extra[SHORTCODE_10] kunt u authenticatie-informatie verstrekken als u wilt dat Uptrends probeert in te loggen op de server (lees hoe [Uptrends uw authenticatie-informatie beschermt]([LINK_URL_2])).
