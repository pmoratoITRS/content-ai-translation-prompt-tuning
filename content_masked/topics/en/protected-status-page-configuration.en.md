{
  "hero": {
    "title": "Setting up protected status pages"
  },
  "title": "Setting up protected status pages",
  "summary": "This article describes how you create a new protected status page and setting up operators.",
  "url": "[URL_BASE_TOPICS]dashboards-and-reporting/status-pages/protected-status-page-configuration",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

To create a protected status page you need to set up the page and take care of assigning the necessary permissions to the operator(s) that should be able to view the page. The permissions of the new operator need to be restricted, such that they can access only the protected status page (and no other things, like monitors). Note that you need administrator rights to manage operators and permissions.

## Creating a protected status page


1. Create a regular public status page using the instructions in [Setting up public status pages]([LINK_URL_1]). 
2. Since you're creating a protected status page, make sure that the **Publish** checkbox on the [SHORTCODE_1] General [SHORTCODE_2] tab is unchecked. If you publish a status page, it will become available to the general public. 
3. Optionally add a logo, change the color scheme and title and footer text. This is described in [Customizing your public status page]([LINK_URL_2]).
4. Save the status page.
5. In the public status pages overview notice the *Preview* link for the new status page. This link contains the URL that authorized users have to use to access the status page.

## Creating operators with access to the protected status page

You have to create at least one operator and set the permissions such that the operator can access only the protected status page. Note that you need to be an administrator to add operators and manage permissions. In addition, you will need some help from Uptrends to complete the process:

1. Add a [new operator]([LINK_URL_3]). We strongly recommend that you do not share the new login credentials with third parties until the next steps have been completed. 
2. Remove the *Basic operator* [permission]([LINK_URL_4]) from the new operator by opening the operator settings. On the [SHORTCODE_3] Permissions [SHORTCODE_4] tab in the **System-wide permissions** section click the [SHORTCODE_5] Turn off [SHORTCODE_6] button next to the *Basic operator* permission.
3. Confirm your choice by clicking [SHORTCODE_7] Turn off [SHORTCODE_8] in the popup dialog.
4. Click [SHORTCODE_9] Save [SHORTCODE_10] at the bottom of the operator screen. 
5. Grant the operator access to the protected status page. This step is done by Uptrends Support. Please [file a support request]([LINK_URL_5]) asking for a protected status page. In your request, include the name of the protected status page and the name of the operator(s) that need to get access. The Support team will grant the operator(s) access to the new status page and update you as soon as the request has been processed.
