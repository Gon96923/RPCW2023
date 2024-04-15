# Problema

O desafio é converter o dataset de XML para TTL, sendo que na ontologia deverão existir apenas duas relações entre os indivíduos: temPai e temMae.

Para tal foi escolhido o ficheiro biblia.xml.

# Ficheiros


- [biblia.xml](https://github.com/Gon96923/RPCW2024/blob/main/TPC8/biblia.xml). Ficheiro xml a converter para TTL. 
- [familia-base.ttl](https://github.com/Gon96923/RPCW2024/blob/main/TPC8/familia-base.ttl). TTL base usado para criar a ontologia final.
- [xml_to_ttl.py](https://github.com/Gon96923/RPCW2024/blob/main/TPC8/xml_to_ttl.py) Script que transforma o ficheiro xml numa ontologia TTL.
- [biblia.ttl](https://github.com/Gon96923/RPCW2024/blob/main/TPC8/biblia.ttl). Ontologia povoada final.

# Metodos

No ficheiro xml existem "tipos de individuo", person e family. 

Para povoar a ontologia iremos primeiro criar um dicionarinario 'people', o qual iremos preencher com pessoas individuais 'per', identificado pelo seu  ID e com o seu ID e nome.

Posteriormente, a cada pessoa são adicionadas as relações temPai e temMae através das 'family' identificando a familia em que se encontra como criança e associando-a ao seu pai e mãe.

