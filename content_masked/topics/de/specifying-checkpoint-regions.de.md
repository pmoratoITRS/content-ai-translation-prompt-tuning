{
  "hero": {
    "title": "Auswahl von Checkpoint-Regionen"
  },
  "title": "Auswahl von Checkpoint-Regionen",
  "summary": "Die Auswahl Ihrer Checkpoints, wenn Ihr Konto Sie auf komplette Regionen beschränkt.",
  "url": "[URL_BASE_TOPICS]api/auswahl-von-checkpoint-regionen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Bei Konten, bei denen nur ganze Checkpoint-Regionen ausgewählt werden können, um das Monitoring auszuführen (im Gegensatz zu unbeschränkter Auswahl individueller Checkpoints), muss ein Spezialwert eingegeben werden, wenn Monitorings in der API erstellt und aktualisiert werden.  
Geben Sie in das Feld „Checkpoints“ (das in der Regel eine kommagetrennte Liste von Checkpoint-IDs enthält), eine dieser Phrasen ein:

-   Nur Europa: `[INLINE_CODE_1]{"Regions":[1004]}[INLINE_CODE_2][INLINE_CODE_3][INLINE_CODE_4]{"Regions":[1005]}[INLINE_CODE_5][INLINE_CODE_6]'{"Regions":[1004,1005]}'` ein.
