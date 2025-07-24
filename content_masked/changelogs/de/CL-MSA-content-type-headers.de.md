{
  "title": "Automatische Content-Type-Header bei Multi-step API-Prüfobjekten",
  "date": "2024-01-17",
  "url": "[URL_BASE_CHANGELOG]januar-2024-msa-content-type-header",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Unser Prüfobjekttyp [Multi-step API]([LINK_URL_1]) ermöglicht Nutzern, mit ihren wichtigen APIs direkt zu interagieren. In einigen Monitoring-Fällen müssen Daten an die API gesendet werden, zum Beispiel, um POST-Abfragen, die ein neues Objekt erstellen, oder PUT/PATCH-Abfragen, die ein bestehendes Objekt aktualisieren, auszuführen. In diesen Fällen ist es wichtig, einen [INLINE_CODE_1] Header einzufügen, um die empfangende API über die Art der eingehenden Daten (JSON, XML, Formulardaten usw.) zu informieren, sodass diese weiß, wie die Abfrage analysiert werden muss. Eine API gibt häufig eine Fehlermeldung aus, wenn sie eine Abfrage ohne einen [INLINE_CODE_2] Header erhält.

Bislang mussten diese Header manuell in den Prüfobjektschritt bzw. -schritten beim Multi-step API Monitoring eingetragen werden. Mit diesem Update wird der Inhaltstyp automatisch erkannt und der korrekte [INLINE_CODE_3] Header für Abfragen mit JSON, XML oder Formulardaten angegeben. Diese Änderung hilft Nutzern, POST-, PUT- und PATCH-Abfragen bei ihren Multi-step API-Prüfobjekten zu konfigurieren.