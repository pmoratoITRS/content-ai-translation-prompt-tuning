{
  "hero": {
    "title": "Die Überwachungs-Frequenz"
  },
  "title": "Die Überwachungs-Frequenz",
  "summary": "Die Überwachungs-Frequenz oder Prüffrequenz ist der Zeitraum zwischen dem Ende der letzten Überprüfung bis zum Beginn der nächsten.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/pruefobjekt-einstellungen/die-ueberwachungs-frequenz",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Die dritte Angabe bei deinen Prüfobjekteinstellungen bittet Dich um die Angabe der Häufigkeit Deiner Monitoring-Checks (siehe Abbildung unten). Du kannst die Überwachungen so häufig wie einmal pro Minute bis hin zu einmal pro Stunde einrichten. Was also heißt Überwachungs-Frequenz genau? **Die Überwachungs-Frequenz ist der Zeitraum zwischen dem Ende der letzten Überprüfung bis zum Beginn der nächsten.** Sehen wir uns dies etwas genauer an.

![]([LINK_URL_1])

Du denkst vielleicht, dass eine Minute als Überwachungs-Frequenz bedeutet, dass Uptrends Deine Website 1440 Mal am Tag mit Checks prüft, die zu Beginn jeder Minute starten. Dem ist aber nicht so. Uptrends muss erst sicher sein, dass der vorherige Check erfolgreich abgeschlossen ist, bevor der nächste Check geplant wird. Daher hängt die Anzahl der Checks, die täglich durchgeführt werden, ab von:

-   Prüfobjekttyp
-   Seitenladezeit oder Antwortzeit
-   ausgewählte Frequenz
-   Anzahl der von Uptrends erfassten Fehler bei Deiner Website oder deinem Service
-   System-Overhead zum Senden der Prüfdefinition zum Checkpoint, Verarbeitung, Übermittlung und Verarbeitung der Ergebnisse.

Sehen wir uns einige Beispiele an:

**Verfügbarkeits-Check, Frequenz eine Minute**

Wenn ein Verfügbarkeits-Check zehn Sekunden von Anfang bis Ende dauert, beginnt der nächste Check 60 Sekunden nach dem erfolgreichen Abschluss des ersten Checks. In diesem Fall also kannst Du mit etwa 70-Sekunden-Intervallen vom Beginn eines Checks zum Beginn des nächsten rechnen. Statt 1.440 Checks pro Tag erhältst Du etwa 1.234 Checks pro Tag.

**Transaktionsprüfobjekt, Frequenz fünf Minuten**

Komplexe Transaktionen können einige Zeit benötigen, bis sie abgeschlossen sind. Dies hängt von der Anzahl der Schritte und die Reaktionszeit Deiner Website oder Deines Service ab. Wenn ein Check zwei Minuten von Anfang bis Ende benötigt, beginnt der nächste Check fünf Minuten, nachdem der erste Check beendet wurde, oder sieben Minuten nach Beginn des ersten Checks. Statt 288 Checks pro Tag ergibt dieses Szenario etwa 206 Checks pro Tag.

## Wie wirken sich Fehler auf die Frequenz des Prüfobjekts aus?

Wenn Uptrends einen Fehler bei Deiner Website oder deinem Service feststellt, ignoriert Uptrends die Überwachungs-Frequenz und setzt direkt den nächsten Check von einem anderen Checkpoint aus an. Stellt Uptrends dabei wieder den Fehler fest, sendet es einen Warnmeldung. Uptrends plant den nächsten Check dann nach deinen Einstellungen der Frequenz. Ist die Testzwischenzeit abgelaufen, prüft Uptrends noch einmal, bzw. zweimal, wenn es wieder einen Fehler feststellt. Obwohl das Prüfobjekt eine Überwachungs-Frequenz von fünf Minuten eingestellt hat, siehst Du im Prüfobjektprotokoll, dass der bestätigte Fehler (rot) direkt nach dem nicht bestätigten Fehler (gelb) gemeldet wurde. Das Zeitintervall zwischen dem bestätigten Fehler und dem nächsten Check beträgt fünf Minuten.

![]([LINK_URL_2])
