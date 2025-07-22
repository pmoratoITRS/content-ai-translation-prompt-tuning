{
  "title": "Zusätzliche Bedingungen zur Prüfung von URLs, die von der Seite geladen werden",
  "date": "2025-02-19",
  "url": "[URL_BASE_CHANGELOG]februar-2025-zusaetzliche-bedingungen-von-der-seite-geladene-urls-ueberpruefen-fehlerbedingungen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[Von der Seite geladene URLs überprüfen]([LINK_URL_1]) ist eine Fehlerbedingung, die prüft, ob bestimmte Seitenobjekte von deiner Website geladen werden. Diese Seitenobjekte sind die URLs, die in deinem [Wasserfalldiagramm]([LINK_URL_2]) angezeigt werden, darunter für Bilder, Dateien und andere Website-Ressourcen.

Diese Fehlerbedingung ermöglicht nun, gesonderte Kriterien zur Überprüfung der Messwerte für jedes Seitenobjekt festzulegen. Durch Klicken der neuen Schaltfläche [SHORTCODE_1] +Zusätzliche Bedingung hinzufügen[SHORTCODE_2] kannst du nun die Antwortgröße des Seitenobjekts in Bytes (B), die Gesamtzeit in Millisekunden (ms) und den Statuscode angeben:

![Zusätzliche Bedingungen für von der Seite geladene URLs überprüfen]([LINK_URL_3])

Möchtest du eine Fehlermeldung, wenn ein Bild länger als 2 Sekunden zum Laden benötigt oder wenn eine Datei einen Statuscode höher als 400 wiedergibt, kannst du jeweils spezifische Kriterien hinzufügen.

Die Fehlerbedingung „Von der Seite geladene URLs überprüfen‟ ist für [Browser- und Full Pagecheck-]([LINK_URL_4]) sowie [Transaktionsprüfobjekte]([LINK_URL_5]) verfügbar. Beachte, dass bei Transaktionsprüfobjekten die [Wasserfall-Option in einem Schritt]([LINK_URL_6]) ausgewählt sein muss, um zusätzliche Bedingungen einzurichten.