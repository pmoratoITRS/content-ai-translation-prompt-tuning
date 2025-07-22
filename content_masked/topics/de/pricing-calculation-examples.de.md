{
  "hero": {
    "title": "Preise für das Parallel-Monitoring"
  },
  "title": "Preise für das Parallel-Monitoring",
  "summary": "In diesem Artikel erfährst du, nach welchen Formeln die Credits des Parallel-Monitorings berechnet werden. Dazu gibt es Beispiele.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/parallel-monitoring/preisberechnung-beispiele",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Preise für Full Page Checks (FPC) und Transaktionsprüfobjekte

Der Preis wird anhand des Credit-Systems berechnet, bei dem unterschiedliche Prüfobjekttypen unterschiedliche Grundpreise haben – als Credit ausgedrückt. Im Allgemeinen ist die Berechnung wie folgt:

Preis = Grundpreis des Prüfobjekts x Anzahl der Checkpoints, die die Prüfung ausführen

### Vergleichsbeispiel

Die folgende Tabelle zeigt anhand eines Beispiels wie das Preissystem funktioniert – als Vergleich zwischen parallelem und klassischem Monitoring.

[HTML_TAG_1][HTML_TAG_2][HTML_TAG_3][HTML_TAG_4][HTML_TAG_5][HTML_TAG_6][HTML_TAG_7][HTML_TAG_8]Parallel-Monitoring[HTML_TAG_9][HTML_TAG_10]Standard-Monitoring[HTML_TAG_11][HTML_TAG_12][HTML_TAG_13][HTML_TAG_14][HTML_TAG_15][HTML_TAG_16]Transaktion (Grundpreis 4 Credits), benutzerdefiniert auf 3 Checkpoints ausgeführt[HTML_TAG_17]
4 Credits x 3 = [HTML_TAG_18]12 Credits[HTML_TAG_19][HTML_TAG_20][HTML_TAG_21]Transaktion (Grundpreis 4 Credits)[HTML_TAG_22]
4 Credits x 1 = [HTML_TAG_23]4 Credits[HTML_TAG_24][HTML_TAG_25][HTML_TAG_26][HTML_TAG_27][HTML_TAG_28]

## Preise für einfache Prüfobjekte und Multi-step API (MSA)-Prüfobjekte 

Für diese Prüfobjekte wird ein Preisstufenmodell mit einem Skalierungsfaktor angesetzt. Die Preisberechnung unterscheidet sich daher zu der von Full Page Checks und Transaktionsprüfobjekten. Einfache Prüfobjekte umfassen Ping, Http(s), SSL-Zertifikate usw. Bedenke auch, dass der Preis bei einem MSA-Prüfobjekt von der Anzahl der Schritte abhängt. Unten findest du die Preisformel.

**Einfache Prüfobjekte**

Preis = Grundpreis des Prüfobjekts x Skalierungsfaktor aus der Preisstufentabelle unten

**MSA-Prüfobjekt**

Preis = Anzahl der Schritte des MSA-Prüfobjekts x Skalierungsfaktor aus der Preisstufentabelle unten

### Preisstufentabelle [ANCHOR_1]

[HTML_TAG_29]
  [HTML_TAG_30][HTML_TAG_31][HTML_TAG_32][HTML_TAG_33]
  [HTML_TAG_34][HTML_TAG_35][HTML_TAG_36]Anzahl Checkpoints[HTML_TAG_37][HTML_TAG_38]Skalierungsfaktor[HTML_TAG_39][HTML_TAG_40][HTML_TAG_41]
  [HTML_TAG_42]
    [HTML_TAG_43][HTML_TAG_44]1 bis 2[HTML_TAG_45][HTML_TAG_46]N/A (siehe Hinweis am Ende d. Tabelle)[HTML_TAG_47][HTML_TAG_48]
    [HTML_TAG_49][HTML_TAG_50]3 bis 4[HTML_TAG_51][HTML_TAG_52]2[HTML_TAG_53][HTML_TAG_54]
    [HTML_TAG_55][HTML_TAG_56]5 bis 7[HTML_TAG_57][HTML_TAG_58]3[HTML_TAG_59][HTML_TAG_60]
    [HTML_TAG_61][HTML_TAG_62]8 bis 10[HTML_TAG_63][HTML_TAG_64]4[HTML_TAG_65][HTML_TAG_66]
    [HTML_TAG_67][HTML_TAG_68]11 bis 14[HTML_TAG_69][HTML_TAG_70]5[HTML_TAG_71][HTML_TAG_72]
    [HTML_TAG_73][HTML_TAG_74]15 bis 18[HTML_TAG_75][HTML_TAG_76]6[HTML_TAG_77][HTML_TAG_78]
    [HTML_TAG_79][HTML_TAG_80]19 bis 22[HTML_TAG_81][HTML_TAG_82]7[HTML_TAG_83][HTML_TAG_84]
    [HTML_TAG_85][HTML_TAG_86]23 bis 26[HTML_TAG_87][HTML_TAG_88]8[HTML_TAG_89][HTML_TAG_90]
    [HTML_TAG_91][HTML_TAG_92]27 bis 30[HTML_TAG_93][HTML_TAG_94]9[HTML_TAG_95][HTML_TAG_96]
    [HTML_TAG_97][HTML_TAG_98]31 bis 35[HTML_TAG_99][HTML_TAG_100]10[HTML_TAG_101][HTML_TAG_102]
    [HTML_TAG_103][HTML_TAG_104]36 bis 40[HTML_TAG_105][HTML_TAG_106]11[HTML_TAG_107][HTML_TAG_108]
    [HTML_TAG_109][HTML_TAG_110]41 bis 45[HTML_TAG_111][HTML_TAG_112]12[HTML_TAG_113][HTML_TAG_114]
    [HTML_TAG_115][HTML_TAG_116]46 bis 50[HTML_TAG_117][HTML_TAG_118]13[HTML_TAG_119][HTML_TAG_120]
  [HTML_TAG_121]
[HTML_TAG_122]

[SHORTCODE_1] **Hinweis**: Du musst mindestens drei (hoch verfügbare) oder fünf (unter allen) Checkpoints wählen, um das Parallel-Monitoring zu nutzen. Für das Standard-Monitoring musst du ebenfalls mindestens drei Checkpoints auswählen, aber es wird jeweils nur einer zum jeweiligen Testzeitpunkt eingesetzt (und in der Preisberechnung berücksichtigt). [SHORTCODE_2]
### Vergleichsbeispiele

Die folgenden Tabellen zeigen anhand von Beispielen, wie das Preissystem funktioniert – als Vergleich zwischen parallelem und Standard-Monitoring und für unterschiedliche Level beim Preisstufenmodell.

**Einfache Prüfobjekte**

[HTML_TAG_123][HTML_TAG_124][HTML_TAG_125][HTML_TAG_126][HTML_TAG_127]
  [HTML_TAG_128][HTML_TAG_129][HTML_TAG_130]Parallel-Monitoring (Preisstufen)[HTML_TAG_131][HTML_TAG_132]Standard-Monitoring[HTML_TAG_133][HTML_TAG_134][HTML_TAG_135]
  [HTML_TAG_136]
    [HTML_TAG_137][HTML_TAG_138]HTTPS-Prüfobjekt (Grundpreis 1 Credit), benutzerdefiniert auf 4 Checkpoints ausgeführt[HTML_TAG_139]
1 Credit x 2 (Skalierungsfaktor) = [HTML_TAG_140]2 Credits[HTML_TAG_141][HTML_TAG_142][HTML_TAG_143]HTTPS-Prüfobjekt (Grundpreis 1 Credit)[HTML_TAG_144]
1 Credit x 1 = [HTML_TAG_145]1 Credit[HTML_TAG_146][HTML_TAG_147][HTML_TAG_148]
    [HTML_TAG_149][HTML_TAG_150]HTTPS-Prüfobjekt (Grundpreis 1 Credit), benutzerdefiniert auf 10 Checkpoints ausgeführt[HTML_TAG_151]
1 Credit x 4 (Skalierungsfaktor) = [HTML_TAG_152]4 Credits[HTML_TAG_153][HTML_TAG_154][HTML_TAG_155]HTTPS-Prüfobjekt (Grundpreis 1 Credit)[HTML_TAG_156]
1 Credit x 1 = [HTML_TAG_157]1 Credit[HTML_TAG_158][HTML_TAG_159][HTML_TAG_160]
  [HTML_TAG_161]
[HTML_TAG_162]

**Multi-step API-Prüfobjekt**

[HTML_TAG_163][HTML_TAG_164][HTML_TAG_165][HTML_TAG_166][HTML_TAG_167]
  [HTML_TAG_168][HTML_TAG_169][HTML_TAG_170]Parallel-Monitoring (Preisstufen)[HTML_TAG_171][HTML_TAG_172]Standard-Monitoring[HTML_TAG_173][HTML_TAG_174][HTML_TAG_175]
  [HTML_TAG_176]
[HTML_TAG_177][HTML_TAG_178]MSA-Prüfobjekt mit 10 Schritten, benutzerdefiniert auf 4 Checkpoints ausgeführt[HTML_TAG_179]
10 Credits (Anzahl d. Schritte) x 2 (Skalierungsfaktor) = [HTML_TAG_180]20 Credits[HTML_TAG_181][HTML_TAG_182]
[HTML_TAG_183]MSA-Prüfobjekt mit 10 Schritten (Grundpreis 10 Credits)[HTML_TAG_184]
10 Credits (Anzahl d. Schritte) x 1 = [HTML_TAG_185]10 Credits[HTML_TAG_186][HTML_TAG_187][HTML_TAG_188]
   [HTML_TAG_189][HTML_TAG_190]MSA-Prüfobjekt mit 10 Schritten, benutzerdefiniert auf 10 Checkpoints ausgeführt[HTML_TAG_191]
10 Credits (Anzahl d. Schritte) x 4 (Skalierungsfaktor) = [HTML_TAG_192]40 Credits[HTML_TAG_193][HTML_TAG_194]
[HTML_TAG_195]MSA-Prüfobjekt mit 10 Schritten (Grundpreis 10 Credits)[HTML_TAG_196]
10 Credits (Anzahl d. Schritte) x 1 = [HTML_TAG_197]10 Credits[HTML_TAG_198][HTML_TAG_199][HTML_TAG_200] 
  [HTML_TAG_201]
[HTML_TAG_202]

[SHORTCODE_3] **Hinweis**: Im Allgemeinen ist also zu bedenken, dass ein Prüfobjekttyp mit einem höheren Grundpreis (Credits pro Prüfobjekt) zu einem hohen Credit-Verbrauch führt, wenn viele Checkpoints einbezogen werden. [SHORTCODE_4]
