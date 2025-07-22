{
  "hero": {
    "title": "User Agents und Real Browser Checks"
  },
  "title": "User Agents und Real Browser Checks",
  "summary": "User Agents sind eine großartige Möglichkeit, ein Synthetic Monitoring für bestimmte Nutzerumgebungen wie Mobilgeräte durchzuführen. In diesem Artikel wird erläutert, wie Real Browser Checks und User Agents für dich arbeiten können.",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/user-agents-und-real-browser-checks",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/user-agents-and-real-browser-checks"
}

Wenn du das Thema User Agents und Real Browser Monitoring verwirrend findest, keine Sorge, du bist nicht allein. Die Frage nach den User Agents und ihre Anwendung beim Real Browser Monitoring gehört zu den meistgestellten Fragen an unser Support-Team. Die kurze Antwort lautet:

Real Browser Checks (Full Pagecheck und Transaktions-Monitoring) verwenden einen tatsächlichen Browser (genauso wie deine Website-Besucher), um die Inhalte einer Website abzurufen und zu laden. Der Browser erzeugt einen User Agent, der deinen Servern von der Umgebung des Nutzers berichtet. Der User Agent erlaubt dem Server, für die spezielle, vom User Agent definierte Umgebung optimierte Inhalte zurückzugeben. Du kannst den User Agent bei deinen Prüfobjekten so einrichten, dass die Inhalte für andere Browser, Betriebssysteme und Geräte wie Mobiltelefone und Tablets getestet werden.

Ok, das war jetzt nicht wirklich kurz, aber wenn dir die Antwort reicht – hervorragend! Wir anderen steigen noch etwas tiefer in das Thema ein. Sehen wir uns zunächst die drei Hauptkomponenten von HTTP-Kommunikationen an.

## Die Beteiligten

Kommunikation ist eine Straße mit zwei Richtungen zwischen zwei Parteien. Eine Partei fragt nach Informationen, die andere Partei gibt die Informationen. Dieser Informationsaustausch wird durch Sprache ermöglicht. Damit beide Parteien sich verstehen, müssen sie dieselbe Sprache sprechen. Sehen wir uns die Beteiligten an.

-   **Client**: Der Client fragt nach etwas aus einer Ressource. Der Client kann ein Internetbrowser oder eine andere Art von Softwareanwendung wie zum Beispiel ein Webcrawler sein.
-   **HTTP:** Die gemeinsame Sprache. Das Hypertext Transfer Protocol legt die Bedeutung der Kommunikation eindeutig fest.
-   **Server**: Der Server sendet die Informationen zurück an den Client – für den Client auf Grundlage des User Agents angepasst.

Ein Client nutzt eine HTTP-Anfrage, um Informationen vom Server abzufragen. Der Server sendet die Informationen als HTTP-Antwort zurück. Also was hat das alles mit Real Browser Checks und User Agents zu tun? Sehen wir uns den User Agent zuerst an.

## Was ist ein User Agent?

Ein User Agent ist ein besonderes Feld der HTTP-Anfrage, das Informationen zum Client enthält. Der Server sucht nach bestimmten Wörtern im Text und ignoriert alles andere. Davon abhängig, was der Server im Text des User Agents findet (oder nicht findet), baut der Server den Inhalt optimiert für den Client auf. Der User Agent enthält:

-   Browsertyp und Browserversion
-   Betriebssystem und Version
-   Rendering Engine

Um das Ganze noch verwirrender zu machen, enthält der User Agent Informationen wie etwa den Text „Mozilla/5.0“ (bei den meisten Browser User Agents), was dem Server signalisiert, dass dieser Client mit diesem Browser kompatibel ist.

Der User Agent von Chrome sagt dem Server, dass er ein Mozilla/5.0 Browser, ein Safari Browser und ein Chrome Browser ist, wie du beim User Agent unten sehen kannst.

`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36`

## Was ist ein Real Browser Check?

Wie oben beschrieben kann der Client jede Art von Softwareanwendung sein, die über das Internet kommunizieren kann. Ein Internetbrowser ist nur eine Art von Client. Softwareanwendungen sind voll zufrieden damit, sich die Kommunikation im Rohformat anzusehen, aber der Endbenutzer würde das nicht mögen. Für die Endbenutzer nimmt der Browser den zurückgegebenen Inhalt, analysiert ihn und zeigt ihn aufbereitet auf dem Bildschirm an.

