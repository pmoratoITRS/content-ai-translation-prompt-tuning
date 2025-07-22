{
  "hero": {
    "title": "Operator API account management"
  },
  "title": "Operator API account management",
  "summary": "Adding or removing registered API users to an operator",
  "url": "/support/kb/account/users/operators/operator-API-management",
  "translationKey": "https://www.uptrends.com/support/kb/account/users/operators/operator-API-management"
}

If you want to use [Uptrends' API]({{< ref path="support/kb/api" lang="en" >}}) you need an API account (which is not the same as your Uptrends account). The credentials of the API account have to be entered using the *Basic authentication* scheme for execution of an API call. Check the information in [Usage of your API account]({{< ref path="support/kb/api/authentication-v4#usage-API-account" lang="en" >}}) on how to enter the credentials when making API calls.

The {{< AppElement type="tab" >}} API management {{< /AppElement >}} tab of an operator lets you manage all API accounts that are related to a specific operator.

{{< callout >}} **Note**: You cannot retrieve passwords on the *API management* tab or elsewhere in your account. Make sure to take note of the passwords while creating a new API account. {{< /callout >}}

## Adding an API account 

To add a new API account to an operator:

1. Go to {{< AppElement type="menuitem" >}} Account setup > Operators, groups (and sub accounts) {{< /AppElement >}}.
2. Click the {{< AppElement type="buttonPrimary" >}} View all operators {{< /AppElement >}} button. 
3. In the list of operators click the one that you want to add an API account to.
4. Switch to the {{< AppElement type="tab" >}} API management {{< /AppElement >}} tab.
5. Click the {{< AppElement type="buttonPrimary" >}} Add API user {{< /AppElement >}} button.
6. Follow the wizard and make sure to note down the password. The API account is added to the list of API users:

   ![screenshot API management tab of an operator](/img/content/scr_operator-API-management.min.png)

7. Click the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} button at the bottom to save the changes to the operator.

On the {{< AppElement type="tab" >}} API management {{< /AppElement >}} tab of an operator you can see all API user accounts that are linked to this operator. You can also see the creation date and when the account was last used. These options may appear in the *Last used* column:

- **Unknown** — is shown when the API account was created before the functionality of "Last used" became available.
- **Not yet used** — means that the API account was created after introduction of the "Last used" feature, but the account hasn't been used.
- **Date/time** — the timestamp of the latest use of the API account will be shown if the account was created and used after introduction of the "Last used" feature.

Note that there is another (older) way of adding a API account by using the /Register method of Uptrends' API. This method is not recommended, as it is less handy in most situations. However, this will still work and the instructions can be found in [Register an API account]({{< ref path="support/kb/api/authentication-v4#register-API-account" lang="en" >}}). An account that is added through the API will also appear on the {{< AppElement type="tab" >}} API management {{< /AppElement >}} tab of an operator. 

 ## Deleting an API account 

 To delete an API account from an operator:

1. Go to {{< AppElement type="menuitem" >}} Account setup > Operators, groups (and sub accounts) {{< /AppElement >}}.
2. Click the {{< AppElement type="buttonPrimary" >}} View all operators {{< /AppElement >}} button. 
3. In the list of operators click the one that you want to remove an API account from.
4. Switch to the {{< AppElement type="tab" >}} API management {{< /AppElement >}} tab.
5. In the row of the account that you want to remove, click the {{< AppElement type="deletebutton" >}} Delete API user {{< /AppElement >}} button.
6. Click the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} button at the bottom.
