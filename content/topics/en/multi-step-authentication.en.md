{
  "hero": {
    "title": "Multi-step monitoring Authentication"
  },
  "title": "Multi-step monitoring Authentication",
  "summary": "Learn about the available options for authentication when using Multi-step API Monitoring.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-authentication",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-authentication"
}

Many APIs require that the caller specifies authentication information to verify their identity, and possibly the access rights of that caller. Authentication information can be passed along using HTTP headers (Basic/NTLM/Digest authentication), by exchanging access tokens (OAuth), by requiring the client to include a client certificate in the request, or a combination.   
  
This article discusses the HTTP header and token based authentication options in Uptrends. To set up client certificates, please [read the article on client certificate authentication](/support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-client-certificate-authentication). 

## Default authentication types

The Authentication section on the Request tab of a Multi-step API monitor offers several authentication types. They all use a username / password combination, but the way those credentials are processed and sent to the API is different for each type:

-   **Basic authentication**: the username and password are encoded in a simple Base64 encoded format and sent to the API server.
-   **NTLM (Windows) authentication**: when you specify this type, several requests are sent to the API to negotiate about the authentication that should be used, before the final HTTP request is sent with the appropriate authentication. This sequence of requests counts as one single step. If a Windows domain must be specified, include it in the username: YOURDOMAIN\\username.
-   **Digest authentication**: the username and password are hashed using the MD5 hashing algorithm, and the hash is sent to the server. 
-   **None**: choose *None* if you don't want to use authentication for your HTTP request.

### HTTP headers

The authentication types described above will all send multiple requests (though they all still count as one step). The first request will not include any credentials (hashed/encoded or otherwise). The client will then wait for the server to send a challenge, in the form of a 401 (Unauthorized) response code, and a **WWW-Authenticate** header that specifies the required method of authentication. Then, the client will resend the request, but this time including the correct Authorization header. 

When you use any of these authentication types, you typically won't need to specify any other authentication-specific HTTP headers: the appropriate Authorization header will be automatically generated. However, if the challenge is incomplete (because the server responds with a status code other than 401, or the WWW-Authenticate header is missing) the monitor will return an error and you may have to manually define the correct Authorization header. 

As an example, for Basic authentication, we'd expect the server to respond with a challenge after the first request, with a header `WWW-Authenticate: Basic` and a status code of 401: Unauthorized. If this doesn't happen, you may need to manually set up the Basic authentication header, so that the credentials are passed along even without a proper challenge. 

Per the [Basic authentication scheme](https://datatracker.ietf.org/doc/html/rfc7617), the credentials must be passed along in a Base64 encoded string of *username:password*. Base64 encoding string 'username:password' yields `dXNlcm5hbWU6cGFzc3dvcmQ=` which must then be passed along in an Authorization header. By adding header `Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=` to the MSA step, you can effectively circumvent the need for a challenge.


### Variable support

The username and password fields support variables. You can create predefined variables (for example: {{< Code/Symbol type="variable" >}}{{username}}{{< /Code/Symbol >}} and {{< Code/Symbol type="variable" >}}{{password}}{{< /Code/Symbol >}}) with the appropriate values and then use those variable names in the authentication fields. [More information about variables and predefined variables](/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables).

## Custom authentication (including OAuth)

When your API uses OAuth as its authentication protocol, you'll need a more elaborate setup. Depending on your API, you may need something quite specific to your situation. OAuth 2.0 in particular uses at least one separate request just for the authentication process. This request requests access to the API (using one of the default authentication types, by specifying login credentials in the URL, or even performing a web page login). Upon successful authentication, the OAuth access token is captured and stored in a variable, so it can be used in subsequent requests.

If you're not using OAuth but a different protocol, it may still operate in a similar way: you'll first have to specify login information that "proves" your identity to the API. The API server will then respond by giving you a login token that is valid for a certain amount of time. By capturing that token and storing it in a variable, you can execute a sequence of requests that use the login token to gain access.

### Setting up OAuth 2.0 authentication {id="setting-up-oauth-20"}

In the following example, we'll set up a simple form of OAuth 2.0 authentication. Our goal is to acquire an access token from the API, which we can then use in later requests.

To do this, we will first send a request containing the appropriate OAuth fields. In this case, we're requesting access based on an authorization code, a client id and a client secret. The client id and client secret are fixed values that we can define as predefined variables. In our simple setup, the authorization code will also be a fixed value, but in your setup it may be necessary to retrieve that authorization code first using a separate step.

First, we'll add those values to the predefined variables:

![Predefined variables](/img/content/scr-MSA-predefined-variables-auth.min.png)

With those variables defined, we can now set up a request to our API by including references to those variables, along with any other parameters the API expects. In the first step of our multi-step setup, add this URL:

`GET https://myapi.com/oauth/token?grant_type=authorization_code&code={{authorizationcode}}&client_id={{clientid}}&client_secret={{clientsecret}}`

We expect the API to return a data structure that contains the access token we need, but how will that data structure be formatted? To ensure we will get JSON-formatted data, let's tell the server we will only accept the application/json format by specifying that in an HTTP header:

![MSA accept header](/img/content/scr-msa-header-example.min.png)

With this header specified, we can now expect the response to look something like:

`{    "access_token":"SGV5ISBZb3UgZm91bmQgdGhpcyB0ZXh0IQ==",    "token_type":"Bearer",    "expires_in":86400  } `

All we need to do now, is capture the access\_token field in the JSON response. To do this, we'll create a new variable in the Response tab of our step:

-   The response should contain JSON, so choose {{< Code/Symbol type="source" >}}Response body as JSON{{< /Code/Symbol >}} as the source for our variable.
-   Since the **access\_token** attribute is located at the top level in our data structure, our JSON expression is simply {{< Code/Symbol type="property" >}}access\_token{{< /Code/Symbol >}}.
-   We'll choose {{< Code/Symbol type="variable" >}}accesstoken{{< /Code/Symbol >}} as our variable name. This is the name we'll refer to in later steps.

![Access token variable](/img/content/scr-msa-auth-variable.min.png)

Even though the main goal of this first step is to capture the access token, it already performs some monitoring as well: if the API returns an error at this point, or if the response does not contain an access token, this step will detect this and report an error.

Now that we have a valid access token, we can finally access the actual API method we want to check (say, for retrieving a list of products). Create a new step to define this API call. After specifying the method and URL for this new request, we're going to pass in the access token we've just captured. OAuth 2.0 based APIs expect an HTTP header called **Authorization**, with a value `Bearer {{accesstoken}}`

![Access token header](/img/content/scr-msa-auth-accesstoken-header.min.png)

We can repeat this for each additional step that requires the same access token.