Du kannst deine Website testen, indem du einen [einfachen Prüfobjekttypen oder einen Real Browser Check]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/basic-webpage-checks-versus-real-browser-checks" lang="de" >}}) wählst. Uptrends’ Checkpoints können entweder einen Browser verwenden oder halt auch nicht, je nachdem, welchen Prüfobjekttypen du gewählt hast. Die einfachen Prüfobjekte HTTP und HTTPS senden eine Anfrage an den Server (ohne Einsatz eines Browsers). Wenn der Checkpoint-Computer die Antwort erhält, sucht er nach einem Ergebnis-Code, eventuell nach bestimmten Inhalten und einigen grundlegenden Elementen. Die Antwort wird niemals verarbeitet, Bilder werden niemals heruntergeladen und Skriptdateien niemals ausgeführt. Dieser Check sagt dir, ob deine Website verfügbar oder ausgefallen ist.

Wenn du dich für das Real Browser Monitoring entscheidest, wird Uptrends' Checkpoint-Computer ein Browserfenster öffnen und eine Anfrage an den Server senden, wie dies auch deine Website-Besucher mit einem Browser machen. Die Antwort wird entgegengenommen, verarbeitet, Bilder werden heruntergeladen, Skriptdateien ausgeführt und CSS-Dateien angewendet und die Seite erscheint im Browserfenster. Ein Real Browser Check wie der [Full Page Check]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="de" >}}) kann dir Dinge wie die Verbindungs- und Ladezeiten für jedes Element der Seite sowie nicht ausgeführte Inhalte sagen. Wir können sogar einen Screenshot erstellen, wenn ein Seitenfehler auftritt.

## Wo ist nun die Überleitung zwischen User Agents und das Real Browser Monitoring?

Du kannst den User Agent sowohl für das nicht browserbasierte wie auch das browserbasierte Monitoring ändern. Du möchtest vielleicht den User Agent für einfache Prüfobjekte ändern, sodass du Inhalts-Checks für bestimmte Nutzer-Umgebungen durchführen kannst. Du wirst sehen, dass die wahre Stärke im Einsatz eines echten Browsers liegt. Durch Ändern des User Agents kannst du die Performance und die Inhalte einer Seite für die meisten Umgebungen testen. Sehen wir uns einige Beispiele an:

### Es ist eine Mobilgerät-orientierte Welt

Mobilgeräte überholen Desktop-Geräte hinsichtlich der Beliebtheit bei Nutzern mit großen Schritten. Es ist enorm wichtig, dass deine Server schnell bei der Arbeit mit mobilspezifischen Inhalten reagieren. Du denkst vielleicht, dass du neben manuellen Testen nicht viel unternehmen kannst. Weit gefehlt. Der Einsatz von User Agents bei einem Real Browser Check kann jedes Gerät, jede Bildschirmgröße und jeden Mobil-Browser emulieren. Deine Server werden mit deinen mobilen Inhalten antworten und unsere Real Browser Checks werden die Inhalte laden. Unten siehst du einige User Agents für beliebte Geräte, Betriebssysteme und Browser.

**Android Chrome**

`Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36`

**iPhone Safari**

`Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_4 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B350 Safari/8536.25`

**Amazon Fire**

`Mozilla/5.0 (Linux; U; Android 5.1; locale; device Build/build) AppleWebKit/webkit (KHTML, like Gecko) Version/4.0 Chrome/chrome Safari/safari`

### Test für nicht unterstützte Browser

Derzeit kannst du native Tests mit Chrome ausführen. Andere werden bald hinzugefügt. Den aktuellen nativen Browser zu verwenden, ist großartig, um für Nutzer zu testen, die ihren Browser regelmäßig aktualisieren. Ein großer Anteil von Nutzern führt das jedoch nicht durch. Deine Website funktioniert also möglicherweise sehr gut im aktuellen Chrome Browser, wie funktioniert sie aber in einem Browser-Release, das fünf Updates zurückliegt? Durch Ändern des User Agents kannst du jede Version des Browsers testen.

### Teste andere Betriebssysteme

Ein Chrome Browser, der auf einem Mac OSX ausgeführt wird, kann ein anderes Erlebnis erzeugen als der gleiche Chrome Browser auf Windows 10. Die einzige Möglichkeit, wie du dir sicher sein kannst, ist den User Agent anzupassen, sodass er andere Betriebssysteme und Versionen angibt. Wenn du den nativen Browser für den Checkpoint nutzt, wählt der User Agent standardmäßig das Betriebssystem des Checkpoints und die aktuelle Browserversion.
