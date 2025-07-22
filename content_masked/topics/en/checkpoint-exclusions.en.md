{
  "hero": {
    "title": "Checkpoint exclusions"
  },
  "title": "Checkpoint exclusions",
  "summary": "Depending on the region from where you want to test or based on previous results you may want to explicitly exclude some checkpoints.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/checkpoint-exclusions",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

We operate a global network for over {{% Features/Variable variable="CheckpointCount" %}} checkpoints to make sure your website is available around the world 24/7. Although we do advise to use as many checkpoints as possible, that doesn't mean you need to. Introducing: **checkpoint exclusions!**

[SHORTCODE_1]
**Note:** You need to have either a Business or Enterprise account to use checkpoint exclusions. If you are experiencing a problem with a particular checkpoint, please let us know by opening a [support ticket]([LINK_URL_1]).
[SHORTCODE_2]

## Adding checkpoint exclusions

It is possible to keep an entire region of checkpoints (e.g. Canada) selected (with the benefit of **automatically getting new checkpoints as they are added** to that region) but have additional control over individual checkpoint locations that you want to skip.

You can add exclusions by clicking the link [SHORTCODE_5]add exclusions[SHORTCODE_6] in the text at the top of the [SHORTCODE_7]Checkpoints[SHORTCODE_8] tab. Any checkpoints you specify will be skipped when performing checks for your monitor, regardless of the selection you make.

![]([LINK_URL_2])

Checkpoint exclusions can come in handy in different occasions. A few examples:

-   If the Kelowna (Canada) checkpoint is giving you unexpected results, you can select Canada as a region, but exclude Kelowna.
-   It could be that your site is hosted from Berlin and you don't want overly close measurements. Rather than deselecting Germany and selecting all the checkpoints individually, you can simply add an exclusion.

[SHORTCODE_3]
**Note:** you can only exclude **specific checkpoints**. It's not possible to exclude whole countries from a selected continent.
[SHORTCODE_4]
