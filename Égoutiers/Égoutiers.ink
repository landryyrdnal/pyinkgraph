-> debut

=== debut===

    — « Tiens essayes si tu peux », l’homme vous tend la perche flexible au bout de laquelle est fixée un crochet.
    
        * (vexe)— « Eu… bah, je sais pas… »
        L’autre vous coupe net : « Tu rigoles !? Fais pas ton petit bourgeois ! Vas-y je te dis, si tu y met jamais les mains tu n’apprendras jamais rien ! »
         Au ton de sa voix, vous sentez de l’ironie se mêler à de l’agacement.
            ** Vous prenez la perche[] un peu vexé…
        
        * [— « Ok »]
        Vous prenez la perche.
        
    - — « Tu la met comme ça, l’idée c’est de sentir ce qui bouche et de voir si ça bouge{vexe:, fais pas la gueule, il faut bien en passer par là !|… t’as pas peur toi ! C’est bien !} »
    
        * Vous enfoncez la perche dans le [tubulaire] petit conduit.
        — « Ça c’est l’évacuation de l’immeuble qu’on voyait en entrant dans l’égout bon normalement c’est pas à nous de le faire, mais bon, on est sympa… Non attends ! Prends-la comme ça, tu y arrivera mieux »

    // à améliorer !
    - Vous tâtonez quelques instants jusqu’à sentir là résistance du bouchon, une résistance…<>
        * [Molle & visqueuse]<>
        plutôt molle et visqueuse. -> debouchage("un chiffon")
        * [Granuleuse & éffritable]<>
        plutôt granuleuse. -> debouchage("un morceau de moellon")
        * [Élastique & cahoutchouteuse]<>
        plutôt élastique. -> debouchage("un balon crevé")

    
    = debouchage(bouchon)
    

    * [Vous tournez le crochet]
    Vos gesticulations n’agrippent rien… mais la chose obstruante commence à prendre forme à l’intérieur de votre tête à force de la parcourir du bout  de votre crochet.
        
        ** (couleur)[Vous essayez de regarder à l’intérieur du conduit]
        Vous ne distinguez rien d’ici, si ce n’est un truc 
            {bouchon == "un chiffon": crâde et vaguement blanc}
            {bouchon == "un balon crevé": vaguement orange et plutôt lisse}
            {bouchon == "un morceau de moellon": vaguement rocailleux}<>, <>
            englué dans…
            *** [De la merde…]
                <> de la merde
            {not crochet: -> crochet}
            
        ** (crochet)[Vous essayez encore d’agripper quelque chose avec le crochet]
        Vous retentez d’agriper le bouchon avec le crochet.
            *** [Vous le tournez]
            — « Non, pas comme ça… »
                **** [Le retournez]
                — « Toujours pas… »
                    ***** {not couleur} [Vous essayez de regarder à l’intérieur du conduit] -> couleur
                    ***** {couleur} [Vous tourner encore]
    
    - À force de tourner, de retourner votre crochet, d’appuyer, de relâcher ; l’objet apparaît net dans votre esprit : c’est {bouchon}, ça ne fait aucun doute !
        * [Vous l’annoncez à votre collègue]
        — « Je pense que c’est {bouchon}, ou un truc du genre… »
        — « Peut-être bien… En dix ans j’en ai vu des trucs, et des trucs autrements plus improbables. C’est peut être ça, mais c’est pas dit… » vous répond-il un peu blasé.
            ** — « Quel genre de trucs improbables ?[ »] C’est quoi le pire que vous ayez vu ? » lui demandez vous.
            — « Je crois que le pire ça a été la fois où on a trouvé un doigt. » -> truc_improbable
    
    
    = truc_improbable
        * — « Un doigt ?![ »] Tu veux dire… » 
        Sourire aux lèvre, l’autre vous fait un doigt d’honneur : « Exactement comme celui-là ! »
            ** (amuse)— « Non ! Sérieusement ? »[] vous comprenez que votre air déconcerté l’amuse beaucoup…
            ** (defie)— « Je ne te crois pas ! »
            -- — « {amuse:Ahah ! m}{not amuse:M}ais je t’assure ! {amuse:Et puis là j’en rigoles, mais sur}{not amuse:Sur} le moment, c’était pas drôle du tout ! »
            ** [— « Vous en avez fait quoi ? »]— « Et alors, vous en avez fait quoi ? »
            
            --    (doigt){stopping:
                - — « Ahah ! t’es drôle toi, on n’allait pas le garder ! T’aurais voulu qu’on le garde ? Nan, on l’as juste balancé.  »
                - Vous sentez que votre collègue est un peu mal à l’aise avec cette affaire.
                - Vous essuyez un moment de silence « Bon, on s’y remet ? ça ne va pas se déboucher tout seul ! » -> suite
                }
                
                ** — « Et vous n’avez alerté personne ?[ »] Les flics ou  les pompiers ? »
                    — « Ça n’aurait servi à rien, de toute façon, vu l’état du truc, on aurait pas pu le rendre à son propriétaire… » il marque une pause comme pour chercher ses mots : « Et puis de toute façon on as un peu paniqué, on ne voulait pas avoir d’emmerdes alors le mieux c’était de vite l’oublier » -> doigt
                ** — « Comment c’est arrivé ? »
                    — « Comment ça comment c’est arrivé ? On visitait un égout, visite de routine quoi ! Comme là. Et puis il y avait un tas de gravas alors on as ramassé les gravas dans le seau et puis en remontant le seau, à la lumière du jour, on as vu qu’il y avait un doigt… » -> doigt
                ** — « Vous auriez dû le garder ![ »] Ça aurait fait un bon souvenir pour votre musée !
                    — « Comment, ils t’en ont parlés du musée ? » Vous opinez. « De toute façon on n’était pas très bien de voir ce truc apparaître, on est habitués à en voir des trucs dégeux, mais là c’était pas pareil, c’était violent quand même… » -> doigt
            - (suite)
        
// finir le point pour déboucher le tuyaux. Pour chaque objet il faut une sorte de récompense spéciale pour le joueur.

   
    
    
    

        
        -> END