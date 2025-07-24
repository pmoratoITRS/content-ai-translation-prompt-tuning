{
  "hero": {
    "title": "Fréquence de la vérification : une explication"
  },
  "title": "Fréquence de la vérification : une explication",
  "summary": "The check interval is the time between the end of the last check and the beginning of the next.",
  "url": "[URL_BASE_TOPICS]surveillance-synthetique/parametres-moniteurs/frequence-de-la-verification-une-explication",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

La troisième option dans les paramètres de votre moniteur vous demande la fréquence de vérification (voir la figure ci-dessous). La vérification peut se faire aussi souvent qu'une fois par minute ou au maximum une fois par heure. Alors, que signifie exactement "Fréquence de vérification" ? **C'est la durée entre la fin d'une vérification et le début de la vérification suivante.** Regardons ça de plus près.

![]([LINK_URL_1])

Vous auriez pu penser qu'avec une fréquence de vérification d'une minute, Uptrends vérifierait votre site web 1440 fois par jour, chaque vérification commençant au top de chaque minute ; ce n'est pas le cas ! Uptrends doit s'assurer que la vérification précédente s'est terminée avec succès avant de planifier la vérification suivante. Par conséquent, le nombre de vérifications effectuées chaque jour dépend :

-   du type de moniteur
-   du temps de chargement de la page ou de la réponse
-   de la fréquence que vous avez sélectionnée
-   des nombres d'erreurs rencontrées avec votre site ou service, et
-   des temps annexes du système : l'envoi de la définition de la fréquence au point de contrôle, son traitement, la transmission et puis le traitement des résultats.

Regardons quelques exemples :

**Vérification de la disponibilité, fréquence = 1 minute**

Si une vérification de la disponibilité prend dix secondes du début à la fin, la vérification suivante commence 60 secondes après la fin de la vérification. Ainsi, dans ce cas, il y aura un intervalle d'environ 70 secondes entre le début d'une vérification et le début de la suivante. Au lieu de 1 440 vérifications par jour, il y en aurait environ 1 234.

**Moniteur de transaction, fréquence = 5 minutes**

Les transactions complexes peuvent prendre un certain temps en fonction du nombre d'étapes et de la réactivité de votre site ou service. Si une vérification dure deux minutes du début à la fin, la prochaine vérification a lieu cinq minutes après la fin de la vérification, donc sept minutes après le début de la première vérification. Au lieu de 288 vérifications par jour, ce scénario génère environ 206 vérifications par jour.

## Comment les erreurs affectent-elles la fréquence de vérification de mon moniteur ?

Lorsqu’Uptrends reçoit une erreur de votre site web ou de votre service, Uptrends ne tient pas compte de la fréquence de vérification, mais génère immédiatement une autre vérification à partir d'un autre point de contrôle. Si Uptrends reçoit une deuxième erreur, Uptrends envoie une alerte. Uptrends planifie ensuite la prochaine vérification en fonction de votre valeur de fréquence de vérification. Lors du top suivant, Uptrends vérifie à nouveau et effectue une double vérification en cas d'erreur. Notez que dans le journal du moniteur ci-dessous, bien que le moniteur dispose d'une fréquence de vérification de cinq minutes, les erreurs confirmées (en rouge) se produisent immédiatement après les erreurs non confirmées (en jaune). L'intervalle de temps entre l'erreur confirmée et la vérification suivante est de cinq minutes.

![]([LINK_URL_2])
