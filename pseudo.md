Algoritmo:

    Select(S, k):
        S+ = {};
        Sm = {};
        S− = {};
        i <-random(1,n)

        for j=1 to n do
            if sj > si then
                S+ = S+ ∪ {sj};
            elseif sj < si then
                S− = S− ∪ {sj};
            else
                Sm = Sm U {sj}
            end if
        end for


        if k <= |S−|then          #: nesse caso k (que eh n/2) no caso da mediana é maior ou iqual ao numero de elementos no subconjuntos dos menores elementos
            return Select(S−, k);  #: logo fazemos uma busca pela mediana no grupo dos menores elementos.

        elseif k > |S−| + |Sm| then #: nesse caso verificamos se K é maior que o num elementos no subconjunto dos menores e do subconjunto dos medianos
            return Select(S+, k − |S−| − |Sm|) #: então fazemos uma busca no vetor dos maiores elementos, sendo que o novo K passa a ser K menos o numero de elementos em S- menos o numero de elementos em Sm.
        else #: nesse caso é quando K é parte do subconjunto dos medianos
            return s[i] #: logo o indice aleatorio "i" é de fato parte dos medianos, logo é a mediana. então retorna essa o elemento dessa posição