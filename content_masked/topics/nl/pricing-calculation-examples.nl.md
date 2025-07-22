{
  "hero": {
    "title": "Prijzen voor Gelijktijdige monitoring"
  },
  "title": "Prijzen voor Gelijktijdige monitoring",
  "summary": "In dit artikel vindt u de formules die worden gebruikt om te berekenen hoeveel credits de gelijktijdige monitoring kost en enkele voorbeelden.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/gelijktijdige-monitoring/prijzen-berekening-voorbeelden",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Prijzen voor controleregeltypes Full page check en transactie

De prijs wordt berekend volgens het creditssysteem, waarbij verschillende soorten controleregels verschillende basisprijzen hebben, uitgedrukt in credits. Dus in het algemeen is de berekening:

Prijs = de basiscontroleregelprijs x het aantal controlestations dat in de controle is opgenomen

### Voorbeelden

In onderstaande tabel kunt u twee voorbeelden van de prijzen van Gelijktijdige monitoring versus Standaard monitoring vergelijken.

[HTML_TAG_1][HTML_TAG_2][HTML_TAG_3][HTML_TAG_4][HTML_TAG_5][HTML_TAG_6][HTML_TAG_7][HTML_TAG_8]Gelijktijdige monitoring[HTML_TAG_9][HTML_TAG_10]Standaard monitoring[HTML_TAG_11][HTML_TAG_12][HTML_TAG_13][HTML_TAG_14][HTML_TAG_15][HTML_TAG_16]Transactie (kosten van 4 credits), door de gebruiker gedefinieerd om op 3 controlestations uit te voeren[HTML_TAG_17]
4 credits x 3 = [HTML_TAG_18]12 credits[HTML_TAG_19][HTML_TAG_20][HTML_TAG_21]Transactie (kosten van 4 credits)[HTML_TAG_22]
4 credits x 1 = [HTML_TAG_23]4 credits[HTML_TAG_24][HTML_TAG_25][HTML_TAG_26][HTML_TAG_27][HTML_TAG_28]

## Prijzen voor basiscontroleregels en Multi-step API (MSA)-controleregels 

Voor deze controleregels geldt een gedifferentieerde prijsstelling met een schaalfactor, daarom wordt de prijs anders berekend dan voor de controleregeltypes Full page checks en transactie. De basiscontroleregels omvatten Ping, Http(s), SSL-certificaat enzovoort. Houd er ook rekening mee dat voor een MSA-controleregel de prijs afhankelijk is van het aantal stappen. Zie onderstaande prijsformules.

**Basiscontroleregel**

Prijs = de basiscontroleregelprijs x de schaalfactor uit onderstaande gedifferentieerde prijstabel

**MSA-controleregel**

Prijs = het aantal stappen in de MSA-controleregel x de schaalfactor uit onderstaande gedifferentieerde prijstabel

### Gedifferentieerde prijstabel [ANCHOR_1]

[HTML_TAG_29]
  [HTML_TAG_30][HTML_TAG_31][HTML_TAG_32][HTML_TAG_33]
  [HTML_TAG_34][HTML_TAG_35][HTML_TAG_36]Aantal controlestations[HTML_TAG_37][HTML_TAG_38]Schaalfactor[HTML_TAG_39][HTML_TAG_40][HTML_TAG_41]
  [HTML_TAG_42]
    [HTML_TAG_43][HTML_TAG_44]1 tot en met 2[HTML_TAG_45][HTML_TAG_46]N.v.t. (zie opmerking onder de tabel)[HTML_TAG_47][HTML_TAG_48]
    [HTML_TAG_49][HTML_TAG_50]3 tot en met 4[HTML_TAG_51][HTML_TAG_52]2[HTML_TAG_53][HTML_TAG_54]
    [HTML_TAG_55][HTML_TAG_56]5 tot en met 7[HTML_TAG_57][HTML_TAG_58]3[HTML_TAG_59][HTML_TAG_60]
    [HTML_TAG_61][HTML_TAG_62]8 tot en met 10[HTML_TAG_63][HTML_TAG_64]4[HTML_TAG_65][HTML_TAG_66]
    [HTML_TAG_67][HTML_TAG_68]11 tot en met 14[HTML_TAG_69][HTML_TAG_70]5[HTML_TAG_71][HTML_TAG_72]
    [HTML_TAG_73][HTML_TAG_74]15 tot en met 18[HTML_TAG_75][HTML_TAG_76]6[HTML_TAG_77][HTML_TAG_78]
    [HTML_TAG_79][HTML_TAG_80]19 tot en met 22[HTML_TAG_81][HTML_TAG_82]7[HTML_TAG_83][HTML_TAG_84]
    [HTML_TAG_85][HTML_TAG_86]23 tot en met 26[HTML_TAG_87][HTML_TAG_88]8[HTML_TAG_89][HTML_TAG_90]
    [HTML_TAG_91][HTML_TAG_92]27 tot en met 30[HTML_TAG_93][HTML_TAG_94]9[HTML_TAG_95][HTML_TAG_96]
    [HTML_TAG_97][HTML_TAG_98]31 tot en met 35[HTML_TAG_99][HTML_TAG_100]10[HTML_TAG_101][HTML_TAG_102]
    [HTML_TAG_103][HTML_TAG_104]36 tot en met 40[HTML_TAG_105][HTML_TAG_106]11[HTML_TAG_107][HTML_TAG_108]
    [HTML_TAG_109][HTML_TAG_110]41 tot en met 45[HTML_TAG_111][HTML_TAG_112]12[HTML_TAG_113][HTML_TAG_114]
    [HTML_TAG_115][HTML_TAG_116]46 tot en met 50[HTML_TAG_117][HTML_TAG_118]13[HTML_TAG_119][HTML_TAG_120]
  [HTML_TAG_121]
[HTML_TAG_122]

[SHORTCODE_1] **Opmerking**: U moet minimaal drie (hoge beschikbaarheid) of vijf (uit alle) controlestations kiezen om gelijktijdige monitoring te gebruiken. Voor standaard monitoring moet u ook minimaal drie controlestations kiezen, maar er wordt er maar één tegelijk gebruikt (en opgenomen in de prijsberekening). [SHORTCODE_2]
### Voorbeelden

In de volgende tabellen ziet u voorbeelden van hoe de prijsstelling werkt, vergeleken tussen gelijktijdige en standaard monitoring en ook voor verschillende niveaus in gedifferentieerde prijsstelling.

**Basiscontroleregel**

[HTML_TAG_123][HTML_TAG_124][HTML_TAG_125][HTML_TAG_126][HTML_TAG_127]
  [HTML_TAG_128][HTML_TAG_129][HTML_TAG_130]Gelijktijdige monitoring (gedifferentieerde prijsstelling)[HTML_TAG_131][HTML_TAG_132]Standaard monitoring[HTML_TAG_133][HTML_TAG_134][HTML_TAG_135]
  [HTML_TAG_136]
    [HTML_TAG_137][HTML_TAG_138]HTTPS-controleregel (basisprijs van 1), door de gebruiker gedefinieerd om op 4 controlestations uit te voeren[HTML_TAG_139]
1 credit x 2 (schaalfactor) = [HTML_TAG_140]2 credits[HTML_TAG_141][HTML_TAG_142][HTML_TAG_143]HTTPS-controleregel (basisprijs van 1)[HTML_TAG_144]
1 credit x 1 = [HTML_TAG_145]1 credit[HTML_TAG_146][HTML_TAG_147][HTML_TAG_148]
    [HTML_TAG_149][HTML_TAG_150]HTTPS-controleregel (basisprijs van 1), door de gebruiker gedefinieerd om op 10 controlestations uit te voeren[HTML_TAG_151]
1 credit x 4 (schaalfactor) = [HTML_TAG_152]4 credits[HTML_TAG_153][HTML_TAG_154][HTML_TAG_155]HTTPS-controleregel (basisprijs van 1)[HTML_TAG_156]
1 credit x 1 = [HTML_TAG_157]1 credit[HTML_TAG_158][HTML_TAG_159][HTML_TAG_160]
  [HTML_TAG_161]
[HTML_TAG_162]

**Multi-step API-controleregel**

[HTML_TAG_163][HTML_TAG_164][HTML_TAG_165][HTML_TAG_166][HTML_TAG_167]
  [HTML_TAG_168][HTML_TAG_169][HTML_TAG_170]Gelijktijdige monitoring (gedifferentieerde prijsstelling)[HTML_TAG_171][HTML_TAG_172]Standaard monitoring[HTML_TAG_173][HTML_TAG_174][HTML_TAG_175]
  [HTML_TAG_176]
[HTML_TAG_177][HTML_TAG_178]MSA-controleregel met 10 stappen, door de gebruiker gedefinieerd om op 4 controlestations uit te voeren[HTML_TAG_179]
10 credits (aantal stappen) x 2 (schaalfactor) = [HTML_TAG_180]20 credits[HTML_TAG_181][HTML_TAG_182]
[HTML_TAG_183]MSA-controleregel met 10 stappen (basisprijs van 10)[HTML_TAG_184]
10 credits (aantal stappen) x 1 = [HTML_TAG_185]10 credits[HTML_TAG_186][HTML_TAG_187][HTML_TAG_188]
   [HTML_TAG_189][HTML_TAG_190]MSA-controleregel met 10 stappen, door de gebruiker gedefinieerd om op 10 controlestations uit te voeren[HTML_TAG_191]
10 credits (aantal stappen) x 4 (schaalfactor) = [HTML_TAG_192]40 credits[HTML_TAG_193][HTML_TAG_194]
[HTML_TAG_195]MSA-controleregel met 10 stappen (basisprijs van 10)[HTML_TAG_196]
10 credits (aantal stappen) x 1 = [HTML_TAG_197]10 credits[HTML_TAG_198][HTML_TAG_199][HTML_TAG_200] 
  [HTML_TAG_201]
[HTML_TAG_202]

[SHORTCODE_3] **Opmerking**: In het algemeen kunt u ervan uitgaan dat een controleregeltype met een hoge basisprijs (credits per controleregel) zal leiden tot een hoog creditverbruik als u veel controlestations opneemt. [SHORTCODE_4]
