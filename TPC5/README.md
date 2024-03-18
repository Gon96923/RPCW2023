# Problema

Construir um dataset, em formato json, sobre cinema, com ajuda da dbpedia.

# Solução

Através de diveresas queries SPARQL foi adquirida uma lista com todos os filmes presentes na dbpedia, assim como as seguintes informações sobre cada um:
- uri
- Titulo
- Duração
- Tipo(caso se trate de uma curta metragem) 
- Escritores (uri)
- Realizadores (uri)
- Músicos (uri)
- Argumentistas (uri)
- Elenco
  - Ator (uri)
  - uri
  - Filmes em que atuou(uri)

# Ficheiros

- [movies.py](https://github.com/Gon96923/RPCW2024/blob/main/TPC5/movies.py) lista todos os filmes (uri,titulo e duração) no ficheiro [filmes.json](https://github.com/Gon96923/RPCW2024/blob/main/TPC5/filmes.json).
- [addExtras.py](https://github.com/Gon96923/RPCW2024/blob/main/TPC5/addExtras.py) adiciona os escritores, realizadores, músicos, argumentistas e elenco ao ficheiro [filmes.json](https://github.com/Gon96923/RPCW2024/blob/main/TPC5/filmes.json).
- [filmes.json](https://github.com/Gon96923/RPCW2024/blob/main/TPC5/filmes.json) dataset resultante.
