{
  "hero": {
    "title": "Automatic variables"
  },
  "title": "Automatic variables",
  "summary": "A list of automatic variables for use in transaction and multi-step API monitors",
  "url": "/support/kb/synthetic-monitoring/transactions/automatic-variables",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/automatic-variables"
}

Uptrends' [Transaction]({{< ref path="support/kb/synthetic-monitoring/transactions" lang="en" >}}) and [Multi-Step API]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="en" >}}) monitor types allow you to traverse a flow consisting of several steps, either across a page on the web or by directly interacting with an API. In some cases, you may have a need to submit variable data. For example, a certain form in one of your transactions requires a timestamp, or you may need to generate a unique identifier to be used in one of the API requests. Uptrends supports a number of **automatic variables** that are created for you. Most of them are actually functions that generate a value you can use in your HTTP requests, fill out in textfields, or add to selectors in your transaction monitors.

## Generic automatic variables

The following automatic variables are available for both the **Transaction** and **Multi-Step API** monitor types:

### Date and time

{{< Code/Symbol type="variable" >}}{{@DateTime(format,offset)}}{{< /Code/Symbol >}} : This variable generates dynamic date/time values, according to the format you specify and with an optional offset. The date/time (without an offset) is always the current time expressed in the UTC (coordinated universal time) standard. 

To format the date/time to your needs, set the `format` parameter to:
  
- a value supported by .NET date formatting, e.g. `dd/MM/yyyy` or `MM/dd/yyyy`
- `Iso`, for ISO 8601 format
- `Unix`, for Unix epoch time

The optional `offset` parameter can be used to recalculate the date/time based on a given difference (in seconds) or a date/time function. If you omit the offset parameter, no offset is applied. To recalculate the date/time, use the following options: 

- Set the offset parameter to a positive or negative number of seconds. The specified number of seconds is added or subtracted from the current date/time value. A typical use case is to calculate the date/time in a different timezone or to move to a different day before or after the current date/time.

  See the table below for some examples.

- Use a date/time function to calculate the last or first day of the current, previous or next month, relative to the given date/time value. The possible values for the offset are:
  - `LastDayOfMonth`
  - `FirstDayOfMonth`
  - `LastDayOfPreviousMonth`
  - `FirstDayOfPreviousMonth`
  - `LastDayOfNextMonth`
  - `FirstDayOfNextMonth`

The table below shows some examples, based on the idea that it is 24 February, 2018 22:30 UTC right now.
| Expression                                  | Value                        | Description                                   |
|---------------------------------------------|------------------------------|-----------------------------------------------|
| `{{@DateTime(dd-MM-yyyy HH:mm)}}`           | 24-02-2018 22:30             | Now, in dd-MM-yyyy HH:mm format               |
| `{{@DateTime(dd-MM-yyyy HH:mm,-18000)}}`    | 24-02-2018 17:30             | Now, in Eastern Standard Time (UTC-5)         |
| `{{@DateTime(ISO)}}`                        | 2018-02-24T22:30:00.0000000Z | Now, in ISO 8601 format                       |
| `{{@DateTime(UNIX)}}`                       | 1519511400                   | Now, in Unix epoch time                       |
| `{{@DateTime(MM/dd/yyyy,-86400)}}`          | 02/23/2018                   | Yesterday, in MM/dd/yyyy format               |
| `{{@DateTime(MM/dd/yyyy,86400)}}`           | 02/25/2018                   | Tomorrow, in MM/dd/yyyy format                |
| `{{@DateTime(MM/dd/yyyy,FirstDayOfMonth)}}` | 02/01/2018                   | First day of this month, in MM/dd/yyyy format |
| `{{@DateTime(MM/dd/yyyy,LastDayOfMonth)}}`  | 02/28/2018                   | Last day of this month, in MM/dd/yyyy format  |

### Random unique identifier

{{< Code/Symbol type="variable" >}}{{@RandomGuid}}{{< /Code/Symbol >}} : This variable produces a random value in the form `AB0AD14D-9611-41A8-9C25-7D94B895CFF1`. You can use this variable if you need to include a random value in your URL, POST data or HTTP header. If you use the {{< Code/Symbol type="variable" >}}@RandomGuid{{< /Code/Symbol >}} variable in multiple steps, each step will get a different random value. Each time the monitor is executed, you will get completely new random values.
### Recurring random unique identifier
{{< Code/Symbol type="variable" >}}{{@UniqueGuid}}{{< /Code/Symbol >}} : This unique, randomly generated value can be reused multiple times during the entire transaction. Unlike the {{< Code/Symbol type="variable" >}}@RandomGuid{{< /Code/Symbol >}} mentioned above, which creates a new value every time, you can use this variable if you need to include a recurring value in your URL, POST data or HTTP header.
For example, this could be useful when creating a script for a sign-up process, where you need the generated email address and the confirmed email address to be exactly the same.
### Random integer

{{< Code/Symbol type="variable" >}}{{@RandomInt(min,max)}}{{< /Code/Symbol >}} : This variable produces a random integer number, between the minimum and maximum values you specify (min and max included). For example, if you specify `{{@RandomInt(0,100)}}`, this variable produces a number in the range 0..100.
### Random uppercase letters

