import json


text_file = open("avalia_out.ttl", "w",encoding='utf-8')


ttl = f"""
@prefix : <http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/> .

<http://www.semanticweb.org/gvale/ontologies/2024/3/avalia> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#cursoDe
:cursoDe rdf:type owl:ObjectProperty ;
         owl:inverseOf :inCurso .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#exameDe
:exameDe rdf:type owl:ObjectProperty ;
         owl:inverseOf :hasExame .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#hasExame
:hasExame rdf:type owl:ObjectProperty ;
          rdfs:domain :Aluno ;
          rdfs:range :Exame .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#hasProjeto
:hasProjeto rdf:type owl:ObjectProperty ;
            owl:inverseOf :projetoDe ;
            rdfs:domain :Aluno ;
            rdfs:range :Projeto .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#hasTPC
:hasTPC rdf:type owl:ObjectProperty ;
        owl:inverseOf :tpcDe ;
        rdfs:domain :Aluno ;
        rdfs:range :TPC .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#inCurso
:inCurso rdf:type owl:ObjectProperty ;
         rdfs:domain :Aluno ;
         rdfs:range :Curso .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#projetoDe
:projetoDe rdf:type owl:ObjectProperty .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#tpcDe
:tpcDe rdf:type owl:ObjectProperty .


#################################################################
#    Data properties
#################################################################

###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#alunoId
:alunoId rdf:type owl:DatatypeProperty ;
         rdfs:domain :Aluno .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#alunoNome
:alunoNome rdf:type owl:DatatypeProperty ;
           rdfs:domain :Aluno .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#cursoNome
:cursoNome rdf:type owl:DatatypeProperty ;
           rdfs:domain :Curso .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#exameNota
:exameNota rdf:type owl:DatatypeProperty ,
                    owl:FunctionalProperty ;
           rdfs:domain :Exame .
        
###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#exameTipo
:exameTipo rdf:type owl:DatatypeProperty ,
                    owl:FunctionalProperty ;
           rdfs:domain :Exame .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#projetoNota
:projetoNota rdf:type owl:DatatypeProperty ;
             rdfs:domain :Projeto .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#tpcNota
:tpcNota rdf:type owl:DatatypeProperty ;
         rdfs:domain :TPC .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#tpcTp
:tpcTp rdf:type owl:DatatypeProperty ;
       rdfs:domain :TPC .


#################################################################
#    Classes
#################################################################

###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#Curso
:Curso rdf:type owl:Class .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/Aluno
:Aluno rdf:type owl:Class .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/Exame
:Exame rdf:type owl:Class .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/Projeto
:Projeto rdf:type owl:Class .


###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/TPC
:TPC rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################


"""

text_file.write(ttl)

with open('aval-alunos.json', encoding='utf-8') as f:
    datab = json.load(f)


    for aluno in datab['alunos']:
        registo = f"""

###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#{aluno['idAluno']}
:{aluno['idAluno']} rdf:type owl:NamedIndividual ,
                 :Aluno ;
        :hasProjeto :{aluno['idAluno']}_proj;
        :inCurso :{aluno['curso']} ;
        :alunoId "{aluno['idAluno']}" ;
        :alunoNome "{aluno['nome']}" .

"""
        text_file.write(registo)

        registoP = f"""
###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#{aluno['idAluno']}_proj
:{aluno['idAluno']}_proj rdf:type owl:NamedIndividual ,
                      :Projeto ;
             :projetoNota {aluno['projeto']} .
        """
        text_file.write(registoP)

        registoC = f"""
###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#{aluno['curso']}
:{aluno['curso']} rdf:type owl:NamedIndividual ,
              :Curso ;
     :cursoNome "{aluno['curso']}" .
        """
        text_file.write(registoC)

        for exame,nota in aluno['exames'].items():
            registoE = f"""
###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#{aluno['idAluno']}_{exame}
:{aluno['idAluno']}_{exame} rdf:type owl:NamedIndividual ,
                          :Exame ;
                 :exameDe :{aluno['idAluno']} ;
                 :exameTipo "{exame}" ;
                 :exameNota {nota} .
            """
            text_file.write(registoE)
        
        for tpc in aluno['tpc']:
            registoT = f"""
###  http://www.semanticweb.org/gvale/ontologies/2024/3/avalia#{aluno['idAluno']}_{tpc['tp']}
:{aluno['idAluno']}_{tpc['tp']} rdf:type owl:NamedIndividual ,
                      :TPC ;
             :tpcDe :{aluno['idAluno']} ;
             :tpcNota {tpc['nota']} ;
             :tpcTp "{tpc['tp']}" .
            """
            text_file.write(registoT)




ttl2 = f"""

###  Generated by the OWL API (version 4.5.26.2023-07-17T20:34:13Z) https://github.com/owlcs/owlapi

"""
text_file.write(ttl2)

text_file.close()