{
  "hero": {
    "title": "Funktionsweise eines HTTP-Prüfobjekts"
  },
  "title": "Funktionsweise eines HTTP-Prüfobjekts",
  "summary": "Erfahren Sie, wie Uptrends einen HTTP(S)-Test ausführt und was das System macht, wenn es einen Fehler entdeckt.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/verfuegbarkeits-monitoring/http-und-https/funktionsweise-eines-http-pruefobjekts",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Haben Sie sich jemals gefragt, was passiert, wenn Uptrends ein HTTP- oder HTTPS-Monitoring bei Ihrer Website ausführt? Es kann zu vielen unterschiedlichen Szenarien je nach den jeweiligen Umständen kommen. Sehen wir uns einige an.

1.  Uptrends verwendet einen der von Ihnen ausgewählten Checkpoints nach dem Zufallsprinzip.
2.  Uptrends versucht, den angegebenen Domainnamen aufzulösen.  
    [SHORTCODE_1]**Hinweis:** Sie können die IP-Adresse statt des Domainnamens verwenden, um den Auflösungsprozess des Tests zu überspringen, aber Sie erhalten keine Warnmeldungen, falls es ein Auflösungsproblem gibt.[SHORTCODE_2] 
3.  Mithilfe der IP-Adresse versucht Uptrends dann eine Low-Level-TCP-Verbindung über Port 80 für HTTP, über Port 443 für HTTPS oder über den von Ihnen angegebenen Port aufzubauen.
4.  Nach dem grundlegenden Test, wie in Schritte 3 beschrieben, öffnen wir eine TCP Connection, senden einen HTTP/S Request und warten auf Response.

## Was passiert, wenn Uptrends auf ein Problem stößt?

Fehler können während jedes Schritts im Testverlauf auftreten. Abhängig vom Fehlertyp unternimmt Uptrends sofort verschiedene Schritte, bevor eine Warnmeldung gesendet wird. Bei den meisten Fehlern wird Uptrends versuchen, über einen anderen Checkpoint eine fehlerfreie Verbindung zu erstellen. Wenn Uptrends von einem anderen Checkpoint den Fehler dupliziert, senden wir eine Warnmeldung. Bei bestimmten Fehlern gibt es jedoch Ausnahmen.

### HTTPS-Fehler

Wenn der HTTPS-Prüfobjekttyp und die Anfrage einen Fehler zurückgeben (Schritt 3), testet Uptrends eventuell mehrere Male mithilfe unterschiedlicher Sicherheitsprotokolle, bevor ein Test als fehlgeschlagen gilt.

### HTTP(S) mit angegeben Authentifizierungsdaten

Bei HTTP- und HTTPS-Anfragen, die Nutzerauthentifizierungen enthalten, führt Uptrends einen Test erneut aus, bevor ein Versuch als fehlerhaft eingestuft wird.

### Netzwerkfehler

Wenn die HTTP- oder HTTPS-Anfrage aufgrund eines Netzwerkproblems einen Fehler ausgibt, versucht Uptrends, eine Routenverfolgung (Traceroute) zur IP-Adresse durchzuführen. Bei der Routenverfolgung werden eine Reihe von Ping (=ICMP)-Paketen gesendet.
