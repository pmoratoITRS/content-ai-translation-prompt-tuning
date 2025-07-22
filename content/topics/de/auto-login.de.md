{
  "hero": {
    "title": "Auto-Login"
  },
  "title": "Auto-Login",
  "url": "/support/kb/basics/auto-login",
  "summary": "Direkte Anmeldung/automatische Anmeldung (mit Benutzername/Passwort in einem Lesezeichen-URL)",
  "translationKey": "https://www.uptrends.com/support/kb/basics/auto-login"
}

## Direkte Anmeldung/automatische Anmeldung (mit Benutzername/Passwort in einem Lesezeichen-URL)

Sie können den folgenden URL nutzen, um sich direkt bei Ihrem Uptrends Account anzumelden:  
`https://app.uptrends.com/Account/DirectLogin?username=<username>&password=<password>`

Optional können Sie den URL eines Dashboards angeben, um **direkt zu dem Dashboard** nach der Anmeldung zu gelangen. Um zum Beispiel das Operations-Dashboard (den Nachfolger des Uptrends v3 Cockpits) zu laden, verwenden Sie bitte:  
`https://app.uptrends.com/Account/DirectLogin?username=<username>&password=<password>&returnurl=/Report/Operations`

## Kodierung von Sonderzeichen

Wenn der Benutzername oder das Passwort Sonderzeichen oder diakritische Zeichen enthalten, müssen diese in der URL kodiert werden.

Der Benutzername “Maël” muss in `Ma%C3%ABl` geändert werden, während das Passwort “123@GZ!98” in `123%40GZ%2198` geändert werden muss. Mit dem Beispiel oben würde die URL folgendermaßen mit dem Benutzernamen und Passwort aussehen:  
`https://app.uptrends.com/Account/DirectLogin?username=Ma%C3%ABl&password=123%40GZ%2198`

{{< callout >}}
**Hinweis:** Mehr über Zeichen-Kodierung und eine vollständige Liste der sind auf der Website von w3schools.com unter [HTML URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.asp) zu finden.
{{< /callout >}}
