{
  "hero": {
    "title": "Überblick – Single Sign-on"
  },
  "title": "Überblick – Single Sign-on",
  "summary": "Erfahre, wie Uptrends und Dein Single Sign-on (SSO)-Anbieter zusammenarbeiten, um das Nutzermanagement zu verbessern und Nutzern ein schnelleres, reibungsloseres Anmeldeverfahren zu bieten.",
  "url": "/support/kb/account/einstellungen/ueberblick-single-sign-on",
  "translationKey": "https://www.uptrends.com/support/kb/account/single-sign-on-overview"
}

Wenn ein Uptrends Account zum ersten Mal eingerichtet wird, erstellt der Account-Administrator ein Login für sich selbst mit seiner E-Mail-Adresse und einem selbst gewählten Passwort. Zusätzliche Operator können mit der Zeit eingerichtet werden, um mehr Personen Zugang zum Account zu gewähren. Dabei erhält jeder Operator eigene Anmeldedaten mit seiner E-Mail-Adresse und einem Passwort.

Dieses Vorgehen funktioniert in der Regel gut. Aber wenn sich das Unternehmen verändert oder wächst und das Team mehr Online-Tools und -Services nutzt, gibt es einiges zu beachten:

- Mitarbeiter müssen sich ihr Passwort für Uptrends merken, neben den Passwörtern aller anderen Online-Tools, die sie verwenden.
- Sie müssen sich jedes Mal manuell anmelden, wenn sie auf Uptrends zugreifen.
- Aus der Perspektive des Nutzermanagements kann es immer schwieriger werden, den Überblick und die Kontrolle darüber zu haben, wer zu welchen Tools Zugang hat.

## Einfachere und sicherere Zugangskontrolle mit Single Sign-on

