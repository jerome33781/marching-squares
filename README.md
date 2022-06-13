# Marching Square
Visualisation d'équation cartesienne

J'ai implémenté un algorithme de marching squares permettant visualiser une ligne de valeur constante pour une équation cartesienne ou un champ scalaire.   
Cette implémentation permet dans un premier temps de dessiner des fonctions à motif complexe, comme par exemple ici : tan(x^2 + y^2) = 1

![fct_joli2](https://user-images.githubusercontent.com/83364235/173252789-e3ed160c-9ad3-4be5-a8be-10973554fe09.png)

On peut ensuite dans un second temps créer une animation visualisant les lignes de champ dans une cuve où évolueraient des particules. (ici le champ électrique généré par 3 ions de charges différentes)

![mygif2](https://user-images.githubusercontent.com/83364235/173252849-9b28b426-3f7f-4893-a548-c93e61176173.gif)

Dans une version plus complète, on pourrait plutôt que de dessiner une ligne de valeur constante, visualiser le champ dans tout l'espace par un gradient de couleur.

Enfin, en utilisant cet algorithme, on peut vérifier l'approximation du champ constant dans un condensateur plan : on positionne un grand nombre d'electrons sur deux plaques et on trace le champ dans l'espace du condensateur. On peut alors vérifier sous quelles conditions le modèle du condensateur plan est valable.

![champs E cond](https://user-images.githubusercontent.com/83364235/173253274-9c4a6fba-f585-4f85-abcb-f8f4ac54dd3d.png)
![potentiel cond](https://user-images.githubusercontent.com/83364235/173253280-069c137e-aea3-490b-97f5-5301168579b1.png)

On remarque ici que l'hypothèse pour une telle plaque est valable, le champ E est constant dans l'espace entre les plaques, et le potentiel est linéaire. On distingue les limites du condensateur plan sur les bords des plaques, le potentiel a une ligne isovaleur courbée est non plan, son gradient et donc E n'est donc pas seulement selon l'axe x. 
