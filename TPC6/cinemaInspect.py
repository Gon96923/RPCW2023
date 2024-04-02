import json
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, OWL

g = Graph()
g.parse("cinema.ttl")

with open("mov.json", "r", encoding='UTF-8') as f:
    data = json.load(f)
    f.close()

cinema = Namespace("http://www.semanticweb.org/gvale/ontologies/2024/cinema/")

for filme in data:
    f_uri = URIRef(f"{cinema}{filme['uri'].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?").replace("%","")}")
    g.add((f_uri,RDF.type,cinema.Film))
    if filme["Titulo"] != [] :
        g.add((f_uri,cinema.title,Literal(filme["Titulo"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?"))))
    else:
        g.add((f_uri,cinema.title,Literal("")))
    g.add((f_uri,cinema.description,Literal(filme["Resumo"].replace("%22","'").replace("%25","%").replace("%3F","?"))))

    for actor in filme["Elenco"]:
        uri = URIRef(f"{cinema}{actor["uri"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?").replace("%","")}")
        name = actor["Name"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?")
        bd = actor["birthDate"]
        g.add((uri,RDF.type,cinema.Actor))
        g.add((uri,cinema.name,Literal(name)))
        g.add((uri,cinema.birthDate,Literal(bd)))
        g.add((f_uri,cinema.hasActor,uri))

    for realizador in filme["Realizadores"]:
        uri = URIRef(f"{cinema}{realizador["uri"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?").replace("%","")}")
        name = realizador["Name"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?")
        bd = realizador["birthDate"]
        g.add((uri,RDF.type,cinema.Director))        
        g.add((uri,cinema.name,Literal(name)))
        g.add((uri,cinema.birthDate,Literal(bd)))
        g.add((f_uri,cinema.hasDirector,uri))
    
    for escritor in filme["Escritores"]:
        uri = URIRef(f"{cinema}{escritor["uri"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?").replace("%","")}")
        name = escritor["Name"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?")
        bd = escritor["birthDate"]
        g.add((uri,RDF.type,cinema.Writer))
        g.add((uri,cinema.name,Literal(name)))
        g.add((uri,cinema.birthDate,Literal(bd)))
        g.add((f_uri,cinema.hasWriter,uri))

    for musico in filme["Músicos"]:
        uri = URIRef(f"{cinema}{musico["uri"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?").replace("%","")}")
        name = musico["Name"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?")
        bd = musico["birthDate"]
        g.add((uri,RDF.type,cinema.Musician))
        g.add((uri,cinema.name,Literal(name)))
        g.add((uri,cinema.birthDate,Literal(bd)))
        g.add((f_uri,cinema.hasComposer,uri))
    
    for musica in filme["Músicas"]:
        uri = URIRef(f"{cinema}{musica["Name"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?").replace("%","")}")
        g.add((uri,RDF.type,cinema.Music))
        g.add((f_uri,cinema.hasMusic,uri))
    
    for argumentista in filme["Argumentistas"]:
        uri = URIRef(f"{cinema}{argumentista["uri"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?").replace("%","")}")
        name = argumentista["Name"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?")
        bd = argumentista["birthDate"]
        g.add((uri,RDF.type,cinema.Screenwriter))
        g.add((uri,cinema.name,Literal(name)))
        g.add((uri,cinema.birthDate,Literal(bd)))
        g.add((f_uri,cinema.hasScreenwriter,uri))
    
    for produtor in filme["Produtores"]:
        uri = URIRef(f"{cinema}{produtor["uri"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?").replace("%","")}")
        name = produtor["Name"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?")
        bd = produtor["birthDate"]
        g.add((uri,RDF.type,cinema.Producer))
        g.add((uri,cinema.name,Literal(name)))
        g.add((uri,cinema.birthDate,Literal(bd)))
        g.add((f_uri,cinema.hasProducer,uri))

    if filme["Lançamento"] != [] :
        uri = URIRef(f"{cinema}{filme["Lançamento"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?").replace("%","")}")
        g.add((uri,RDF.type,cinema.Release))
        g.add((f_uri,cinema.hasRelease,uri))

    
    
    for genero in filme["Géneros"]:
        uri = URIRef(f"{cinema}{genero["Name"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?").replace("%","")}")
        g.add((uri,RDF.type,cinema.Genre))
        g.add((f_uri,cinema.hasGenre,uri))
    
    for livro in filme["Livros"]:
        uri = URIRef(f"{cinema}{livro["Name"].replace(" ","_").replace("%22","'").replace("%25","%").replace("%3F","?").replace("%","")}")
        g.add((uri,RDF.type,cinema.Book))
        g.add((f_uri,cinema.hasBook,uri))



import pprint


print(len(g))
f = open('cinema_pg53849.ttl', 'wb')
f.write(g.serialize().encode('UTF-8'))
print("=====================================")
