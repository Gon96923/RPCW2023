# TPC3
- A partir do dataset "mapa-virtual.json" criar uma ontologia no Protege;
- Escrever script em Python para povoar a ontologia;
  - [Script para povoar a ontologia](https://github.com/Gon96923/RPCW2024/blob/main/TPC3/geraTTL.py)
- Carregar a ontologia no GraphDB;
  - [Ontologia criada](https://github.com/Gon96923/RPCW2024/blob/main/TPC3/mapa_virtual_out.ttl)
- Especificar as querries:
  - Quais as cidades de um determinado distrito?
  - Distribuição das cidades por distrito?
  - Quantas cidades se podem atingir a partir do Porto?
  - Quais as cidades com população acima de um determinado valor?
 
  - [Respostas às querries](https://github.com/Gon96923/RPCW2024/blob/main/TPC3/Querries.md)
 
# Dataset

Foram criadas 2 **Classes** nesta ontologia:
- Cidade
- Ligação

Foram criadas os **Object Properties**:
- temDestino: Ligação -> Cidade
- temOrigem: Cidade -> Ligação

A classe **Cidade** contém as **Data Properties**:
- cidade_descrição 
- cidade_distrito 
- cidade_id 
- cidade_nome
- cidade_população

Individuos desta classe são identificados com _cidade_id_.

A classe **Ligação** contém as **Data Properties**:
- ligação_distância
- ligação_id

Individuos desta classe são identificados com _ligação_id_.


