{
  "hero": {
    "title": "SSL-Zertifikats-Prüfobjekte"
  },
  "title": "SSL-Zertifikats-Prüfobjekte",
  "summary": "Uptrends’ fortschrittliches SSL-Monitoring behält deine SSL-Zertifikate im Blick und überwacht Ablaufdaten und Änderungen am Zertifikat, die auf eine Sicherheitsverletzung hinweisen könnten. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/verfuegbarkeits-monitoring/ssl-zertifikat",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

Das SSL (Secure Socket Layers)-Zertifikat ist wichtiger, als den meisten bewusst ist. Forschungen haben ergeben, dass Nutzer den Rat des Browsers annehmen und deine Website verlassen und zur Konkurrenz wechseln, wenn sie eine Warnung wegen eines ungültigen oder abgelaufenen SSL-Zertifikats oder Zertifikatskette erhalten. SSL-Fehlermeldungen kommen laufend vor. Selbst Google ist es passiert, dass das Zertifikat abgelaufen war. Wenn Mitarbeiter oder Verantwortlichkeiten wechseln, verschwinden SSL-Zertifikate häufig aus dem Blickfeld. Mit Uptrends kannst du alle SSL-Daten an einem Ort verwahren und Benachrichtigungen erhalten, wenn dein Zertifikat abläuft oder sich etwas ändert.

## Was wird überwacht?

Neben der Einrichtung der Laufzeit des SSL-Zertifikats kannst du alle anderen Zertifikatswerte überwachen und nachhalten:

- Allgemeiner Name
- Organisation
- Organisationseinheit
- Seriennummer
- Fingerabdruck
- Aussteller allgemeiner Name
- Aussteller Organisation
- Aussteller Organisationseinheit

Wenn einer dieser Werte zum Zertifikat deiner Website sich ändert (ein möglicher Hinweis auf einen Hack), sendet Uptrends eine Warnmeldung.

#### Warn- und Fehlermeldungen

Dies sind die Meldungen, die du empfängst, wenn dein SSL-Zertifikat demnächst abläuft:

- **SSL-Zertifikat erlischt bald** – Dies ist eine allgemeine Fehlermeldung, die auf der Anzahl Tage, die du im Feld [SHORTCODE_1] Verfall Warnung Tage [SHORTCODE_2] auf der Registerkarte [SHORTCODE_3] Allgemein [SHORTCODE_4] deines SSL-Prüfobjekts eingegeben hast, basiert. Wenn das Datum deines Zertifikats dem Werte-Set in diesem Feld entspricht, siehst du diese Nachricht im Dashboard *Fehler Übersicht* oder an Orten, an denen Fehler gruppiert angezeigt werden.

Unter deinem SSL-Prüfobjekt-Dashboard *Prüfobjektprotokoll* und im Dashboard *Alarmierungshistorie* siehst du spezifischere Warnmeldungen, die die verbleibende Anzahl Tage wiedergeben, bis dein Zertifikat erlischt:

- **Das SSL-Zertifikat wird in einem Tag ablaufen**
- **Das SSL-Zertifikat wird in weniger als einem Tag ablaufen**
- **Das SSL-Zertifikat wird in *n* Tagen ablaufen** – Das n stellt die tatsächliche Anzahl Tage, wann das Zertifikat abläuft, in numerischem Format dar. Wenn zum Beispiel nur *45* Tage verbleiben, zeigt die Warnmeldung *SSL-Zertifikat wird in 45 Tagen ablaufen*.

Diese Benachrichtigungen sind auch auf dem Bildschirm *Kontrolldetails* zu sehen, wenn du die Aktion [SHORTCODE_5] Jetzt testen [SHORTCODE_6] bei SSL-Prüfobjekten ausführst.

## Die Einrichtung eines SSL-Zertifikat-Prüfobjekts

Die Einrichtung des Prüfobjekts für SSL-Zertifikate ist ähnlich der Konfiguration des Prüfobjekts für Websites. Hinweise, wie du die ersten Schritte eines neuen Prüfobjekts einrichtest, findest du im Knowledge-Base-Artikel [Prüfobjekte hinzufügen]([LINK_URL_1]).

Die Einrichtung eines SSL-Zertifikat-Prüfobjekts:

1. Rufe [SHORTCODE_7] Überwachung > Prüfobjekteinrichtung [SHORTCODE_8] auf und klicke auf die Schaltfläche [SHORTCODE_9][SHORTCODE_10].
2. Klicke im Pop-up-Fenster *Wähle einen Prüfobjekttyp aus* zunächst auf den Prüfobjekttyp *SSL-Zertifikat* und klicke dann auf die Schaltfläche [SHORTCODE_11] Wähle aus [SHORTCODE_12].
3. Richte die [Haupteinstellungen des Prüfobjekts ]([LINK_URL_2]) ein.
4. Gib im *URL-Feld* die URL oder Browseradresse an, die du überwachen möchtest.
5. Gib die entsprechenden Daten in den SSL-Zertifikats-Bereich ein. Diese Informationen sollten leicht von der Ausgabestelle deines SSL-Zertifikats erhältlich sein.

![SSL Certificate details section]([LINK_URL_3])

6. Klicke auf [SHORTCODE_13] Speichern [SHORTCODE_14], um alle Änderungen anzuwenden.

Uptrends überwacht nun die Daten deines SSL-Zertifikats und warnt dich, wenn die Bedingungen, die du auf den Tabs [SHORTCODE_15]Fehlerbedingungen[SHORTCODE_16] und [SHORTCODE_17]Erweitert[SHORTCODE_18] angegeben hast, erfüllt werden. Der Knowledge-Base-Artikel zu den [Prüfobjekteinstellungen]([LINK_URL_4]) hält weitere Infos bereit.