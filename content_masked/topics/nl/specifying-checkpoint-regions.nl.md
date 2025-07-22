{
  "hero": {
    "title": "Controlestationregio's specificeren"
  },
  "title": "Controlestationregio's specificeren",
  "url": "[URL_BASE_TOPICS]api/controlestationregios-specificeren",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Accounts die alleen complete controlestationregio's kunnen selecteren om hun controleregels op te draaien (in tegenstelling tot een onbeperkt aanbod van individuele checkpoints), moeten een bijzondere waarde specificeren wanneer ze controleregels aanmaken of bijwerken via de API.

In het Checkpoints-veld (welke bestaat uit een lijst van controlestation ID's, gescheiden met een komma) specificeert u een van deze regels:

-   Alleen Europa: `[INLINE_CODE_1]{"Regions":[1004]}[INLINE_CODE_2][INLINE_CODE_3][INLINE_CODE_4]{"Regions":[1005]}[INLINE_CODE_5][INLINE_CODE_6][INLINE_CODE_7]{"Regions":[1004,1005]}[INLINE_CODE_8]`
