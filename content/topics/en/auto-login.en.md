{
  "hero": {
    "title": "Auto-login"
  },
  "title": "Auto-login",
  "summary": "Learn how to login directly with an auto-login. Jump straight to the dashboard you want to watch.",
  "url": "/support/kb/basics/auto-login",
  "translationKey": "https://www.uptrends.com/support/kb/basics/auto-login"
}

## Direct login/auto-login (with username/password in a bookmarked URL)

You can use the following URL to log in directly into your Uptrends account:  
`https://app.uptrends.com/Account/DirectLogin?username=<username>&password=<password>`

Optionally, you can specify the URL of a dashboard to **jump straight to that dashboard** after logging in. For example, to load the Operations Dashboard, please use:  
`https://app.uptrends.com/Account/DirectLogin?username=<username>&password=<password>&returnurl=/Report/Operations`

## Special character encoding

If your username or password includes any special characters, you will need to encode them in the URL.

For example, the username, “Maël” needs to be changed to `Ma%C3%ABl` while the password, “123@GZ!98” needs to be changed to `123%40GZ%2198`. Using the first example above, the URL would look like the following with this username and password.

`https://app.uptrends.com/Account/DirectLogin?username=Ma%C3%ABl&password=123%40GZ%2198`

{{< callout >}}
**Note:** You can learn more about character encoding and get a complete list of characters on the w3schools' [HTML URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.asp).
{{< /callout >}}
