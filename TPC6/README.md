
# Problema

Usar o flask para gerar uma interface web ao repositório filmes definido durante as aulas.

# Solução

- Utilizando a ontologia criada na aula passada e o dataset criada para o TPC 5(alterado entretanto), povoar a ontologia através do progama cinemaInspect.py.
- Utilizando a ferramenta Flask criar uma interface web para a ontologia anteriormente criada e colocada no repositório criado pelo professor.

# Ficheiros

- [cinema.ttl](https://github.com/Gon96923/RPCW2024/blob/main/TPC5/filmes.json). ontologia inicial criada na aula.
- [cinemaInspect.py](https://github.com/Gon96923/RPCW2024/blob/main/TPC5/filmes.json). aplicação que criar, com a ontologia inicial e uma lista com todos os filmes e os seus dados, uma ontologia povoada com os dados do cinema.
- [cinema_pg53849.json](https://github.com/Gon96923/RPCW2024/blob/main/TPC5/filmes.json). ontologia final com todos os dados do cinema.
- [mov.json](https://github.com/Gon96923/RPCW2024/blob/main/TPC5/movies.py) lista de todos os filmes no repsitório, asssim como os seus dados de interesse.(https://github.com/Gon96923/RPCW2024/blob/main/TPC5/mov.json).

## Na pasta app_cinema

- [templates](https://github.com/Gon96923/RPCW2024/tree/main/TPC6/app_cinema/templates). pasta com todos os templates utilizados na crição da interface web.
- [static](https://github.com/Gon96923/RPCW2024/tree/main/TPC6/app_cinema/static).
- [app.py](https://github.com/Gon96923/RPCW2024/blob/main/TPC6/app_cinema/app.py). aplicação que gera a interface web através da ferramenta flask.

# Queries

Quantos filmes existem no repositório?
```
prefix tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT (COUNT(?s) AS ?n)WHERE {
  ?s a tp:Film .
}
```

Qual a distribuição de filmes por ano de lançamento?
```
prefix tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?s ?date WHERE {
  ?s a tp:Film .
  ?s tp:date ?date .
} order by ?release
```

Qual a distribuição de filmes por género?
```
prefix tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?gen (COUNT(?s) AS ?n) WHERE {
  ?s a tp:Film .
  ?s tp:hasGenre ?gen .
} group by ?gen
order by desc(?n)
```

Em que filmes participou o ator "Burt Reynolds"?
```
prefix tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?s WHERE {
  ?s a tp:Film .
  ?s tp:hasActor ?ac .
  ?ac tp:name "Burt_Reynolds".
}
```

Produz uma lista de atores com o seu nome e o número de filmes que realizou.
```
prefix tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?name (COUNT(?fi) AS ?n) WHERE {
  ?s a tp:Actor .
  ?s tp:acted ?fi .
  ?ac tp:name ?name.
}
```

Qual o título dos livros que aparecem associados aos filmes?
```
prefix tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?b WHERE {
  ?s a tp:Film .
  ?s tp:hasBook ?b.
}
```
