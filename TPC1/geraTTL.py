import json


text_file = open("plantas.ttl", "w",encoding='utf-8')

ttl = f"""
@prefix : <https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/> .

<https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/plantas> rdf:type owl:Ontology .

#################################################################
#    Annotation properties
#################################################################

###  http://purl.org/dc/elements/1.1/creator
<http://purl.org/dc/elements/1.1/creator> rdf:type owl:AnnotationProperty .


#################################################################
#    Object Properties
#################################################################

###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/naMorada
:naMorada rdf:type owl:ObjectProperty ;
          rdfs:domain :Planta ;
          rdfs:range :Morada ;
          <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/éDaEspécie
:éDaEspécie rdf:type owl:ObjectProperty ;
            rdfs:domain :Planta ;
            rdfs:range :Espécie ;
            <http://purl.org/dc/elements/1.1/creator> "gvale" .


#################################################################
#    Data properties
#################################################################

###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/caldeira
:caldeira rdf:type owl:DatatypeProperty ;
          rdfs:domain :Planta ;
          rdfs:range xsd:string ;
          <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/dataDeActualização
:dataDeActualização rdf:type owl:DatatypeProperty ;
                    rdfs:domain :Planta ;
                    rdfs:range xsd:string ;
                    <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/dataDePlantação
:dataDePlantação rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Planta ;
                 rdfs:range xsd:string ;
                 <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/estado
:estado rdf:type owl:DatatypeProperty ;
        rdfs:domain :Planta ;
        rdfs:range xsd:string ;
        <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/gestor
:gestor rdf:type owl:DatatypeProperty ;
        rdfs:domain :Planta ;
        rdfs:range xsd:string ;
        <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/id
:id rdf:type owl:DatatypeProperty ;
    rdfs:domain :Planta ;
    rdfs:range xsd:integer ;
    <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/implantação
:implantação rdf:type owl:DatatypeProperty ;
             rdfs:domain :Planta ;
             rdfs:range xsd:string ;
             <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/nomeCientifico
:nomeCientifico rdf:type owl:DatatypeProperty ;
                rdfs:domain :Espécie ;
                rdfs:range xsd:string ;
                <http://purl.org/dc/elements/1.1/creator> "gvale" .

###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/nomeEspécie
:nomeEspécie rdf:type owl:DatatypeProperty ;
                rdfs:domain :Espécie ;
                rdfs:range xsd:string ;
                <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/numeroDeIntervenções
:numeroDeIntervenções rdf:type owl:DatatypeProperty ;
                      rdfs:domain :Planta ;
                      rdfs:range xsd:int ;
                      <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/numeroDeRegisto
:numeroDeRegisto rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Planta ;
                 rdfs:range xsd:int ;
                 <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/origem
:origem rdf:type owl:DatatypeProperty ;
        rdfs:domain :Planta ;
        rdfs:range xsd:string ;
        <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/tutor
:tutor rdf:type owl:DatatypeProperty ;
       rdfs:domain :Planta ;
       rdfs:range xsd:string ;
       <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/plantas#codigoDeRua
:codigoDeRua rdf:type owl:DatatypeProperty ;
             rdfs:domain :Morada ;
             rdfs:range xsd:int ;
             <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/plantas#freguesia
:freguesia rdf:type owl:DatatypeProperty ;
           rdfs:domain :Morada ;
           rdfs:range xsd:string ;
           <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/plantas#local
:local rdf:type owl:DatatypeProperty ;
       rdfs:domain :Morada ;
       rdfs:range xsd:string ;
       <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/plantas#rua
:rua rdf:type owl:DatatypeProperty ;
     rdfs:domain :Morada ;
     rdfs:range xsd:string ;
     <http://purl.org/dc/elements/1.1/creator> "gvale" .


#################################################################
#    Classes
#################################################################

###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/Espécie
:Espécie rdf:type owl:Class ;
         <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/Morada
:Morada rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/1/untitled-ontology-9/Planta
:Planta rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "gvale" .


#################################################################
#    Individuals
#################################################################

"""

text_file.write(ttl)

with open('plantas.json', encoding='utf-8') as f:
    datab = json.load(f)

    for planta in datab:
        registo = f"""


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/plantas#{planta['Espécie'].replace(" ","_")}
:{planta['Espécie'].replace(" ","_")} rdf:type owl:NamedIndividual ,
                         :Espécie ;
                :nomeEspécie "{planta['Espécie'].replace(" ","_")}" ;
                :nomeCientifico "{planta['Nome Científico'].replace(" ","_")}" ;
                <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/plantas#{planta['Local'].replace(" ","_").replace('"',"")}_{planta['Código de rua']}
<https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/plantas#{planta['Local'].replace(" ","_").replace('"',"")}_{planta['Código de rua']}> rdf:type owl:NamedIndividual ,
                                                                                 :Morada ;
                                                                        :codigoDeRua "{planta['Código de rua']}"^^xsd:int ;
                                                                        :freguesia "{planta['Freguesia'].replace(" ","_").replace('"',"")}" ;
                                                                        :local "{planta['Local'].replace(" ","_").replace('"',"")}" ;
                                                                        :rua "{planta['Rua'].replace(" ","_").replace('"',"")}" ;
                                                                        <http://purl.org/dc/elements/1.1/creator> "gvale" .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/plantas#{planta['Id']}
<https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/plantas#{planta['Id']}> rdf:type owl:NamedIndividual ,
                                                                                  :Planta ;
                                                                         :naMorada "{planta['Código de rua']}"^^xsd:int ;
                                                                         :éDaEspécie :{planta['Espécie'].replace(" ","_")} ;
                                                                         :caldeira "{planta['Caldeira'].replace(" ","_")}" ;
                                                                         :dataDeActualização "{planta['Data de actualização'].replace(" ","_")}" ;
                                                                         :dataDePlantação "{planta['Data de Plantação'].replace(" ","_")}" ;
                                                                         :estado "{planta['Estado'].replace(" ","_")}" ;
                                                                         :gestor "{planta['Gestor'].replace(" ","_")}" ;
                                                                         :id {planta['Id']} ;
                                                                         :implantação "{planta['Implantação'].replace(" ","_")}" ;
                                                                         :numeroDeIntervenções "{planta['Número de intervenções']}"^^xsd:int ;
                                                                         :numeroDeRegisto "{planta['Número de Registo']}"^^xsd:int ;
                                                                         :origem "{planta['Origem'].replace(" ","_")}" ;
                                                                         :tutor "{planta['Tutor'].replace(" ","_")}" ;
                                                                         <http://purl.org/dc/elements/1.1/creator> "gvale" .
        


"""
        text_file.write(registo)

text_file.write("###  Generated by the OWL API (version 4.5.26.2023-07-17T20:34:13Z) https://github.com/owlcs/owlapi")

text_file.close()