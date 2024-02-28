
 quais as cidades de um determinado distrito?
```
PREFIX : <https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual/>
select ?s ?o where { 
	?s :cidade_distrito "<nome_do_distrito>" .
	?s :cidade_nome ?o .
}
```

- distribuição das cidades por distrito?
```
PREFIX : <https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual/>
select ?distrito (count(distinct ?s) as ?n) where { 
	?s :cidade_distrito ?distrito .
}
group by(?distrito)
order by(?n)
```

- quantas cidades se podem atingir a partir do Porto?
```
PREFIX : <https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual/>
select (count(distinct ?s) as ?n) where { 
	?s :cidade_distrito "Porto" .
    ?destino :temDestino ?s . 
}
```


- quais as cidades com população acima de um determinado valor?
```
PREFIX : <https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual/>
select ?c ?nome ?pop where { 
	?c :cidade_população ?pop
    filter (?pop > <valor>) .
    ?c :cidade_nome ?nome . 
}
```
