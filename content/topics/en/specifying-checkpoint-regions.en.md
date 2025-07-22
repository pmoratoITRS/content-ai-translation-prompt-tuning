{
  "hero": {
    "title": "Specifying checkpoint regions"
  },
  "title": "Specifying checkpoint regions",
  "summary": "How to specify your checkpoints when your account limits you to entire regions.",
  "url": "/support/kb/api/specifying-checkpoint-regions",
  "translationKey": "https://www.uptrends.com/support/kb/api/specifying-checkpoint-regions"
}

Accounts that can only select entire checkpoint regions to run their monitors on (as opposed to an unrestricted selection of individual checkpoints), need to specify a special value when they're creating or updating monitors in the API.

In the Checkpoints field (which normally holds a comma-separated list of checkpoint Ids), specify one of these phrases:

-   Europe only: `` `{"Regions":[1004]}` ``
-   North America only: `` `{"Regions":[1005]}` ``
-   Both: leave the field empty, or specify `` `{"Regions":[1004,1005]}` ``