{{< Code/Symbol type="variable" >}}{{@RandomChar(length)}}{{< /Code/Symbol >}} : This automatic variable allows you to generate a random series of alphabetical characters with a specified length. All characters will be in uppercase. For example, `{{@RandomChar(5)}}` returns a random value in the form `GPLMQ`.
### Random US Medicare Beneficiary Identifiers (MBI)
{{< Code/Symbol type="variable" >}}{{@RandomUSMedicare}}{{< /Code/Symbol >}} : This automatic variable allows you to generate US Medicare Beneficiary Identifiers. The MBI is a series of 11 alphanumeric characters. For example, `1EG4TE5MK73`. Please note, this code will be generated without dashes. The MBI code can be used by companies in the US healthcare industry.

## Transaction-specific (legacy) variables

The following set of automatic variables are older, but may still be used. These variables are available only for **Transaction** monitors.

### Timestamps

{{< Code/Symbol type="variable" >}}{timespan 0}{now dd-MM-yyyy}{{< /Code/Symbol >}} : To **generate and set a timestamp** (current date) in a text field on your page.

{{< Code/Symbol type="variable" >}}{timespan 1:0:0:0}{now dd-MM-yyyy}{{< /Code/Symbol >}} : To **offset the day by 1** (tomorrow).

{{< Code/Symbol type="variable" >}}{timespan 0:1:0:0}{now dd-MM-yyyy}{{< /Code/Symbol >}} : Same as above, except **offset by 1 hour**.

{{< Code/Symbol type="variable" >}}{timespan 0:0:1:0}{now dd-MM-yyyy}{{< /Code/Symbol >}} and {{< Code/Symbol type="variable" >}}{timespan 0:0:0:1}{now dd-MM-yyyy}{{< /Code/Symbol >}} : Offset the current time by one minute or second, respectively.

### Random value from an array

{{< Code/Symbol type="variable" >}}{random 1 2 3 4 5}{{< /Code/Symbol >}} : Set a random variable from an array. This function sets a random value from one to five.

{{< Code/Symbol type="variable" >}}{random apple banana orange}{{< /Code/Symbol >}} : This function sets a random string from the selected array: either `apple`, `banana`, or `orange` will be set.

## Multi-Step API-specific variables

The following variables and information applies only to the **Multi-step API** monitor type.

### Server identification (ID)

{{< Code/Symbol type="variable" >}}{{@ServerId}}{{< /Code/Symbol >}} : During execution of a Multi-step API monitor, this variable outputs a numeric value that identifies the Uptrends checkpoint location that is executing that check. For example, if the check is being executed on Uptrends' checkpoint in Sydney, Australia, the variable will output `30`. The list of checkpoint servers and their corresponding **Server IDs** is available through the [Uptrends API]({{< ref path="support/kb/api" lang="en" >}}) at the [Checkpoint endpoint](https://api.uptrends.com/v4/Checkpoint). 

### Redirect URL

{{< Code/Symbol type="variable" >}}{{@RedirectUrl}}{{< /Code/Symbol >}} : In case any of the steps in your monitor are expected to return a redirect code, and you want to capture and test that redirect response, rather than automatically following it, this automatic variable will contain the URL the redirect is referring to. This will only happen if you choose not to auto-follow redirects, but set up an assertion that checks for the appropriate redirect code. This procedure is explained in more detail here: [How to handle redirects in multi-step monitoring]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-redirects" lang="en" >}}).

### Random float

{{< Code/Symbol type="variable" >}}{{@RandomFloat(min,max)}}{{< /Code/Symbol >}} : Use this function to generate a floating point number within the range (min/max) entered. The precision (number of digits after the decimal point) of the generated float is derived from the highest precision of the `min` and `max` values used. 

For example, `{{@RandomFloat(-1.2,3.00000)}}` will generate a random float between -1.2 and 3.0 with a precision of 5, like 2.12345.

## Using an automatically generated value multiple times

Some of these variable functions (in particular the ones producing random and date/time values) are re-evaluated each time you use them, and will generate a new value every time. If you want to generate a particular value and use it multiple times throughout your multi-step scenario, you can define a predefined variable (as discussed in the [Multi-step monitoring variables]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="en" >}}) article) and use an automatic variable as its value.

### Examples of predefined variables using automatic variables

| Name          | Value                           | Usage                                                                                                                                                                                                                           |
|---------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SearchDate`  | `{{@DateTime(dd-MM-yyyy)}}`     | A date value to be used as input for a search query.                                                                                                                                                                            |
| `UniqueEmail` | `{{@RandomGuid}}@mycompany.com` | A random guid value combined with fixed text to generate an e-mail address that is different every time.                                                                                                                        |
| `OrderAmount` | `{{@RandomInt(1, 10)}}`         | A random number between 1 and 10 to be used as the number of products to order. In a subsequent call, you could use this variable again to check the contents of a shopping cart and see if it does indeed contain this amount. |
