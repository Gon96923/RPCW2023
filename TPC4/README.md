# Criação de uma página web para a Tabela Periódica

## Ficheiros criados

No decorrer da execução deste trablho de casa foram cirados os seguintes ficheiros:
- app.py : aplicação Flask que cria o servidor web e contém todas as queries necessárias para a invocação da páginas web.
- templates/index : template html para criar a página web inicial.
- templates/empty : template html para criar a página web inicial.
- templates/elementos : template html para criar a página web contendo todos os elementos da Tabela Periódica.
- templates/elemento : template html para criar a página web contendo a informção referente a um dado elemento.
- templates/grupos : template html para criar a página web contendo todos os grupos da Tabela Periódica.
- templates/grupo : template html para criar a página web contendo a informção referente a um dado grupo.

## Queries auxiliares

Querie utilizada para descobrir os types dos elementos e preencher a página web da informação de cada elemnto.
```ruby
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX : <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select DISTINCT ?types where{
    ?s owl:onProperty ?types.
}
```

Querie utilizada para descobrir os types dos elementos e preencher a página web da informação de cada grupo.
```
PREFIX : <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select DISTINCT ?types where{
    ?s a :Group.
    ?s ?types ?r.
}
```
