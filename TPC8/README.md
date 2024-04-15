person -> cria Pessoa com id e nome
family -> relações temPai e temMae

# Ficheiros

- [biblia.ttl](https://github.com/Gon96923/RPCW2024/blob/main/TPC8/biblia.ttl). 
- [biblia.xml](https://github.com/Gon96923/RPCW2024/blob/main/TPC8/biblia.xml). 
- [familia-base.ttl](https://github.com/Gon96923/RPCW2024/blob/main/TPC8/familia-base.ttl). 
- [xml_to_ttl.py](https://github.com/Gon96923/RPCW2024/blob/main/TPC8/xml_to_ttl.py) 

# Queries

Quantos filmes existem no repositório?
```
prefix tp: <http://www.semanticweb.org/gvale/ontologies/2024/cinema/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT (COUNT(?s) AS ?n)WHERE {
  ?s a tp:Film .
}
```
