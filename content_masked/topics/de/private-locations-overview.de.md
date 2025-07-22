{
  "hero": {
    "title": "Private Locations – Überblick"
  },
  "title": "Private Locations – Überblick",
  "summary": "Nutze private Standorte, um deine Checkpoints zu verwalten.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-standorte/ubersicht-uber-private-standorte",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

[SHORTCODE_1] **Hinweis:** Uptrends bietet eine 30-Tage-Testversion für Private Locations! Weitere Informationen findest du im Abschnitt [Private Locations – Testversion]([LINK_URL_1]). [SHORTCODE_2] 

Im Allgemeinen überwacht Uptrends Websites, Anwendungen und APIs anhand seines globalen Netzwerks [öffentlicher Checkpoint-Standorte]([LINK_URL_2]). Es gibt jedoch auch Situationen, in denen man intern ein Monitoring durchführen sollte. Dafür stellt Uptrends die **Private Locations** (auch private Standorte genannt) bereit. Sie ermöglichen dir, Prüfobjekte auf deinem eigenen Server und hinter deiner Firewall auszuführen.

Mit **Private Locations** können Checkpoints erstellt, definiert und gruppiert werden – auf Grundlage eines bestimmten Zwecks, Einsatzes oder physischen Standorts (etwa eine Stadt, ein Land oder ein Kontinent). Uptrends stellt die erforderliche Software-Installationsanweisungen bereit, aber du hast die volle Kontrolle und bist verantwortlich für die Verwaltung der internen Hardware-Infrastruktur, Installation, Updates und weitere [Einrichtungsanforderungen]([LINK_URL_3]).

Um auf **private Standorte** in der Uptrends Webanwendung zuzugreifen, rufe [SHORTCODE_3] Private Locations [SHORTCODE_4] auf.

![Screenshot Private Locations]([LINK_URL_4])

## Privaten Standort hinzufügen

Um einen neuen Standort hinzufügen:

1. Gehe zu [SHORTCODE_5] Private Locations [SHORTCODE_6].
2. Klicke auf [SHORTCODE_7] Standort hinzufügen [SHORTCODE_8].
3. Gib den Name des Standorts ein, von dem aus du die Überwachung durchführen möchtest.
4. Wähle eine [Prüfobjektgruppe]([LINK_URL_5]), die über die Berechtigung zur Erstellung von Prüfobjekten verfügt. Die Prüfobjekte zur Überwachung des Status werden in dieser Gruppe erstellt. Prüfobjektgruppen mit den erforderlichen Berechtigungen werden im Drop-down-Menü aufgelistet.
5. Klicke auf [SHORTCODE_9] Private Location hinzufügen [SHORTCODE_10].

 Der neue Standort wird erstellt und zur Liste privater Standorte hinzugefügt. Standardmäßig werden zwei nicht konfigurierte und nicht installierte Checkpoints hinzugefügt. Die [FAQ]([LINK_URL_6]) enthalten eine Erläuterung, weshalb zwei Checkpoints hinzugefügt werden (und nicht nur einer).

Um einen privaten Standort umzubenennen, klicke auf die Schaltfläche [SHORTCODE_11] [SHORTCODE_12] vor dem Namen.

## Checkpoint hinzufügen

Beachte, dass ein neuer privater Standort zwei Checkpoints, die automatisch hinzugefügt werden, mit sich bringt. Du kannst diese zunächst installieren sowie weitere Checkpoints (jetzt oder später) hinzufügen.

Um einen **Checkpoint** hinzuzufügen:

1. Gehe zu [SHORTCODE_13] Private Locations [SHORTCODE_14] im Menü.
2. Klicke auf [SHORTCODE_15]Checkpoint hinzufügen [SHORTCODE_16] bei dem Standort, bei dem du einen Checkpoint hinzufügen möchtest.
3. Wähle eine Prüfobjektgruppe mit der Berechtigung, Prüfobjekte zu erstellen. Das Prüfobjekt zur Überwachung des Status des Checkpoints wird in dieser Gruppe erstellt.
4. Klicke auf die [SHORTCODE_17] Checkpoint hinzufügen [SHORTCODE_18]-Schaltfläche.

Um einen **Checkpoint** umzubenennen:

Klicke auf den Checkpoint, um die Seite zu öffnen, und dann auf die Bearbeiten-Schaltfläche [SHORTCODE_19] [SHORTCODE_20] hinter dem Namen. Gib einen neuen Namen ein.

Der von dir hinzugefügte Checkpoint existiert nur als digitale Repräsentation in der Uptrends Webanwendung. Der Checkpoint, der die Überwachung ausführt, muss auch installiert werden.

Um einen Checkpoint zu installieren, folge den Schritten wie in [Einen Docker-Checkpoint installieren]([LINK_URL_7]) aufgeführt. Weitere Informationen zu Private Locations findest du unter [Private Locations nutzen]([LINK_URL_8]).

## Private Locations – Testversion

Uptrendsʼ **Private Locations Testversion** ist für alle Account-Nutzer verfügbar. Die Testversion ermöglicht die Einrichtung eines **Privaten Standorts**, um ihn auszuprobieren und mit deinen bestehenden Prüfobjekten zu nutzen.

Damit du ausreichend Zeit für die Vorbereitung hast, bleibt die Testversion bestehen, bis du den ersten privaten Standort auf der Uptrends Plattform erfolgreich installiert hast. Vor dem Hintergrund hast du bereits alle notwendigen [Voraussetzungen]([LINK_URL_9]) erfüllt und [einen privaten Docker-Container-Checkpoint installiert und eingerichtet]([LINK_URL_10]).

Sobald dein erster privater Standort eingerichtet ist und ausgeführt wird, startet deine kostenfreie 30-Tage-Testversion. Beachte, dass das Enddatum festgelegt ist, ungeachtet ob die **privaten Standorte** bei einem Prüfobjekt-Checkpoint ausgewählt sind.

Um die Testversion zu verlängern oder in ein bezahltes Abonnement zu verwandeln, wende dich an deinen Account-Manager oder das [Support-Team]([LINK_URL_11]).
