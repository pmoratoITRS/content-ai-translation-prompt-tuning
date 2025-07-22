{
  "hero": {
    "title": "Accessing the Uptrends API using cURL"
  },
  "title": "Accessing the Uptrends API using cURL",
  "summary": "Using cURL to access the Uptrends API.",
  "url": "/support/kb/api/accessing-the-uptrends-api-using-curl",
  "translationKey": "https://www.uptrends.com/support/kb/api/accessing-the-uptrends-api-using-curl"
}

The following example accesses the Uptrends API and fetches the list of Uptrends monitors in your account. Keep in mind that in order to access our API, you'll need to [register for a set of API-specific credentials]({{< ref path="/support/kb/api/authentication-v4" lang="en" >}}), and make sure to use those rather than your regular Uptrends credentials.

`curl https://api.uptrends.com/v4/Monitor -k --user 9d9f60d1a54ceb34afaf47b3abebde47:1234xxx --header "Accept: application/json"`

{{< callout >}}
**Tip**: don't have cURL? Download it at: <https://curl.haxx.se/download.html>.
{{< /callout >}}
