{
  "hero": {
    "title": "Uptrends und Cloudflare für maximale Sicherheit zusammen einsetzen"
  },
  "title": "Uptrends und Cloudflare für maximale Sicherheit zusammen einsetzen",
  "summary": "Finde heraus, wie Cloudflare und Uptrends im Allgemeinen funktionieren und was du beachten solltest, wenn du beide verwendest. ",
  "url": "/support/kb/synthetic-monitoring/checkpoints/cloudflare",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/cloudflare"
}

Du stützt dich eventuell auf Cloudflares Services, um deine Websites und APIs zu sichern und zu schützen. Im Rahmen dieser Services blockiert Cloudflare den eingehenden Traffic von bösartigen Nutzern, die automatisierte Tools oder Bots (manchmal im Rahmen eines Bot-Netzwerks) verwenden, um Zugriff auf Ressourcen zu erhalten, die deine Websites und APIs bereitstellen. 

Cloudflare nutzt verschiedene Technologien wie Rate Limiting, IP- und Länderblockierung, Anti-DDoS-Technologie und CAPTCHA, um Anfragen von rechtmäßigen Nutzern zu verifizieren und solche von automatisierten Bots zu blockieren. 

Cloudflare bietet auch einen Dienst für verifizierte Bots, über den du bestimmte Bots benennen kannst, die Zugriff auf deine Websites und APIs haben sollen. Dieser Dienst stellt sicher, dass Anfragen von den benannten Bots bestätigt und gestattet werden, während alle anderen Bots gesperrt bleiben, sodass du eine zusätzliche Sicherheit für deine Websites erhältst.

## Uptrends ist ein verifizierter Bot

Bei den Monitoring-Aktivitäten, die von Uptrends durchgeführt werden, um die Verfügbarkeit und Performance deiner Webseiten, User Journeys und APIs zu prüfen, handelt es sich tatsächlich um Bot-Aktivitäten: Automatisierte Prozesse werden verwendet, um laufend auf deine Webserver zuzugreifen. 

Uptrends ist einer der verifizierten Bot-Partner von Cloudflare. Cloudflare kennt Uptrends’ öffentliche Monitoring-Standorte – das Checkpoint-Netzwerk – und aktualisiert regelmäßig die Liste der IP-Adressen (IPv4 und IPv6), von denen aus die Überwachung deiner Websites stattfindet.

Das bedeutet, wenn du Cloudflare und Uptrends zusammen konfigurierst, sind deine Website und API-Ressourcen gegen bösartige Bots geschützt, während der Monitoring-Traffic von Uptrends durch die Cloudflare Firewall gestattet ist.

## Die Liste verifizierter Bots

Im Rahmen von Cloudflare Radar wird eine Liste ausgewählter Bots unter [Verifizierte Bots](https://radar.cloudflare.com/de-de/bots#verified-bots) veröffentlicht. Alle rechtmäßigen Services können beantragen, in der Liste der Bots, denen Cloudflare vertraut, aufgenommen zu werden. 

Uptrends hat den Antragsprozess durchlaufen und Cloudflare hat bestätigt, dass Uptrends ein unbeschränkt verifizierter Bot ist. Leider veröffentlicht Cloudflare nur einen Teil der Liste der von ihnen verifizierten Bots, sodass du Uptrends nicht auf der Liste finden wirst, obwohl es vollständig verifiziert ist.

## Fehlerbehebung

Trotz Cloudflares Bestätigung, dass Uptrends ein verifizierter Bot ist und dass die IP-Adressen der Checkpoint-Server von Cloudflare in einer Whitelist geführt werden, melden einige Nutzer von Uptrends gelegentlich Probleme. 

In dem Fall, dass Cloudflare eingehenden Traffic von einem der Checkpoint-Standorte blockiert, erscheint es aus Monitoring-Perspektive so, als sei deine Website nicht verfügbar. 

Sollte es zu unerwarteten Ausfällen kommen, die vielleicht dadurch verursacht werden, dass Cloudflare eingehenden Traffic von Uptrends blockiert, folge bitte diesen Schritten:

- Siehe in der Cloudflare-Dokumentation nach, [wie vertrauenswürdige Bots verwaltet werden](https://www.cloudflare.com/de-de/learning/bots/how-to-manage-good-bots/). Dieser Artikel erläutert Zulassungslisten, Blocklisten und wie die Regeln eingerichtet werden, damit Bots auf eine Website oder Anwendung zugreifen können.

- Achte darauf, welche Checkpoint-Standorte Probleme haben, deine Website oder API aufzurufen, und welche nicht. Reiche dann ein Ticket mit diesen Informationen beim [Uptrends Support]({{< ref path="contact" lang="de" >}}) ein. So können wir feststellen, ob das Problem im Zusammenhang mit den Cloudflare-Zulassungslisten oder aufgrund einer anderen Ursache besteht.

- Wende dich an den [Cloudflare Support](https://dash.cloudflare.com/support), wenn du Konfigurationsänderungen an deinen Cloudflare-Firewall-Regeln vornehmen willst. Denk daran, die Cloudflare-Dokumentation hinsichtlich [Maßnahmen zu Firewall-Regeln](https://developers.cloudflare.com/firewall/cf-firewall-rules/actions/) zu lesen.

Wir arbeiten mit Cloudflare daran, diese Probleme zu lösen. Dein Feedback ist wichtig, um die Ursache zu verstehen.