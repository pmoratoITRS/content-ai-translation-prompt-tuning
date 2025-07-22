{
  "hero": {
    "title": "Authentication (version 4)"
  },
  "title": "Authentication (version 4)",
  "summary": "How to register your API account and how authentication works",
  "url": "/support/kb/api/authentication-v4",
  "translationKey": "https://www.uptrends.com/support/kb/api/authentication-v4"
}

Each API method requires authentication through an API account, so you'll first need to create one. This API account is based on your Uptrends account, but is not the same. The advantage of having separate accounts is that you use the API credentials within e.g. scripts and don't have to disclose your Uptrends account credentials.

## Managing API accounts in the operator settings

API accounts are managed directly in the operator that the accounts are related to. Check out [Operator API management]({{< ref path="support/kb/account/users/operators/operator-API-management" lang="en" >}}) for instructions on how to add or delete API accounts. For most cases this is the easiest way to register an API account and keep track of which operator has which accounts, because there can be multiple accounts registered with one operator.

## Registering an API account using API calls {id="register-API-account"}

There is also an option to create the API account using Uptrends' API. This is an older, less comfortable way of doing it. However, it still works and an account that is created this way will show up in the {{< AppElement type="tab" >}} API management {{< /AppElement >}} tab of the operator as well.

The **POST** method of the **/Register** endpoint lets you create a new API account. In the steps described, you'll use the Swagger environment to access the API directly. The API account you're about to create will not expire, so you will only need to do this once.  

1.  Go to the [Swagger page](https://api.uptrends.com/v4/swagger/), and locate and expand the [POST /Register](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Register/Register_Post%20) method.

2.  Click the *Try it out* button to start creating an API account.

3.  Click on the *Execute* button.

4.  Your browser will now ask for your Uptrends operator login credentials. Fill in the e-mail address and password that you normally use to access Uptrends and click OK.

5.  After the login credentials of your Uptrends account were verified, the Response body contains values for UserName and Password.  

```json                  
{
  "UserName": "usernamehere",
  "Password": "passwordhere",
  "AccountId": "123456",
  "OperatorName": "Your name",
  "status": "OK"
}
```              
    
These are the credentials of your new API account.

6.  Click the *Download* button within the Response body to save these credentials and keep them in a safe place. Use them as authentication for all other API calls.

{{< callout >}}
**Note:** The API account will not expire. However, if you lose your credentials they cannot be recovered. You will have to create a new API account.
{{< /callout >}}

## Usage of your API account {id="usage-API-account"}

Now that you have an API account you can start using it. If you are using Swagger, you provide the credentials in a dialog. In software like cURL or Postman you provide them as headers and the necessary encoding is taken care of. If you are using your own scripts, you first have to encode your credentials, see the section [Basic authentication](#basic-authentication).

{{< callout >}}
**Note:** Remember that this API account is linked to your Uptrends operator account, so it will have the same privileges you have in your Uptrends account.
{{< /callout >}}

### Swagger environment

If you are executing API methods in the Swagger environment, a {{< AppElement type="menuitem" >}}Sign in{{< /AppElement >}} (referring to api.uptrends.com) window will pop up where you have to enter your API account Username and Password.

### Basic authentication

The account credentials always have to be encoded using the basic authentication scheme and provided to the API as particular header.

Software like Postman, cURL, etc. will take care of encoding the credentials and providing them correctly. If you are writing your own script you have to provide this header to the API call:

`Authorization: Basic {{encoded credentials}}`

The credentials have to be base64 encoded. To create the header, follow these steps:

1.  Define a string with the syntax `username:password`, replacing the `username` and `password` with your credentials. Do not add any spaces.

2.  The string `username:password` has to be base64 encoded. The encoding functionality may be included in your software or scripting language or you use a tool like https://www.base64encode.org.

3.  Once you have the encoded string, create and use a header `Authorization: Basic {{encoded credentials}}`, where the `encoded credentials` is the base64 encoded string from the step before.
