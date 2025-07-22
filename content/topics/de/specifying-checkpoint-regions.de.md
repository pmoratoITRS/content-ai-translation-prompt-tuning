{
  "hero": {
    "title": "Auswahl von Checkpoint-Regionen"
  },
  "title": "Auswahl von Checkpoint-Regionen",
  "summary": "Die Auswahl Ihrer Checkpoints, wenn Ihr Konto Sie auf komplette Regionen beschränkt.",
  "url": "/support/kb/api/auswahl-von-checkpoint-regionen",
  "translationKey": "https://www.uptrends.com/support/kb/api/specifying-checkpoint-regions"
}

Bei Konten, bei denen nur ganze Checkpoint-Regionen ausgewählt werden können, um das Monitoring auszuführen (im Gegensatz zu unbeschränkter Auswahl individueller Checkpoints), muss ein Spezialwert eingegeben werden, wenn Monitorings in der API erstellt und aktualisiert werden.  
Geben Sie in das Feld „Checkpoints“ (das in der Regel eine kommagetrennte Liste von Checkpoint-IDs enthält), eine dieser Phrasen ein:

-   Nur Europa: `` `{"Regions":[1004]}` ``
-   Nur Nordamerika: `` `{"Regions":[1005]}` ``
-   Beides: Lassen Sie das Feld frei oder geben Sie `'{"Regions":[1004,1005]}'` ein.
