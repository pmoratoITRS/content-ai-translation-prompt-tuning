{
  "hero": {
    "title": "Nicht primäre Checkpoints"
  },
  "title": "Nicht primäre Checkpoints",
  "summary": "Erfahre, warum Uptrends einige Checkpoint-Standorte als nicht primär einstuft und was du wissen solltest, bevor du sie auswählst.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/nicht-primare-checkpoints",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/non-primary-checkpoints"
}

Du hast möglicherweise bei der Auswahl von Checkpoints bemerkt, dass wir einige Checkpoints als *nicht primär* eingestuft haben. Nicht primäre Checkpoints sind Checkpoints, die einer zeitweilig unterbrochenen Verfügbarkeit und möglicherweise reduzierten Bandbreite aufgrund der lokalen Internetinfrastruktur und behördlichen Kontrolle unterliegen.

Wir haben entschieden, diese Checkpoints standardmäßig auszuschließen, wenn Du eine Region (siehe unten) auswählst, in denen sich diese befinden. Das heißt jedoch nicht, dass Du sie nicht nutzen sollst. Wir haben sie ausgeschlossen, um Dich darauf aufmerksam zu machen, dass für diese Checkpoints unbeständige Bedingungen gelten und dass dies sich negativ auf Deine Verfügbarkeits- und Performance-Berichte auswirken kann, solltest Du sie aktivieren. Um nicht primäre Checkpoints zu nutzen, deaktiviere das Kontrollkästchen **Ausschließliche Nutzung von Primary Checkpoints (empfohlen)**.

![](/img/content/32a8a159-b090-45cb-9a66-06a7ac9ce45e.png)

## Ich führe nur Tests in Regionen mit nicht primären Checkpoints durch, sehe aber Tests von anderen Checkpoints. Warum?

Obwohl es wichtig ist, vom Standort Deiner Nutzer zu testen, solltest Du dennoch wissen, wie es um den Status Deiner Website oder Deines Service bestellt ist, auch wenn der Standort nicht zum Testen verfügbar ist. Damit Deine Website oder Dein Service in solchen Fällen eingeschränkter oder gar keiner Verbindung mit nicht primären Checkpoints nicht unbewacht bleiben, wird Uptrends andere Checkpoints für die Tests nutzen. Auf diese Weise erfährst Du von Ausfällen oder Performance-Problemen, die in der Zwischenzeit auftreten könnten.
