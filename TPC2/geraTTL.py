import json


text_file = open("escolaMusica.ttl", "w",encoding='utf-8')


ttl = f"""
@prefix : <https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica/> .

<https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#ensinaInstrumento
:ensinaInstrumento rdf:type owl:ObjectProperty ;
                   rdfs:domain :Curso ;
                   rdfs:range :Instrumento .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#noCurso
:noCurso rdf:type owl:ObjectProperty ;
         rdfs:domain :Aluno ;
         rdfs:range :Curso .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#tocaInstrumento
:tocaInstrumento rdf:type owl:ObjectProperty ;
                 rdfs:domain :Aluno ;
                 rdfs:range :Instrumento .


#################################################################
#    Data properties
#################################################################

###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#alunoAnoCurso
:alunoAnoCurso rdf:type owl:DatatypeProperty ;
               rdfs:domain :Aluno ;
               rdfs:range xsd:int .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#alunoDataDeNascimento
:alunoDataDeNascimento rdf:type owl:DatatypeProperty ;
                       rdfs:domain :Aluno ;
                       rdfs:range xsd:string .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#alunoId
:alunoId rdf:type owl:DatatypeProperty ;
         rdfs:domain :Aluno ;
         rdfs:range xsd:string .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#alunoNome
:alunoNome rdf:type owl:DatatypeProperty ;
           rdfs:domain :Aluno ;
           rdfs:range xsd:string .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#cursoDesignacao
:cursoDesignacao rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Curso ;
                 rdfs:range xsd:string .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#cursoDuracao
:cursoDuracao rdf:type owl:DatatypeProperty ;
              rdfs:domain :Curso ;
              rdfs:range xsd:int .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#cursoId
:cursoId rdf:type owl:DatatypeProperty ;
         rdfs:domain :Curso ;
         rdfs:range xsd:string .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#cursoInstrumento
:cursoInstrumento rdf:type owl:DatatypeProperty ;
                  rdfs:domain :Curso ;
                  rdfs:range xsd:string .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#instrumentoId
:instrumentoId rdf:type owl:DatatypeProperty ;
               rdfs:domain :Instrumento ;
               rdfs:range xsd:string .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#instrumentoNome
:instrumentoNome rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Instrumento ;
                 rdfs:range xsd:string .


#################################################################
#    Classes
#################################################################

###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#Aluno
:Aluno rdf:type owl:Class .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#Curso
:Curso rdf:type owl:Class .


###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#Instrumento
:Instrumento rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################

"""

text_file.write(ttl)

with open('db.json', encoding='utf-8') as f:
    datab = json.load(f)


    for aluno in datab['alunos']:
        registo = f"""

###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#{aluno['id']}
:{aluno['id']} rdf:type owl:NamedIndividual ,
                :Aluno ;
       :noCurso :{aluno['curso']} ;
       :tocaInstrumento :{aluno['instrumento'].replace(" ", "_")} ;
       :alunoAnoCurso {aluno['anoCurso']} ;
       :alunoDataDeNascimento "{aluno['dataNasc']}" ;
       :alunoId "{aluno['id']}" ;
       :alunoNome "{aluno['nome']}" .

"""
        text_file.write(registo)


    for curso in datab['cursos']:
        registo = f"""

###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#{curso['id']}
:{curso['id']} rdf:type owl:NamedIndividual ,
              :Curso ;
     :ensinaInstrumento :{curso['instrumento']['#text'].replace(" ", "_")} ;
     :cursoDesignacao "{curso['designacao']}" ;
     :cursoDuracao {curso['duracao']} ;
     :cursoId "{curso['id']}" .

"""
        text_file.write(registo)


    for instrumento in datab['instrumentos']:
        registo = f"""

###  https://epl.di.uminho.pt/~jcr/AULAS/RPCW2024/datasets/2024/escola_de_musica#{instrumento['#text'].replace(" ", "_")}
:{instrumento['#text'].replace(" ", "_")} rdf:type owl:NamedIndividual ,
                   :Instrumento ;
          :instrumentoId "{instrumento['id']}" ;
          :instrumentoNome "{instrumento['#text']}" .

"""
        text_file.write(registo)

ttl2 = f"""


#################################################################
#    General axioms
#################################################################

[ rdf:type owl:AllDisjointClasses ;
  owl:members ( :Aluno
                :Curso
                :Instrumento
              )
] .


###  Generated by the OWL API (version 4.5.26.2023-07-17T20:34:13Z) https://github.com/owlcs/owlapi

"""
text_file.write(ttl2)

text_file.close()