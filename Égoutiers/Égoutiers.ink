-> debut

=== debut===

    — « Tiens essayes voir… », l’homme vous tend la perche flexible au bout de laquelle est fixée un crochet.
    
        * (vexe)— « Eu… bah, je sais pas… »
            L’autre vous coupe net : « Tu rigoles !? Fais pas ton petit bourgeois ! Vas-y je te dis, si tu y met jamais les mains, tu n’apprendras jamais rien ! »
            Au ton de sa voix, vous sentez toute son ironie se mêler à de l’agacement.
            ** Vous prenez la perche[] un peu vexé…
        
        * [— « Ok. »]
            Vous prenez la perche.
        
    - — « Tu la met comme ça, l’idée c’est de sentir ce qui bouche et de voir si ça bouge, c’est pas très compliqué{vexe:, fais pas la gueule, il faut bien en passer par là !|… T’as pas peur toi ! C’est bien !} »
    
        * Vous enfoncez la perche dans le [tubulaire] petit conduit.
            — « Ça c’est l’évacuation de l’immeuble qu’on voyait en entrant dans l’égout. Bon, normalement c’est pas à nous de le faire, on ne s’occupe pas du réseau privé, mais bon, on est sympa… Non attends ! Prends-la comme ça, tu y arrivera mieux »

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
        
        ** (jete_un_oeil)[Vous essayez de regarder à l’intérieur du conduit]
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
                    ***** {not jete_un_oeil} [Vous essayez de regarder à l’intérieur du conduit] -> jete_un_oeil
                    ***** {jete_un_oeil} [Vous tourner encore]
    
    - À force de tourner, de retourner votre crochet, d’appuyer, de relâcher ; l’objet apparaît net dans votre esprit : c’est {bouchon}, ça ne fait aucun doute !
        
        * [Vous l’annoncez à votre collègue]
            — « Je pense que c’est {bouchon}, ou un truc du genre… »
            — « Peut-être bien… » vous répond-il un peu blasé, « En dix ans j’en ai vu des trucs, et des trucs autrements plus improbables. Ça peut être ça, mais c’est pas dit… »
            ** — « Quel genre de trucs improbables ?[ »] C’est quoi le pire que vous ayez vu avec les autres ? » lui demandez vous.
                — « Je crois que le pire ça a été la fois où on a trouvé un doigt. » -> histoire_doigt
            ** — « Ça te paraît bizarre ? »
                — « Non je dis ça comme ça… attends-toi juste à rien, tu risque d’être un peu déçu. À la fin c’est toujours de la merde qu’il y a dans ces conduits, quand ce n’est pas pire… »
                *** (pire)— « Pire ?»[] Intrigué, vous marquez une pause attendant la réponse de votre collègue.
                    — « Oh oui ! Tu sais, il faut s’estimer heureux de n’avoir que de la merde, au moins ce n’est pas chimique, ça ne rentre pas dans tes poumons pour les bousiller. »
                    **** — « C’est pas terrible non plus la merde… »
                        — « Non c’est pas terrible mais au moins on sait que ça ne va nous faire de mal, au pire ça renforce le système imunitaire… »
                    **** — « C’est ce qu’il y a de pire les trucs chimiques ? »
                        — « Pour la santé oui… »
                *** — « De toute façon je ne m’attends à rien… »
                --- Tout en l’écoutant parler, vous vous étonnez du fait qu’au lieu de vous déconcentrer, la discussion vous plonge dans une sorte de transe grâce à laquelle vous vous faîtes une image vraiment nette de ce qui coince. 
                *** C’est bien {bouchon}[ !] que vous avez là !
                        L’autre continue : « …Mais bon, je crois que le pire du pire, ça a été la fois où on a trouvé un doigt… » -> histoire_doigt
        * [Vous ne dîtes rien]
            — « Alors, tu y arrives ? C’est pas toujours évident. Des fois on as de la chance et puis des fois non. »
            ** (chanceux)— « J’ai toujours de la chance ! »
            ** (pas_chanceux)— « J’ai plutôt la poisse en général[. »], la preuve, regarde le boulot que je me retrouve à faire ! »
            ** (presque)— « Encore un peu, j’y suis presque ! »
           
            ** (pas_causant) [Ne pas répondre.]
                — « Hé bien ! t’es pas très causant toi ! Tu as peur que ça t’éclabousse dans bouche ? »
                *** [Le prendre à la rigolade]
                    — « Ahah ! Non c’est que j’en ai déjà trop avalé pour aujourd’hui ! » -> bruit
                *** [Le prendre au sérieux]
                    — « T’es vraiment crâde ! » -> bruit
            -- — « On vas bien voir, de toute façon ces choses là ça ne se décident pas… »
             
            -- (bruit) En disant celà, un claquement guturale se fait entendre du fin fond du tubulaire.
                — « Ah ! On dirait que ça bouge ! »
                *** {chanceux or presque} — « [On dirait surtout que la chance me sourit ! »]Qu’est-ce que j’avais dis ? on dirait bien que la chance me sourit ! »
                    Votre air triomphant ne semble pas convaincre votre collègue : « Tu sais, ça peut peut-être se déboucher, mais tu peux aussi te retrouver couvert de merde… »
                    **** — « On va voir ce qu’on va voir ! »
                    **** Vous restez silencieux.
                    ---- Votre collègue vous regarde, circonspect :
                        — « Et quand bien même tu recevrait tout dans la gueule, dis toi que ce n’est pas ce qu’on trouve de pire dans ce métier… » 
                        -> pire
                *** {pas_chanceux}— « Oulà ![ »] tu vas voir qu’avec la chance que j’ai, ça va tout me revenir dans la gueule. »
                        — « C’est possible ! Mais ne t’inquiètes pas c’est pas ce qu’il y a de pire dans ce métier.» vous répond-il d’un air blasé. 
                        -> pire
                *** {pas_causant}
                
            // Ce choix doit in fine mener à histoire doigt ou à pire
        

    = histoire_doigt
    
        * — « Un doigt ?![ »] Tu veux dire… » 
            Sourire aux lèvre, l’autre vous fait un doigt d’honneur : « Exactement comme celui-là ! »
            ** (amuse)— « Non ! Sérieusement ? »[] vous comprenez que votre air déconcerté l’amuse beaucoup…
            ** (defie)— « Je ne te crois pas ! »
            -- — « {amuse:Ahah ! m}{not amuse:M}ais je t’assure ! {amuse:Et puis là j’en rigoles, mais sur}{not amuse:Sur} le moment, c’était pas drôle du tout ! »
            ** [— « Vous en avez fait quoi ? »]— « Et alors, vous en avez fait quoi ? »
            
        -    (doigt){stopping:
            - — « Ahah ! t’es drôle toi, on n’allait pas le garder ! T’aurais voulu qu’on le garde ? Nan, on l’as juste balancé.  »
            - Vous sentez que votre collègue est un peu mal à l’aise avec cette affaire. -> suite
                    }
            
        * — « Et vous n’avez alerté personne ?[ »] Les flics ou  les pompiers ? »
            — « Ça n’aurait servi à rien, de toute façon, vu l’état du truc, on aurait pas pu le rendre à son propriétaire… » Il marque une pause comme pour chercher ses mots.
            ** [Vous le regardez, un peu déconcerté]
                – « …Et puis de toute façon on as un peu paniqué, on ne voulait pas avoir d’emmerdes alors le mieux c’était de vite l’oublier » -> doigt
        * — « Comment c’est arrivé ? »
            — « Comment ça comment c’est arrivé ? On visitait un égout, visite de routine quoi ! Comme là. Et puis il y avait un tas de gravas alors on as ramassé les gravas dans le seau et puis en remontant le seau, à la lumière du jour, on as vu qu’il y avait un doigt… » -> doigt
        * — « Vous auriez dû le garder ![ »] Ça aurait fait un bon souvenir pour votre musée !
            — « Comment, ils t’en ont parlés du musée ? » 
            ** Vous opinez[.] mais, lui ne semble pas l’avoir vu : « …De toute façon on n’était pas très bien de voir ce truc apparaître, on est habitués à en voir des trucs dégeux, mais là c’était pas pareil, c’était violent quand même… » -> doigt
            - (suite)<>  
            * Vous essuyez un moment de silence[.], un peu surpris de ce qui vient de se passer.
                — « Bon ! On s’y remet ?! On n’a pas que ça à foutre ! et puis on est pas censés faire ça, à la base… » Vous lance-t-il sèchement, histoire de passer à autre chose.
        


   
    
    
    

        
        -> END