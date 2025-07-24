{
  "hero": {
    "title": "Tarification pour la surveillance simultanée"
  },
  "title": "Tarification pour la surveillance simultanée",
  "summary": "Dans cet article, vous trouverez les formules de calcul ainsi que des exemples pour connaître le prix que coûtera la surveillance simultanée.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/surveillance-simultanee/tarifs-calcul-exemples",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Tarification pour le Full Page Check (FPC) et les moniteurs de transactions

Le calcul du prix est basé sur un système de crédits, où les différents types de moniteurs ont des coûts de base différents, exprimés en crédits. Donc en général, le calcul est le suivant :

Prix = le prix de base du moniteur x le nombre de points de contrôle utilisé dans la vérification.

### Exemple avec comparaison

Dans le tableau suivant vous trouverez un exemple des tarifs, en comparant la surveillance simultanée et la surveillance standard.

[HTML_TAG_1][HTML_TAG_2][HTML_TAG_3][HTML_TAG_4][HTML_TAG_5][HTML_TAG_6][HTML_TAG_7][HTML_TAG_8]Surveillance simultanée[HTML_TAG_9][HTML_TAG_10]Surveillance standard[HTML_TAG_11][HTML_TAG_12][HTML_TAG_13][HTML_TAG_14][HTML_TAG_15][HTML_TAG_16]Transaction (coût de 4 crédits), définie par l'utilisateur pour s'exécuter sur 3 points de contrôle[HTML_TAG_17]

4 crédits x 3 = [HTML_TAG_18]12 crédits[HTML_TAG_19][HTML_TAG_20][HTML_TAG_21]Transaction (coût de 4 crédits)[HTML_TAG_22]

4 crédits x 1 = [HTML_TAG_23]4 crédits[HTML_TAG_24][HTML_TAG_25][HTML_TAG_26][HTML_TAG_27][HTML_TAG_28]

## Tarification pour les moniteurs de base et les moniteurs API multi-étapes (MSA)

Pour ces moniteurs, la tarification se fait par paliers avec un coût dégressif, le prix est donc calculé différemment des autres Full Page Check (FPC) et moniteurs de transactions. Les moniteurs de base comprennent les moniteurs Ping, Http(s), certificat SSL, etc. Gardez également à l'esprit que pour un moniteur MSA, le prix dépend du nombre d'étapes. Les formules de prix sont données ci-dessous.

**Moniteur de base**

Prix = le prix de base du moniteur x le coût dégressif du tableau du coût par palier ci-dessous.

**Moniteur MSA**

Prix = le nombre d'étapes du moniteur MSA x le coût dégressif du tableau du coût par palier ci-dessous.

### Tableau du coût par palier [ANCHOR_1]

[HTML_TAG_29]
[HTML_TAG_30][HTML_TAG_31][HTML_TAG_32][HTML_TAG_33]
[HTML_TAG_34][HTML_TAG_35][HTML_TAG_36]Nombre de points de contrôle[HTML_TAG_37][HTML_TAG_38]Coût dégressif[HTML_TAG_39][HTML_TAG_40][HTML_TAG_41]

[HTML_TAG_42]

[HTML_TAG_43][HTML_TAG_44]1 à 2[HTML_TAG_45][HTML_TAG_46]N/A (voir note sous le tableau)[HTML_TAG_47][HTML_TAG_48]
[HTML_TAG_49][HTML_TAG_50]3 à 4[HTML_TAG_51][HTML_TAG_52]2[HTML_TAG_53][HTML_TAG_54]
[HTML_TAG_55][HTML_TAG_56]5 à 7[HTML_TAG_57][HTML_TAG_58]3[HTML_TAG_59][HTML_TAG_60]
[HTML_TAG_61][HTML_TAG_62]8 à 10[HTML_TAG_63][HTML_TAG_64]4[HTML_TAG_65][HTML_TAG_66]
[HTML_TAG_67][HTML_TAG_68]11 à 14[HTML_TAG_69][HTML_TAG_70]5[HTML_TAG_71][HTML_TAG_72]
[HTML_TAG_73][HTML_TAG_74]15 à 18[HTML_TAG_75][HTML_TAG_76]6[HTML_TAG_77][HTML_TAG_78]
[HTML_TAG_79][HTML_TAG_80]19 à 22[HTML_TAG_81][HTML_TAG_82]7[HTML_TAG_83][HTML_TAG_84]
[HTML_TAG_85][HTML_TAG_86]23 à 26[HTML_TAG_87][HTML_TAG_88]8[HTML_TAG_89][HTML_TAG_90]
[HTML_TAG_91][HTML_TAG_92]27 à 30[HTML_TAG_93][HTML_TAG_94]9[HTML_TAG_95][HTML_TAG_96]
[HTML_TAG_97][HTML_TAG_98]31 à 35[HTML_TAG_99][HTML_TAG_100]10[HTML_TAG_101][HTML_TAG_102]
[HTML_TAG_103][HTML_TAG_104]36 à 40[HTML_TAG_105][HTML_TAG_106]11[HTML_TAG_107][HTML_TAG_108]
[HTML_TAG_109][HTML_TAG_110]41 à 45[HTML_TAG_111][HTML_TAG_112]12[HTML_TAG_113][HTML_TAG_114]
[HTML_TAG_115][HTML_TAG_116]46 à 50[HTML_TAG_117][HTML_TAG_118]13[HTML_TAG_119][HTML_TAG_120]
[HTML_TAG_121]

[HTML_TAG_122]

[SHORTCODE_1] **Remarque** : Pour utiliser la surveillance simultanée vous devez choisir un nombre minimum de points de contrôle, trois pour la haute disponibilité ou cinq en tout. Pour une surveillance standard, vous devez également choisir un minimum de trois points de contrôle, mais un seul sera utilisé à la fois (et inclus dans le calcul du prix). [SHORTCODE_2]
### Exemples

Dans le tableau suivant vous trouverez un exemple des tarifs, en comparant la surveillance simultanée et la surveillance standard, ainsi que pour différents niveaux dans la tarification à paliers

**Moniteur de base**

[HTML_TAG_123][HTML_TAG_124][HTML_TAG_125][HTML_TAG_126][HTML_TAG_127]

[HTML_TAG_128][HTML_TAG_129][HTML_TAG_130]Surveillance simultanée (tarification à paliers)[HTML_TAG_131][HTML_TAG_132]Surveillance standard[HTML_TAG_133][HTML_TAG_134][HTML_TAG_135]

[HTML_TAG_136]

[HTML_TAG_137][HTML_TAG_138]Moniteur HTTPS (prix de base de 1), défini par l'utilisateur pour s'exécuter sur 4 points de contrôle[HTML_TAG_139]1 crédit x 2 (coût dégressif) = [HTML_TAG_140]2 crédits[HTML_TAG_141][HTML_TAG_142]
[HTML_TAG_143]Moniteur HTTPS (prix de base de 1)[HTML_TAG_144]1 crédit x 1 = [HTML_TAG_145]1 crédit[HTML_TAG_146][HTML_TAG_147][HTML_TAG_148]
[HTML_TAG_149][HTML_TAG_150]Moniteur HTTPS (prix de base de 1), défini par l'utilisateur pour fonctionner sur 10 points de contrôle[HTML_TAG_151]1 crédit x 4 (coût dégressif) = [HTML_TAG_152]4 crédits[HTML_TAG_153][HTML_TAG_154][HTML_TAG_155]Moniteur HTTPS (prix de base de 1)[HTML_TAG_156]1 crédit x 1 = [HTML_TAG_157]1 crédit[HTML_TAG_158][HTML_TAG_159][HTML_TAG_160]
[HTML_TAG_161]

[HTML_TAG_162]

**Moniteur API multi-étapes**

[HTML_TAG_163][HTML_TAG_164][HTML_TAG_165][HTML_TAG_166][HTML_TAG_167]

  [HTML_TAG_168][HTML_TAG_169][HTML_TAG_170]Surveillance simultanée (tarification à paliers)[HTML_TAG_171][HTML_TAG_172]Surveillance standard[HTML_TAG_173][HTML_TAG_174][HTML_TAG_175]

  [HTML_TAG_176]

[HTML_TAG_177][HTML_TAG_178]Moniteur MSA avec 10 étapes, défini par l'utilisateur pour s'exécuter sur 4 points de contrôle[HTML_TAG_179]

10 crédits (nombre d'étapes) x 2 (coût dégressif) = [HTML_TAG_180]20 crédits[HTML_TAG_181][HTML_TAG_182]

[HTML_TAG_183]Moniteur MSA avec 10 étapes (prix de base de 10)[HTML_TAG_184]

10 crédits (nombre d'étapes) x 1 = [HTML_TAG_185]10 crédits[HTML_TAG_186][HTML_TAG_187][HTML_TAG_188]

   [HTML_TAG_189][HTML_TAG_190]Moniteur MSA avec 10 étapes, défini par l'utilisateur pour fonctionner sur 10 points de contrôle[HTML_TAG_191]

10 crédits (nombre d'étapes) x 4 (coût dégressif) = [HTML_TAG_192]40 crédits[HTML_TAG_193][HTML_TAG_194]

[HTML_TAG_195]Moniteur MSA avec 10 étapes (prix de base de 10)[HTML_TAG_196]

10 crédits (nombre d'étapes) x 1 = [HTML_TAG_197]10 crédits[HTML_TAG_198][HTML_TAG_199][HTML_TAG_200] 

  [HTML_TAG_201]

[HTML_TAG_202]

[SHORTCODE_3] **Remarque** : En général, vous devez garder à l'esprit qu'un type de moniteur avec un prix de base élevé (crédits par moniteur) entraînera une utilisation élevée de crédits lorsque vous utilisez de nombreux points de contrôle. [SHORTCODE_4]
