# Problema

Com base na base de dados contido no ficheiro \<planta.json>\, crie uma ontologia utilizando a ferramenta _Protegé_.

# Estratégias

Uma vez que certos caracteres não são reconhecidos pela ferramenta Protegé, substituí o caracter ' ' pelo caracter '_' e o caracter '"' é eliminado, utilizando o comando replace.

Foram criadas 3 **Classes** nesta ontologia:
- Planta
- Espécie
- Morada

Foram criadas os **Object Properties**:
- naMorada: Planta -> Morada
- éDaEspécie: Planta -> Espécie

A classe **Planta** contém as **Data Properties**:
- caldeira
- dataDeActualização
- dataDePlantação
- estado
- gestor
- id
- implantação
- numeroDeIntervenções
- numeroDeRegisto
- origem
- tutor

Individuos desta classe são identificados com _id_.

A classe **Morada** contém as **Data Properties**:
- codigoDeRua
- freguesia
- local
- rua

Individuos desta classe são identificados com _local_codigoDeRua_, uma vez que foram encontrados casos em que o mesmo _codigoDeRua_ se refeira a multiplas moradas.

A classe **Espécie** contém as **Data Properties**:
- nomeCientifico
- nomeEspécie

Individuos desta classe são identificados com _nomeEspécie_.

# Resultado

![graph](https://github.com/Gon96923/RPCW2024/blob/main/TPC1/graphPrint.png)

De forma a representar a ontologia de uma forma fácil de entender foi utilizada a ferramenta **WebVOWL**: 
https://service.tib.eu/webvowl
