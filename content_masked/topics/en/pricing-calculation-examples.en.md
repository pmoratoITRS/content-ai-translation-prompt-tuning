{
  "hero": {
    "title": "Pricing for concurrent monitoring"
  },
  "title": "Pricing for concurrent monitoring",
  "summary": "In this article you find the formulas used to calculate how many credits the concurrent monitoring will cost and some examples.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/concurrent-monitoring/pricing-calculation-examples",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Pricing for Full Page Check (FPC) and transaction monitors

The price is calculated following the credit system, where different types of monitors have different base prices, expressed in credits. So in general the calculation is:

Price = the monitor base price x the number of checkpoints included in the check

### Comparison example

In the following table you find an example of how the pricing works, compared between concurrent and standard monitoring.

[HTML_TAG_1][HTML_TAG_2][HTML_TAG_3][HTML_TAG_4][HTML_TAG_5][HTML_TAG_6][HTML_TAG_7][HTML_TAG_8]Concurrent monitoring[HTML_TAG_9][HTML_TAG_10]Standard monitoring[HTML_TAG_11][HTML_TAG_12][HTML_TAG_13][HTML_TAG_14][HTML_TAG_15][HTML_TAG_16]Transaction (cost of 4 credits), user-defined to run on 3 checkpoints[HTML_TAG_17]
4 credits x 3 = [HTML_TAG_18]12 credits[HTML_TAG_19][HTML_TAG_20][HTML_TAG_21]Transaction (cost of 4 credits)[HTML_TAG_22]
4 credits x 1 = [HTML_TAG_23]4 credits[HTML_TAG_24][HTML_TAG_25][HTML_TAG_26][HTML_TAG_27][HTML_TAG_28]

## Pricing for basic monitors and Multi-step API (MSA) monitors 

For these monitors tiered pricing with a scaling factor applies, therefore the price is calculated differently than the price for Full Page Checks and transaction monitors. The basic monitors include Ping, Http(s), SSL certificate, etc. monitors. Also, keep in mind that for an MSA monitor the pricing depends on the number of steps. See the price formulas below.

**Basic monitor**

Price = the monitor base price x the scaling factor from the tiered pricing table below

**MSA monitor**

Price = the number of steps in the MSA monitor x the scaling factor from the tiered pricing table below

### Tiered pricing table

[HTML_TAG_29]
  [HTML_TAG_30][HTML_TAG_31][HTML_TAG_32][HTML_TAG_33]
  [HTML_TAG_34][HTML_TAG_35][HTML_TAG_36]Number of checkpoints[HTML_TAG_37][HTML_TAG_38]Scaling factor[HTML_TAG_39][HTML_TAG_40][HTML_TAG_41]
  [HTML_TAG_42]
    [HTML_TAG_43][HTML_TAG_44]1 to 2[HTML_TAG_45][HTML_TAG_46]N/A (see note below table)[HTML_TAG_47][HTML_TAG_48]
    [HTML_TAG_49][HTML_TAG_50]3 to 4[HTML_TAG_51][HTML_TAG_52]2[HTML_TAG_53][HTML_TAG_54]
    [HTML_TAG_55][HTML_TAG_56]5 to 7[HTML_TAG_57][HTML_TAG_58]3[HTML_TAG_59][HTML_TAG_60]
    [HTML_TAG_61][HTML_TAG_62]8 to 10[HTML_TAG_63][HTML_TAG_64]4[HTML_TAG_65][HTML_TAG_66]
    [HTML_TAG_67][HTML_TAG_68]11 to 14[HTML_TAG_69][HTML_TAG_70]5[HTML_TAG_71][HTML_TAG_72]
    [HTML_TAG_73][HTML_TAG_74]15 to 18[HTML_TAG_75][HTML_TAG_76]6[HTML_TAG_77][HTML_TAG_78]
    [HTML_TAG_79][HTML_TAG_80]19 to 22[HTML_TAG_81][HTML_TAG_82]7[HTML_TAG_83][HTML_TAG_84]
    [HTML_TAG_85][HTML_TAG_86]23 to 26[HTML_TAG_87][HTML_TAG_88]8[HTML_TAG_89][HTML_TAG_90]
    [HTML_TAG_91][HTML_TAG_92]27 to 30[HTML_TAG_93][HTML_TAG_94]9[HTML_TAG_95][HTML_TAG_96]
    [HTML_TAG_97][HTML_TAG_98]31 to 35[HTML_TAG_99][HTML_TAG_100]10[HTML_TAG_101][HTML_TAG_102]
    [HTML_TAG_103][HTML_TAG_104]36 to 40[HTML_TAG_105][HTML_TAG_106]11[HTML_TAG_107][HTML_TAG_108]
    [HTML_TAG_109][HTML_TAG_110]41 to 45[HTML_TAG_111][HTML_TAG_112]12[HTML_TAG_113][HTML_TAG_114]
    [HTML_TAG_115][HTML_TAG_116]46 to 50[HTML_TAG_117][HTML_TAG_118]13[HTML_TAG_119][HTML_TAG_120]
  [HTML_TAG_121]
[HTML_TAG_122]

[SHORTCODE_1] **Note**: You have to choose a minimum of three (high availability) or five (out of all) checkpoints to use concurrent monitoring. For standard monitoring you also have to choose a minimum of three checkpoints, but only one will be used at a time (and included in the price calculation). [SHORTCODE_2]
### Comparison examples

In the following tables you find examples of how the pricing works, compared between concurrent and standard monitoring and also for different levels in tiered pricing.

**Basic monitor**

[HTML_TAG_123][HTML_TAG_124][HTML_TAG_125][HTML_TAG_126][HTML_TAG_127]
  [HTML_TAG_128][HTML_TAG_129][HTML_TAG_130]Concurrent monitoring (tiered pricing)[HTML_TAG_131][HTML_TAG_132]Standard monitoring[HTML_TAG_133][HTML_TAG_134][HTML_TAG_135]
  [HTML_TAG_136]
    [HTML_TAG_137][HTML_TAG_138]HTTPS monitor (base price of 1), user-defined to run on 4 checkpoints[HTML_TAG_139]
1 credit x 2 (scaling factor) = [HTML_TAG_140]2 credits[HTML_TAG_141][HTML_TAG_142][HTML_TAG_143]HTTPS monitor (base price of 1)[HTML_TAG_144]
1 credit x 1 = [HTML_TAG_145]1 credit[HTML_TAG_146][HTML_TAG_147][HTML_TAG_148]
    [HTML_TAG_149][HTML_TAG_150]HTTPS monitor (base price of 1), user-defined to run on 10 checkpoints[HTML_TAG_151]
1 credit x 4 (scaling factor) = [HTML_TAG_152]4 credits[HTML_TAG_153][HTML_TAG_154][HTML_TAG_155]HTTPS monitor (base price of 1)[HTML_TAG_156]
1 credit x 1 = [HTML_TAG_157]1 credit[HTML_TAG_158][HTML_TAG_159][HTML_TAG_160]
  [HTML_TAG_161]
[HTML_TAG_162]

**Multi-step API monitor**

[HTML_TAG_163][HTML_TAG_164][HTML_TAG_165][HTML_TAG_166][HTML_TAG_167]
  [HTML_TAG_168][HTML_TAG_169][HTML_TAG_170]Concurrent monitoring (tiered pricing)[HTML_TAG_171][HTML_TAG_172]Standard monitoring[HTML_TAG_173][HTML_TAG_174][HTML_TAG_175]
  [HTML_TAG_176]
[HTML_TAG_177][HTML_TAG_178]MSA monitor with 10 steps, user-defined to run on 4 checkpoints[HTML_TAG_179]
10 credits (number of steps) x 2 (scaling factor) = [HTML_TAG_180]20 credits[HTML_TAG_181][HTML_TAG_182]
[HTML_TAG_183]MSA monitor with 10 steps (base price of 10)[HTML_TAG_184]
10 credits (number of steps) x 1 = [HTML_TAG_185]10 credits[HTML_TAG_186][HTML_TAG_187][HTML_TAG_188]
   [HTML_TAG_189][HTML_TAG_190]MSA monitor with 10 steps, user-defined to run on 10 checkpoints[HTML_TAG_191]
10 credits (number of steps) x 4 (scaling factor) = [HTML_TAG_192]40 credits[HTML_TAG_193][HTML_TAG_194]
[HTML_TAG_195]MSA monitor with 10 steps (base price of 10)[HTML_TAG_196]
10 credits (number of steps) x 1 = [HTML_TAG_197]10 credits[HTML_TAG_198][HTML_TAG_199][HTML_TAG_200] 
  [HTML_TAG_201]
[HTML_TAG_202]

[SHORTCODE_3] **Note**: In general you should keep in mind that a monitor type with a high base price (credits per monitor) will lead to high credit use, when including many checkpoints. [SHORTCODE_4]
