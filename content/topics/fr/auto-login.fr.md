{
  "hero": {
    "title": "Connexion automatique"
  },
  "title": "Connexion automatique",
  "summary": "Découvrez comment activer la connexion automatique à votre compte Uptrends et comment accéder directement au tableau de bord.",
  "url": "/support/kb/demarrage/connexion-automatique",
  "translationKey": "https://www.uptrends.com/support/kb/basics/auto-login"
}

## Connexion directe/automatique (avec nom d'utilisateur / mot de passe dans un marque-page URL)

Vous pouvez utiliser l'URL suivant pour vous connecter directement à votre compte Uptrends :  
`https://app.uptrends.com/Account/DirectLogin?username=<username>&password=<password>`

En plus, vous pouvez spécifier l'URL d'un tableau de bord afin **d'aller directement à ce tableau de bord** après la connexion. Par exemple, pour aller au tableau de bord "Opérations" (qui est le successeur du cockpit d'Uptrends), utilisez :  
`https://app.uptrends.com/Account/DirectLogin?username=<username>&password=<password>&returnurl=/Report/Operations`

## Special character encoding

Si votre nom d'utilisateur ou mot de passe inclut des caractères spéciaux, vous devrez les encoder dans l'URL.

Par exemple, le nom d'utilisateur "Maël" doit être changé en `Ma%C3%ABl` et le mot de passe “123@GZ!98” doit être changé en `123%40GZ%2198`. En utilisant le premier exemple ci-dessus, l'URL devrait ressembler à cela en utilisant le nom d'utilisateur et le mot de passe : 

`https://app.uptrends.com/Account/DirectLogin?username=Ma%C3%ABl &password=123%40GZ%2198`

{{< callout >}}
**Remarque :** Vous pouvez en apprendre plus sur l'encodage de caractères et obtenir une liste complètes des caractères sur le w3schools' [HTML URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.asp).
{{< /callout >}}
