{
  "hero": {
    "title": "Real User Monitoring verstehen"
  },
  "title": "Real User Monitoring verstehen",
  "summary": "In diesem Artikel findest du Infos zu den grundlegenden RUM-Konzepten und darüber, wie RUM funktioniert. ",
  "url": "[URL_BASE_TOPICS]rum/real-user-monitoring-verstehen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In diesem Artikel werden die grundlegenden Konzepte und die Theorie der Einrichtung erläutert.

## Was ist das Real User Monitoring?

Wenn es darum geht, die Performance zu messen, wie sie vom tatsächlichen Website-Besucher erlebt wird, ist das Real User Monitoring (RUM) nicht zu schlagen. RUM zeichnet die Performance der RUM-aktivierten Seiten auf, fasst die Daten zusammen und zeigt Daten in interaktiven Dashboards, wo du die Performance auf Grundlage der aufgerufenen Seiten, des Geräts, Browsers und Version, Betriebssystems und Version und des Standorts vergleichen kannst.

RUM ist ein passiver Ansatz für das Monitoring, weil es sich darauf stützt, dass deine Nutzer die Seite aufrufen, um Daten zu generieren. Wenn deine Website einen Ausfall hat, können Nutzer die Seite nicht aufrufen und dementsprechend werden keine Daten generiert. An dieser Stelle greift das Synthetic oder aktive Monitoring. Deine Prüfobjekte des [Synthetic Monitorings]([LINK_URL_1]) wie Verfügbarkeits-Prüfobjekte, Performance-Prüfobjekte, API-Prüfobjekte und Transaktionsprüfobjekte überwachen deine Website regelmäßig und wenn sie ein Problem feststellen, lassen wir es dich umgehend gemäß deinen [Warnmeldungseinstellungen]([LINK_URL_2]) wissen.

## Wie funktioniert das Real User Monitoring?

Du setzt ein kleines, [nicht invasives Skript]([LINK_URL_3]) innerhalb der [INLINE_CODE_1]-Tags auf den Seiten ein, die du mit RUM überwachen möchtest. Während die Besucher der Website die RUM-aktivierte Seite aufrufen, erfasst das Skript die Performance-Daten. Sobald die Seite komplett geladen ist, bündelt das Skript die Performance-Daten mit den Informationen zur Nutzerumgebung und -standort und sendet sie in die Cloud. Uptrends holt die Daten in [nahezu Echtzeit]([LINK_URL_4]) ab und zeigt sie in deinen RUM-Dashboards. Das Ergebnis ist ein umfassendes Bild der tatsächlichen Performance deiner Website, wie sie von deinen Besuchern erlebt wird. Wenn du dir Sorgen über den Datenschutz deiner Nutzer machst, erfährst du mehr mit unserem Knowledge-Base-Artikel zum [RUM und Nutzer-Datenschutz]([LINK_URL_5]).

## Wie sieht ein RUM-Skript aus?

Uptrends’ Programmierer haben das RUM-Skript so entwickelt, dass es so wenig wie möglich in die Website eingreift. Das kleine Skript lädt fast ohne Auswirkung auf die Seiten-Performance. Das Skript arbeitet im Hintergrund, während das Laden der Seite fortläuft. Nach vollständigem Laden beendet das Skript seine Arbeit und sendet die Nutzer- und Performance-Daten in die Cloud. Dein Skript wird ähnlich aussehen wie das Skript unten.
[CODE_BLOCK_1]
