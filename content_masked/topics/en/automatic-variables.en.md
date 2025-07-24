{
  "hero": {
    "title": "Automatic variables"
  },
  "title": "Automatic variables",
  "summary": "A list of automatic variables for use in transaction and multi-step API monitors",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/automatic-variables",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends' [Transaction]([LINK_URL_1]) and [Multi-Step API]([LINK_URL_2]) monitor types allow you to traverse a flow consisting of several steps, either across a page on the web or by directly interacting with an API. In some cases, you may have a need to submit variable data. For example, a certain form in one of your transactions requires a timestamp, or you may need to generate a unique identifier to be used in one of the API requests. Uptrends supports a number of **automatic variables** that are created for you. Most of them are actually functions that generate a value you can use in your HTTP requests, fill out in textfields, or add to selectors in your transaction monitors.

## Generic automatic variables

The following automatic variables are available for both the **Transaction** and **Multi-Step API** monitor types:

### Date and time

[SHORTCODE_1][SYSTEM_VAR_1][SHORTCODE_2] : This variable generates dynamic date/time values, according to the format you specify and with an optional offset. The date/time (without an offset) is always the current time expressed in the UTC (coordinated universal time) standard. 

To format the date/time to your needs, set the [INLINE_CODE_1] parameter to:
  
- a value supported by .NET date formatting, e.g. [INLINE_CODE_2] or [INLINE_CODE_3]
- [INLINE_CODE_4], for ISO 8601 format
- [INLINE_CODE_5], for Unix epoch time

The optional [INLINE_CODE_6] parameter can be used to recalculate the date/time based on a given difference (in seconds) or a date/time function. If you omit the offset parameter, no offset is applied. To recalculate the date/time, use the following options: 

- Set the offset parameter to a positive or negative number of seconds. The specified number of seconds is added or subtracted from the current date/time value. A typical use case is to calculate the date/time in a different timezone or to move to a different day before or after the current date/time.

  See the table below for some examples.

- Use a date/time function to calculate the last or first day of the current, previous or next month, relative to the given date/time value. The possible values for the offset are:
  - [INLINE_CODE_7]
  - [INLINE_CODE_8]
  - [INLINE_CODE_9]
  - [INLINE_CODE_10]
  - [INLINE_CODE_11]
  - [INLINE_CODE_12]

The table below shows some examples, based on the idea that it is 24 February, 2018 22:30 UTC right now.
| Expression                                  | Value                        | Description                                   |
|---------------------------------------------|------------------------------|-----------------------------------------------|
| [INLINE_CODE_13]           | 24-02-2018 22:30             | Now, in dd-MM-yyyy HH:mm format               |
| [INLINE_CODE_14]    | 24-02-2018 17:30             | Now, in Eastern Standard Time (UTC-5)         |
| [INLINE_CODE_15]                        | 2018-02-24T22:30:00.0000000Z | Now, in ISO 8601 format                       |
| [INLINE_CODE_16]                       | 1519511400                   | Now, in Unix epoch time                       |
| [INLINE_CODE_17]          | 02/23/2018                   | Yesterday, in MM/dd/yyyy format               |
| [INLINE_CODE_18]           | 02/25/2018                   | Tomorrow, in MM/dd/yyyy format                |
| [INLINE_CODE_19] | 02/01/2018                   | First day of this month, in MM/dd/yyyy format |
| [INLINE_CODE_20]  | 02/28/2018                   | Last day of this month, in MM/dd/yyyy format  |

### Random unique identifier

[SHORTCODE_3][SYSTEM_VAR_10][SHORTCODE_4] : This variable produces a random value in the form [INLINE_CODE_21]. You can use this variable if you need to include a random value in your URL, POST data or HTTP header. If you use the [SHORTCODE_5]@RandomGuid[SHORTCODE_6] variable in multiple steps, each step will get a different random value. Each time the monitor is executed, you will get completely new random values.
### Recurring random unique identifier
[SHORTCODE_7][SYSTEM_VAR_11][SHORTCODE_8] : This unique, randomly generated value can be reused multiple times during the entire transaction. Unlike the [SHORTCODE_9]@RandomGuid[SHORTCODE_10] mentioned above, which creates a new value every time, you can use this variable if you need to include a recurring value in your URL, POST data or HTTP header.
For example, this could be useful when creating a script for a sign-up process, where you need the generated email address and the confirmed email address to be exactly the same.
### Random integer

[SHORTCODE_11][SYSTEM_VAR_12][SHORTCODE_12] : This variable produces a random integer number, between the minimum and maximum values you specify (min and max included). For example, if you specify [INLINE_CODE_22], this variable produces a number in the range 0..100.
### Random uppercase letters

[SHORTCODE_13][SYSTEM_VAR_14][SHORTCODE_14] : This automatic variable allows you to generate a random series of alphabetical characters with a specified length. All characters will be in uppercase. For example, [INLINE_CODE_23] returns a random value in the form [INLINE_CODE_24].
### Random US Medicare Beneficiary Identifiers (MBI)
[SHORTCODE_15][SYSTEM_VAR_16][SHORTCODE_16] : This automatic variable allows you to generate US Medicare Beneficiary Identifiers. The MBI is a series of 11 alphanumeric characters. For example, [INLINE_CODE_25]. Please note, this code will be generated without dashes. The MBI code can be used by companies in the US healthcare industry.

## Transaction-specific (legacy) variables

The following set of automatic variables are older, but may still be used. These variables are available only for **Transaction** monitors.

### Timestamps

[SHORTCODE_17]{timespan 0}{now dd-MM-yyyy}[SHORTCODE_18] : To **generate and set a timestamp** (current date) in a text field on your page.

[SHORTCODE_19]{timespan 1:0:0:0}{now dd-MM-yyyy}[SHORTCODE_20] : To **offset the day by 1** (tomorrow).

[SHORTCODE_21]{timespan 0:1:0:0}{now dd-MM-yyyy}[SHORTCODE_22] : Same as above, except **offset by 1 hour**.

[SHORTCODE_23]{timespan 0:0:1:0}{now dd-MM-yyyy}[SHORTCODE_24] and [SHORTCODE_25]{timespan 0:0:0:1}{now dd-MM-yyyy}[SHORTCODE_26] : Offset the current time by one minute or second, respectively.

### Random value from an array

[SHORTCODE_27]{random 1 2 3 4 5}[SHORTCODE_28] : Set a random variable from an array. This function sets a random value from one to five.

[SHORTCODE_29]{random apple banana orange}[SHORTCODE_30] : This function sets a random string from the selected array: either [INLINE_CODE_26], [INLINE_CODE_27], or [INLINE_CODE_28] will be set.

## Multi-Step API-specific variables

The following variables and information applies only to the **Multi-step API** monitor type.

### Server identification (ID)

[SHORTCODE_31][SYSTEM_VAR_17][SHORTCODE_32] : During execution of a Multi-step API monitor, this variable outputs a numeric value that identifies the Uptrends checkpoint location that is executing that check. For example, if the check is being executed on Uptrends' checkpoint in Sydney, Australia, the variable will output [INLINE_CODE_29]. The list of checkpoint servers and their corresponding **Server IDs** is available through the [Uptrends API]([LINK_URL_3]) at the [Checkpoint endpoint]([LINK_URL_4]). 

### Redirect URL

[SHORTCODE_33][SYSTEM_VAR_18][SHORTCODE_34] : In case any of the steps in your monitor are expected to return a redirect code, and you want to capture and test that redirect response, rather than automatically following it, this automatic variable will contain the URL the redirect is referring to. This will only happen if you choose not to auto-follow redirects, but set up an assertion that checks for the appropriate redirect code. This procedure is explained in more detail here: [How to handle redirects in multi-step monitoring]([LINK_URL_5]).

### Random float

[SHORTCODE_35][SYSTEM_VAR_19][SHORTCODE_36] : Use this function to generate a floating point number within the range (min/max) entered. The precision (number of digits after the decimal point) of the generated float is derived from the highest precision of the [INLINE_CODE_30] and [INLINE_CODE_31] values used. 

For example, [INLINE_CODE_32] will generate a random float between -1.2 and 3.0 with a precision of 5, like 2.12345.

## Using an automatically generated value multiple times

Some of these variable functions (in particular the ones producing random and date/time values) are re-evaluated each time you use them, and will generate a new value every time. If you want to generate a particular value and use it multiple times throughout your multi-step scenario, you can define a predefined variable (as discussed in the [Multi-step monitoring variables]([LINK_URL_6]) article) and use an automatic variable as its value.

### Examples of predefined variables using automatic variables

| Name          | Value                           | Usage                                                                                                                                                                                                                           |
|---------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [INLINE_CODE_33]  | [INLINE_CODE_34]     | A date value to be used as input for a search query.                                                                                                                                                                            |
| [INLINE_CODE_35] | [INLINE_CODE_36] | A random guid value combined with fixed text to generate an e-mail address that is different every time.                                                                                                                        |
| [INLINE_CODE_37] | [INLINE_CODE_38]         | A random number between 1 and 10 to be used as the number of products to order. In a subsequent call, you could use this variable again to check the contents of a shopping cart and see if it does indeed contain this amount. |
