import json


text_file = open("mapa_virtual_out.ttl", "w",encoding='utf-8')


ttl = f"""
@prefix : <https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual/> .

<https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual#temDestino
:temDestino rdf:type owl:ObjectProperty ;
            rdfs:domain :Ligação ;
            rdfs:range :Cidade .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual#temOrigem
:temOrigem rdf:type owl:ObjectProperty ;
           rdfs:domain :Ligação ;
           rdfs:range :Cidade .


#################################################################
#    Data properties
#################################################################

###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual#cidade_descrição
:cidade_descrição rdf:type owl:DatatypeProperty ;
                  rdfs:domain :Cidade ;
                  rdfs:range xsd:string .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual#cidade_distrito
:cidade_distrito rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Cidade ;
                 rdfs:range xsd:string .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual#cidade_id
:cidade_id rdf:type owl:DatatypeProperty ;
           rdfs:domain :Cidade ;
           rdfs:range xsd:string .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual#cidade_nome
:cidade_nome rdf:type owl:DatatypeProperty ;
             rdfs:domain :Cidade ;
             rdfs:range xsd:string .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual#cidade_população
:cidade_população rdf:type owl:DatatypeProperty ;
                  rdfs:domain :Cidade ;
                  rdfs:range xsd:integer .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual#ligação_distância
:ligação_distância rdf:type owl:DatatypeProperty ;
                   rdfs:domain :Ligação ;
                   rdfs:range xsd:float .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual#ligação_id
:ligação_id rdf:type owl:DatatypeProperty ;
            rdfs:domain :Ligação ;
            rdfs:range xsd:string .


#################################################################
#    Classes
#################################################################

###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual#Cidade
:Cidade rdf:type owl:Class .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual#Ligação
:Ligação rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################

"""

text_file.write(ttl)

with open('mapa-virtual.json', encoding='utf-8') as f:
    datab = json.load(f)


    for cidade in datab['cidades']:
        registo = f"""

###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual#{cidade['id']}
:{cidade['id']} rdf:type owl:NamedIndividual ,
              :Cidade ;
     :cidade_descrição "{cidade['descrição']}" ;
     :cidade_distrito "{cidade['distrito']}" ;
     :cidade_id "{cidade['id']}" ;
     :cidade_nome "{cidade['nome']}" ;
     :cidade_população {cidade['população']} .


"""
        text_file.write(registo)


    for ligacao in datab['ligacoes']:
        registo = f"""

###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual#{ligacao['id']}
<https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/mapa_virtual#{ligacao['id']}> rdf:type owl:NamedIndividual ,
                                                                                      :Ligação ;
                                                                             :temDestino :{ligacao['destino']} ;
                                                                             :temOrigem :{ligacao['origem']} ;
                                                                             :ligação_distância "{ligacao['distância']}"^^xsd:float ;
                                                                             :ligação_id "{ligacao['id']}" .

"""
        text_file.write(registo)


ttl2 = f"""

###  Generated by the OWL API (version 4.5.26.2023-07-17T20:34:13Z) https://github.com/owlcs/owlapi

"""
text_file.write(ttl2)

text_file.close()