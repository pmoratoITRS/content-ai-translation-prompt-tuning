{
  "hero": {
    "title": "Operator API account management"
  },
  "title": "Operator API account management",
  "summary": "Adding or removing registered API users to an operator",
  "url": "[URL_BASE_TOPICS]account/users/operators/operator-API-management",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

If you want to use [Uptrends' API]([LINK_URL_1]) you need an API account (which is not the same as your Uptrends account). The credentials of the API account have to be entered using the *Basic authentication* scheme for execution of an API call. Check the information in [Usage of your API account]([LINK_URL_2]) on how to enter the credentials when making API calls.

The [SHORTCODE_3] API management [SHORTCODE_4] tab of an operator lets you manage all API accounts that are related to a specific operator.

[SHORTCODE_1] **Note**: You cannot retrieve passwords on the *API management* tab or elsewhere in your account. Make sure to take note of the passwords while creating a new API account. [SHORTCODE_2]

## Adding an API account 

To add a new API account to an operator:

1. Go to [SHORTCODE_5] Account setup > Operators, groups (and sub accounts) [SHORTCODE_6].
2. Click the [SHORTCODE_7] View all operators [SHORTCODE_8] button. 
3. In the list of operators click the one that you want to add an API account to.
4. Switch to the [SHORTCODE_9] API management [SHORTCODE_10] tab.
5. Click the [SHORTCODE_11] Add API user [SHORTCODE_12] button.
6. Follow the wizard and make sure to note down the password. The API account is added to the list of API users:

   ![screenshot API management tab of an operator]([LINK_URL_3])

7. Click the [SHORTCODE_13] Save [SHORTCODE_14] button at the bottom to save the changes to the operator.

On the [SHORTCODE_15] API management [SHORTCODE_16] tab of an operator you can see all API user accounts that are linked to this operator. You can also see the creation date and when the account was last used. These options may appear in the *Last used* column:

- **Unknown** — is shown when the API account was created before the functionality of "Last used" became available.
- **Not yet used** — means that the API account was created after introduction of the "Last used" feature, but the account hasn't been used.
- **Date/time** — the timestamp of the latest use of the API account will be shown if the account was created and used after introduction of the "Last used" feature.

Note that there is another (older) way of adding a API account by using the /Register method of Uptrends' API. This method is not recommended, as it is less handy in most situations. However, this will still work and the instructions can be found in [Register an API account]([LINK_URL_4]). An account that is added through the API will also appear on the [SHORTCODE_17] API management [SHORTCODE_18] tab of an operator. 

 ## Deleting an API account 

 To delete an API account from an operator:

1. Go to [SHORTCODE_19] Account setup > Operators, groups (and sub accounts) [SHORTCODE_20].
2. Click the [SHORTCODE_21] View all operators [SHORTCODE_22] button. 
3. In the list of operators click the one that you want to remove an API account from.
4. Switch to the [SHORTCODE_23] API management [SHORTCODE_24] tab.
5. In the row of the account that you want to remove, click the [SHORTCODE_25] Delete API user [SHORTCODE_26] button.
6. Click the [SHORTCODE_27] Save [SHORTCODE_28] button at the bottom.
