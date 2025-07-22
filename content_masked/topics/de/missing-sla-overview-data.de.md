{
  "hero": {
    "title": "Fehlende SLA-Übersichtsdaten"
  },
  "title": "Fehlende SLA-Übersichtsdaten",
  "summary": "Die SLA Übersicht zeigt keine Daten an, wenn der Berichtszeitraum Zeiten enthält, die vor der Einrichtung des Prüfobjekts liegen.",
  "url": "[URL_BASE_TOPICS]dashboards-und-berichte/sla/fehlende-sla-ueberblicksdaten",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Du hast dir die Mühe gemacht, ein SLA-Prüfobjekt (Service Level Agreement) einzurichten, oder du verwendest das Standard-SLA-Prüfobjekt, das du bei Kontoeröffnung aktiviert hast. Aber wenn du dir den SLA-Überblick ansiehst, findest du nur Striche (z. B. "-") oder Nullen. Warum? Weil deine Berichtskonfiguration zu ungültigen Daten geführt hat. Statt unvollständige und ungültige Datensets zu zeigen, fügt Uptrends Nullen und Gedankenstriche ein.

## Die möglichen Szenarien

Wir kennen zwei häufig auftretende Szenarien für das Problem fehlender Daten im SLA-Überblick: Du hast Zeiten angegeben, die vor der Einrichtung der SLA-Definition oder Prüfobjekterstellung liegen. Möglicherweise hast du auch in der "Zeige Zeilen für"-Option im Kachelmenü "Prüfobjektgruppen" ausgewählt.

### Du hast Zeiten angegeben, die vor der Einrichtung der SLA-Definition oder des Prüfobjekts liegen

Bei der Wahl eines Berichtszeitraums ist es wichtig zu beachten, ob die SLA-Definition oder das Prüfobjekt nach dem Start- und Enddatum des Berichtszeitraums erstellt wurde. Selbst wenn es sich um einige wenige Sekunden handelt, werden die Ergebnisse für das Prüfobjekt entweder als Gedankenstriche (neuere SLA-Definition) oder als Nullen (neuere Prüfobjekte) erscheinen. Selbst wenn du die SLA-Definition am 1. Januar 2016 eingerichtet hast und es jetzt der 31. Dezember 2016 ist, erhältst du bei Eingabe von "Dieses Jahr" als Berichtszeitraum keine Daten. Du erhältst keine Daten, weil das System für einen Zeitraum direkt am 1. Januar keine Daten hat, sodass im Bericht Striche abgebildet werden. Um einen lückenlosen Bericht zu erhalten, verwende bitte die benutzerdefinierte Dateneingabe und wähle den Tag und Uhrzeit, nachdem du das Konto oder die SLA-Definition eingerichtet hast. In diesem Beispiel also 02.01.2016 bis 31.12.2016.

### Du hast "Prüfobjektgruppe" bei der Option "Zeilen zeigen für" im Kachelmenü ausgewählt

Wenn du das Dreipunkte-Menü [SHORTCODE_1] [SHORTCODE_2] öffnest, um die Kacheleinstellungen aufzurufen, werden dir viele Optionen zur Anzeige von Daten für diese Kachel gegeben. Wenn du **Prüfobjektgruppen** bei der Option **Zeige Zeilen für** auswählst, erhältst du keine SLA-Daten. Die Kachel wird andere Felder wie Gesamtzeit, Checks, Bestätigte Fehler, Verfügbarkeit in Prozent und Ausfallzeiten für die Prüfobjektgruppe zeigen. Du erhältst jedoch keine Werte in den SLA-Feldern, da SLA-Daten nicht über mehrere Prüfobjekte gesammelt werden können. Du kannst Daten für spezifische Prüfobjekte oder Prüfobjektgruppen anzeigen lassen, indem du sie im Schnellmenü oder in den Kacheleinstellungen auswählst. Deine Daten erscheinen aber immer noch in Zeilen für einzelne Prüfobjekte in diesen Gruppen.
