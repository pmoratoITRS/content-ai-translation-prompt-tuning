{
  "hero": {
    "title": "Pricing for concurrent monitoring"
  },
  "title": "Pricing for concurrent monitoring",
  "summary": "In this article you find the formulas used to calculate how many credits the concurrent monitoring will cost and some examples.",
  "url": "/support/kb/synthetic-monitoring/concurrent-monitoring/pricing-calculation-examples",
  "translationKey": "https://www.uptrends.com/support/kb/concurrent-monitoring/pricing-calculation-examples"
}


## Pricing for Full Page Check (FPC) and transaction monitors

The price is calculated following the credit system, where different types of monitors have different base prices, expressed in credits. So in general the calculation is:

Price = the monitor base price x the number of checkpoints included in the check

### Comparison example

In the following table you find an example of how the pricing works, compared between concurrent and standard monitoring.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Concurrent monitoring</th><th>Standard monitoring</th></tr></thead><tbody><tr class="odd"><td>Transaction (cost of 4 credits), user-defined to run on 3 checkpoints<br />
4 credits x 3 = <strong>12 credits</strong></td><td>Transaction (cost of 4 credits)<br />
4 credits x 1 = <strong>4 credits</strong></td></tr></tbody></table>

## Pricing for basic monitors and Multi-step API (MSA) monitors 

For these monitors tiered pricing with a scaling factor applies, therefore the price is calculated differently than the price for Full Page Checks and transaction monitors. The basic monitors include Ping, Http(s), SSL certificate, etc. monitors. Also, keep in mind that for an MSA monitor the pricing depends on the number of steps. See the price formulas below.

**Basic monitor**

Price = the monitor base price x the scaling factor from the tiered pricing table below

**MSA monitor**

Price = the number of steps in the MSA monitor x the scaling factor from the tiered pricing table below

### Tiered pricing table

<table>
  <colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup>
  <thead><tr class="header"><th>Number of checkpoints</th><th>Scaling factor</th></tr></thead>
  <tbody>
    <tr><td>1 to 2</td><td>N/A (see note below table)</td></tr>
    <tr><td>3 to 4</td><td>2</td></tr>
    <tr><td>5 to 7</td><td>3</td></tr>
    <tr><td>8 to 10</td><td>4</td></tr>
    <tr><td>11 to 14</td><td>5</td></tr>
    <tr><td>15 to 18</td><td>6</td></tr>
    <tr><td>19 to 22</td><td>7</td></tr>
    <tr><td>23 to 26</td><td>8</td></tr>
    <tr><td>27 to 30</td><td>9</td></tr>
    <tr><td>31 to 35</td><td>10</td></tr>
    <tr><td>36 to 40</td><td>11</td></tr>
    <tr><td>41 to 45</td><td>12</td></tr>
    <tr><td>46 to 50</td><td>13</td></tr>
  </tbody>
</table>

{{< callout >}} **Note**: You have to choose a minimum of three (high availability) or five (out of all) checkpoints to use concurrent monitoring. For standard monitoring you also have to choose a minimum of three checkpoints, but only one will be used at a time (and included in the price calculation). {{< /callout >}}
### Comparison examples

In the following tables you find examples of how the pricing works, compared between concurrent and standard monitoring and also for different levels in tiered pricing.

**Basic monitor**

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup>
  <thead><tr class="header"><th>Concurrent monitoring (tiered pricing)</th><th>Standard monitoring</th></tr></thead>
  <tbody>
    <tr><td>HTTPS monitor (base price of 1), user-defined to run on 4 checkpoints<br />
1 credit x 2 (scaling factor) = <strong>2 credits</strong></td><td>HTTPS monitor (base price of 1)<br />
1 credit x 1 = <strong>1 credit</strong></td></tr>
    <tr><td>HTTPS monitor (base price of 1), user-defined to run on 10 checkpoints<br />
1 credit x 4 (scaling factor) = <strong>4 credits</strong></td><td>HTTPS monitor (base price of 1)<br />
1 credit x 1 = <strong>1 credit</strong></td></tr>
  </tbody>
</table>

**Multi-step API monitor**

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup>
  <thead><tr class="header"><th>Concurrent monitoring (tiered pricing)</th><th>Standard monitoring</th></tr></thead>
  <tbody>
<tr><td>MSA monitor with 10 steps, user-defined to run on 4 checkpoints<br />
10 credits (number of steps) x 2 (scaling factor) = <strong>20 credits</strong></td>
<td>MSA monitor with 10 steps (base price of 10)<br />
10 credits (number of steps) x 1 = <strong>10 credits</strong></td></tr>
   <tr><td>MSA monitor with 10 steps, user-defined to run on 10 checkpoints<br />
10 credits (number of steps) x 4 (scaling factor) = <strong>40 credits</strong></td>
<td>MSA monitor with 10 steps (base price of 10)<br />
10 credits (number of steps) x 1 = <strong>10 credits</strong></td></tr> 
  </tbody>
</table>

{{< callout >}} **Note**: In general you should keep in mind that a monitor type with a high base price (credits per monitor) will lead to high credit use, when including many checkpoints. {{< /callout >}}
