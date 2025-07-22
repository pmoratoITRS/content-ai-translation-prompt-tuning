{
  "title": "Clarification des informations sur le contournement DNS dans les détails des vérifications",
  "date": "2024-03-20",
  "url": "[URL_BASE_CHANGELOG]mars-2024-contournement-dns",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Lors de la dernière mise à jour, nous avons apporté des modifications pour afficher clairement l'URL de contournement DNS et l'adresse IP résolue dans les [détails des vérifications]([LINK_URL_1]) lorsqu'un contournement DNS est configuré. Auparavant, Uptrends montrait uniquement l'adresse IP résolue de façon séparée, ce qui pouvait manquer de clarté. Désormais, ces adresses sont plus faciles à distinguer. Vous pouvez ainsi mieux comprendre les situations et résoudre plus facilement les problèmes.

Lorsque vous créez ou que vous modifiez un moniteur Full Page Check ou un moniteur de transaction, vous pouvez ajouter un [contournement DNS]([LINK_URL_2]). Le contournement DNS permet de s'assurer que la résolution de la page web se fait dans une adresse IP spécifique, au lieu de celle utilisée par défaut. Cette option se situe dans la section _Connexion_ située dans l'onglet [SHORTCODE_1] Avancé [SHORTCODE_2] du moniteur.