Damit dies sowohl für Endnutzer als auch Administratoren für alle Online-Apps, die das Team nutzt, leichter wird, kannst Du eine Lösung einsetzen, die zwischen den Nutzern und diesen Online-Apps geschaltet ist. Es gibt viele Produkte externer Anbieter, die eine Single Sign-on (SSO)-Lösung bereitstellen. Wir haben mit [Azure Active Directory](https://azure.microsoft.com/de-de/services/active-directory/), Active Directory Federation Services (ADFS), [Okta](https://www.okta.com/), [OneLogin](https://www.onelogin.com/), [SecureAuth](https://www.secureauth.com/) und [Duo Access Gateway](https://duo.com/docs/dag) gearbeitet, aber es gibt noch viele weitere. Jedes Produkt, das das [SAML 2.0-Protokoll](https://de.wikipedia.org/wiki/Security_Assertion_Markup_Language) für Single Sign-on unterstützt, sollte geeignet sein.

## Single Sign-on bei Uptrends

Wie erwähnt benötigst Du ein Produkt eines externen Anbieters, das als zentrale Stelle für die Nutzer agiert, um auf Anwendungen zuzugreifen, und damit Administratoren steuern können, welche Nutzer Zugang zu welchen Anwendungen wie z. B. Uptrends haben. In diesem Artikel beziehen wir uns mit der Bezeichnung **Identity Provider (IdP)** auf dieses Produkt, da es die Identität eines jeden Nutzers verwaltet, wenn dieser sich bei den Anwendungen anmeldet. In diesem Szenario ist Uptrends eine dieser Anwendungen und übernimmt die Rolle des **Service Providers (SP)**.

Sobald Du einen IdP eingerichtet hast, verwendest Du die Funktionen der IdP-Anmeldung, um sicherzustellen, dass Deine Nutzer unter anderem in ihrem Browser und auf Mobilgeräten authentifiziert sind – häufig auf Grundlage ihrer Netzwerk-Anmeldedaten. Diese Funktionen umfassen auch die Zwei-Faktor-Authentifizierung, strenge Passwortrichtlinien usw. Der Hauptvorteil für die Endnutzer besteht darin, dass sie sich nicht mehr an unterschiedliche Passwörter für unterschiedliche Anwendungen erinnern müssen. Sie können auf Uptrends und andere Anwendungen mit einem Klick zugreifen. Die meisten IdPs stellen eine App-Galerie oder eine App-Zentrale bereit, die alle für den Nutzer verfügbaren Tools und Services zeigen. Tools sind sofort erkennbar und zugänglich, ohne dass Nutzer URLs als Lesezeichen abspeichern, sich an das richtige Passwort erinnern und die üblichen lästigen Prozesse durchlaufen müssen, damit die Dinge sicher und organisiert bleiben.

Eine SSO-Einrichtung ist für Administratoren vorteilhaft, da sie kontrollieren, welche Nutzer Zugang auf Uptrends haben. Dieser Zugang kann genauso leicht widerrufen werden, wenn ein Mitarbeiter das Unternehmen verlässt oder das Team wechselt.

## Single Sign-on – Einrichtungsüberblick

Zur Nutzung einer SSO-Einrichtung in Uptrends sind die folgenden Schritte notwendig:

- **Aktiviere die SSO-Option** in Deinen Account-Einstellungen. Beachte, dass das Single Sign-on nur in Enterprise Accounts verfügbar ist.
- **Definiere eine neue App in Deinem Identity Provider** anhand der SAML-Konfigurationsdaten, die Uptrends bereitstellt. Im Grunde musst Du nur eine URL kopieren: Das ist die Single Sign-on-URL (auf der Uptrends-Seite), die einzigartig für die SSO-Einrichtung deiner Organisation ist. Dein IdP benötigt diese URL, damit Deine Nutzer an die richtige Stelle geleitet werden, wenn sie sich anmelden.
- Sobald die Definition erfolgt ist, wird die neue Uptrends App in Deinem IdP ebenfalls SAML-Konfigurationsdaten erzeugen. Diese Daten bestehen aus zwei Informationen: **die Anmelde-URL Deines IdPs** (damit Uptrends weiß, wo Deine Nutzer herkommen) und das **von Deinem IdP generierte Zertifikat**, um die SAML-Anfragen digital zu signieren, die an Uptrends gesendet werden. Dadurch kann Uptrends absolut sicherstellen, dass die eingehenden Anmeldungen tatsächlich von Deinem Identity Provider stammen und nicht von einer anderen Person. Es ist ein unerlässlicher Bestandteil der Sicherheit des Single Sign-ons. Den öffentlichen Schlüssel/Public Key für das SSO speicherst Du in Deiner [Uptrends Vault](/support/kb/vault).
- Stelle sicher, dass **Deine Nutzer auf beiden Seiten definiert sind**: Dein IdP wird in Deiner eigenen Umgebung ausgeführt, also kennt es Deine Nutzer schon. Bei Uptrends wird jeder Nutzer als eigener Operator geführt (und muss eingerichtet werden, wenn er nicht schon besteht). Wenn ein Nutzer von Deinem IdP angemeldet wird, prüfen wir die E-Mail-Adresse. Sie muss auf beiden Seiten gleich sein.
- Du musst das SSO nicht direkt für alle Nutzer einrichten. Du kannst mit einem anfangen, während die anderen Nutzer Uptrends weiterhin mit den klassischen Logins aufrufen, bis Du sie im SSO eingerichtet hast.

Detaillierte Einrichtungsanweisungen findest Du unter [Single Sign-on Setup Guide](/support/kb/account/einstellungen/sso-setup-guide).

## Anmeldung von SSO-Nutzern {id="how-sso-users-log-in"}

Nachdem die Einrichtung des Single Sign-ons abgeschlossen ist, solltest du Nutzern Anweisungen zur Anmeldung bei Uptrends geben. Zum Beispiel Anweisungen dazu, welche Seite Du zur Anmeldung beim Uptrends Account aufrufen sollten. Es gibt zwei Möglichkeiten:

1. Richte das *IdP-initiated SSO* Mit dieser Methode verfügen deine Nutzer über einen zentralen Ort (häufig eine Webseite, die mithilfe deiner IdP-Software in Form einer *App-Galerie* gehostet wird), um sich bei Uptrends oder anderen SSO-aktivierten Services anzumelden. Die App-Galerie enthält einen besonderen Link zu Uptrends, über den der SSO-Anmeldevorgang gestartet wird. Die Methode wird IdP-initiiert genannt, da die ersten Schritte zur Anmeldung auf Seiten des Identity Providers erfolgen.
2. Richte das *SP-initiated SSO* Bei dieser Methode wird davon ausgegangen, dass Du nicht über eine zentrale App-Galerie oder ein Portal verfügst, sondern dass deine Nutzer selbst den SSO-aktivierten Dienst aufrufen müssen. Du musst den Namen deiner Organisation auf der SSO-Anmeldeseite von Uptrends eingeben, um den Anmeldevorgang zu initiieren, der eine Verbindung mit deinem Identity Provider errichtet. Alternativ kannst du ein Lesezeichen zur Subdomain "your-company.uptrends.com" erstellen. Bitte [wende dich an unseren Support](/contact), wenn du die SP-initiierte Anmeldemethode verwenden möchtest. Unser Support stellt dann sicher, dass deine Subdomain eingerichtet wird.
