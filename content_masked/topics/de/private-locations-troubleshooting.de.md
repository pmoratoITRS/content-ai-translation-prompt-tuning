{
  "hero": {
    "title": "Private Locations – Fehlerbehebung"
  },
  "title": "Private Locations – Fehlerbehebung",
  "summary": "Hinweise zur Fehlerbehebung und Beispiele zur Fehlerbehebung an deinen privaten Standorten Locations.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/private-locations-fehlerbehebung",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Die Installation eines privaten Standorts erfolgt voll automatisiert. Du hast anschließend einen aktiven Container-Checkpoint, der sich selbst auf dem neuesten Stand hält und Messungen für Prüfobjekte ausführen kann. Dieser Leitfaden zeigt Schritte auf, anhand derer du deine [Installation des privaten Standorts verifizieren]([LINK_URL_1]) und deine [Einrichtung einem Smoke Test unterziehen]([LINK_URL_2]) sowie wie du [Probleme lösen]([LINK_URL_3]) kannst, die während oder nach der Installation eines privaten Standorts aufgetreten sind. 

## Installation eines privaten Standorts verifizieren

Der erste Schritt besteht darin zu verifizieren, dass dein privater Standort korrekt [installiert und eingerichtet]([LINK_URL_4]) ist. Das automatisierte Installationspaket ist vorkonfiguriert und umfasst drei Schritte.

- Installation der Grundvoraussetzungen (einschließlich eines Neustarts, sofern erforderlich).
- Herunterladen der Uptrends Container Images von Azure
- Installation der Auto-run- und Auto-update-Funktionen


### Installation der Grundvoraussetzungen
Drei Grundvoraussetzungen zur Ausführung der Uptrends Container Images werden installiert: die „Containers“ Windows-Funktion, Docker Engine und Docker Compose. Die Installation der Containers Windows-Funktion erfordert eventuell einen Neustart. Dafür wird eine Aufforderung eingeblendet. Nach dem Neustart wird die Installation automatisch (über einen geplanten Task) fortgesetzt.

Wenn du prüfen möchtest, dass diese drei Voraussetzungen korrekt installiert sind, kannst du drei Befehle ausführen. 

Liste zunächst alle Windows-Funktionen und prüfe, ob „Containers“ in der Liste enthalten ist:
1. Öffne eine PowerShell-Konsole im Admin-Modus. 
2. Wechsle zu dem Ordner, in dem die docker-compose.yml-Datei abgelegt ist, und führe den Befehl `[INLINE_CODE_1][INLINE_CODE_2][INLINE_CODE_3][INLINE_CODE_4][INLINE_CODE_5][INLINE_CODE_6][INLINE_CODE_7][INLINE_CODE_8][INLINE_CODE_9][INLINE_CODE_10][INLINE_CODE_11][INLINE_CODE_12][INLINE_CODE_13][INLINE_CODE_14][INLINE_CODE_15][INLINE_CODE_16][INLINE_CODE_17][INLINE_CODE_18][INLINE_CODE_19][INLINE_CODE_20][INLINE_CODE_21][INLINE_CODE_22][INLINE_CODE_23][INLINE_CODE_24][INLINE_CODE_25][INLINE_CODE_26]docker-compose up -d[INLINE_CODE_27]docker-compose down[INLINE_CODE_28]docker-compose restart[INLINE_CODE_29][INLINE_CODE_30][INLINE_CODE_31][INLINE_CODE_32][INLINE_CODE_33][INLINE_CODE_34][INLINE_CODE_35][INLINE_CODE_36][INLINE_CODE_37][INLINE_CODE_38][INLINE_CODE_39]Docker-compose logs -t -n 5000[INLINE_CODE_40][INLINE_CODE_41][INLINE_CODE_42][INLINE_CODE_43][INLINE_CODE_44][INLINE_CODE_45][INLINE_CODE_46][INLINE_CODE_47][INLINE_CODE_48][INLINE_CODE_49][INLINE_CODE_50][INLINE_CODE_51][INLINE_CODE_52][INLINE_CODE_53][INLINE_CODE_54][INLINE_CODE_55][INLINE_CODE_56][INLINE_CODE_57][INLINE_CODE_58][INLINE_CODE_59], und prüfe die zurückgegebene IP-Adresse. Sollte dies zu einer Zeitüberschreitung führen, ist die Anwendung vom Container nicht erreichbar (und kann dann nicht überwacht werden).

Sollte keiner der Schritte zum Erfolg führen, versuche Folgendes:

- Vergleiche die ipconfig vom Host mit der im Container (`[INLINE_CODE_60][INLINE_CODE_61][INLINE_CODE_62]`. Wenn es korrekt funktioniert, ohne die öffentliche DNS’ IP-Adresse zu nutzen, aber Probleme auftreten, wenn keine IP-Adresse angegeben ist, kann der Fehler bei der DNS-Auflösung liegen. Beachte, dass der Einsatz von 8.8.8.8 als DNS-Server in Produktion nicht wünschenswert ist, da er nicht die Adresse interner Anwendungen auflösen kann.

Gib spezifische DNS-Server in der Compose-Datei, wie im Code unten gezeigt, an. Dies muss für beide Container in der yaml-Datei erfolgen.

[CODE_BLOCK_4]

Gib die IP-Adressen der DNS-Server ein, die du nutzen möchtest. Du kannst diese für probemaster1.uptrends.com wie auch den Hostnamen anhand von nslookup testen. Achte darauf, dies in einem Container auszuführen.

Du wirst eventuell DNS-Anfragen von den Docker-Containern erlauben müssen, falls deine DNS-Server eine Allow-Liste nutzen. Wenn du Container-Checkpoints auf einer Cloud-Plattform wie Google Cloud, AWS oder Azure ausführst, sind eventuell zusätzliche Konfigurationen erforderlich, um die Verbindung aus den Docker-Containern zu gewährleisten. 

## Funktioniert die Einrichtung immer noch nicht? 

Sollte dir zu irgendeinem Zeitpunkt bei der Problembehebung etwas nicht klar sein, oder wenn du sonstige Fragen hast, wende dich bitte an Uptrends, indem du ein [Support-Ticket]([LINK_URL_14]). einreichst. Wir werden uns so schnell wie möglich zurückmelden. 