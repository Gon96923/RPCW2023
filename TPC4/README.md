# Criação de uma página web para a Tabela Periódica

## Ficheiros criados

No decorrer da execução deste trablho de casa foram cirados os seguintes ficheiros:
- app.py : aplicação Flask que cria o servidor web e contém todas as queries necessárias para a invocação da páginas web.
- templates/index :
- templates/empty :
- templates/elementos :
- templates/elemento :
- templates/grupos :
- templates/grupo :

//partes do elemento
```
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX : <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select DISTINCT ?types where{
    ?s owl:onProperty ?types.
}
```

//partes do grupo
```
PREFIX : <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select DISTINCT ?types where{
    ?s a :Group.
    ?s ?types ?r.
}
```
