{
  "hero": {
    "title": "Controlestationregio's specificeren"
  },
  "title": "Controlestationregio's specificeren",
  "url": "/support/kb/api/controlestationregios-specificeren",
  "translationKey": "https://www.uptrends.com/support/kb/api/specifying-checkpoint-regions"
}

Accounts die alleen complete controlestationregio's kunnen selecteren om hun controleregels op te draaien (in tegenstelling tot een onbeperkt aanbod van individuele checkpoints), moeten een bijzondere waarde specificeren wanneer ze controleregels aanmaken of bijwerken via de API.

In het Checkpoints-veld (welke bestaat uit een lijst van controlestation ID's, gescheiden met een komma) specificeert u een van deze regels:

-   Alleen Europa: `` `{"Regions":[1004]}` ``
-   Alleen Noord-Amerika: `` `{"Regions":[1005]}` ``
-   Allebei: laat het veld leeg, of specificeer `` `{"Regions":[1004,1005]}` ``
