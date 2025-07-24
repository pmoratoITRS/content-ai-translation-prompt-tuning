{
  "hero": {
    "title": "Specifying checkpoint regions"
  },
  "title": "Specifying checkpoint regions",
  "summary": "How to specify your checkpoints when your account limits you to entire regions.",
  "url": "[URL_BASE_TOPICS]api/specifying-checkpoint-regions",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Accounts that can only select entire checkpoint regions to run their monitors on (as opposed to an unrestricted selection of individual checkpoints), need to specify a special value when they're creating or updating monitors in the API.

In the Checkpoints field (which normally holds a comma-separated list of checkpoint Ids), specify one of these phrases:

-   Europe only: `[INLINE_CODE_1]{"Regions":[1004]}[INLINE_CODE_2][INLINE_CODE_3][INLINE_CODE_4]{"Regions":[1005]}[INLINE_CODE_5][INLINE_CODE_6][INLINE_CODE_7]{"Regions":[1004,1005]}[INLINE_CODE_8]`
