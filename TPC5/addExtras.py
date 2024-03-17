import requests
import json



# Define the DBpedia SPARQL endpoint
sparql_endpoint = "http://dbpedia.org/sparql"
    
headers = {
    "Accept": "application/sparql-results+json"
}


    
f = open("filmes.json", "r", encoding='UTF-8')
filmes = json.load(f)
f.close()

atores = []

for filme in filmes:
    #print(filme['Titulo'])
    sparql_queryAtores = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select distinct ?s ?label ?bd ?dd where {{
    <{filme["uri"]}> dbo:starring ?s.
    optional{{
        ?s rdfs:label ?label
        filter(lang(?label)="en").
        }}
    optional{{?s dbo:birthDate ?bd.}}
    optional{{?s dbo:deathDate ?dd.}}
    
}}
"""
    sparql_queryD = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select distinct ?s where {{
    <{filme["uri"]}> dbo:director ?s.
}}
"""
    
    sparql_queryW = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select distinct ?s where {{
    <{filme["uri"]}> dbo:writer ?s.
}}
"""
    
    sparql_queryM = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select distinct ?s where {{
    <{filme["uri"]}> dbo:musicComposer ?s.
}}
"""


    # Define the parameters
    params = {
        "query": sparql_queryAtores,
        "format": "json"
    }

    response = requests.get(sparql_endpoint, params=params, headers=headers)

    if response.status_code == 200:
        results = response.json()
        filme["Elenco"] = []
        
        for result in results["results"]["bindings"]:
            actor = {}
            actor["uri"] = result["s"]["value"]
            if "label" in result.keys():
                actor["Nome"] = result["label"]["value"]
            if "bd" in result.keys():
                actor["Data de Nascimento"] = result["bd"]["value"]
            if "dd" in result.keys(): 
                actor["Data de Óbito"] = result["dd"]["value"]

            atores.append(actor)
            filme['Elenco'].append(actor['uri'])
    else:
        print("Error:", response.status_code)
        print(response.text)

    # Define the parameters
    params = {
        "query": sparql_queryD,
        "format": "json"
    }

    response = requests.get(sparql_endpoint, params=params, headers=headers)

    if response.status_code == 200:
        results = response.json()
        filme["Realizadores"] = []
        
        for result in results["results"]["bindings"]:
            actor = {}
            actor["uri"] = result["s"]["value"]

            filme['Realizadores'].append(actor['uri'])
    else:
        print("Error:", response.status_code)
        print(response.text)

    # Define the parameters
    params = {
        "query": sparql_queryW,
        "format": "json"
    }
    
    response = requests.get(sparql_endpoint, params=params, headers=headers)

    if response.status_code == 200:
        results = response.json()
        filme["Escritores"] = []
        
        for result in results["results"]["bindings"]:
            actor = {}
            actor["uri"] = result["s"]["value"]

            filme['Escritores'].append(actor['uri'])
    else:
        print("Error:", response.status_code)
        print(response.text)

    # Define the parameters
    params = {
        "query": sparql_queryM,
        "format": "json"
    }
    
    response = requests.get(sparql_endpoint, params=params, headers=headers)

    if response.status_code == 200:
        results = response.json()
        filme["Músicos"] = []
        
        for result in results["results"]["bindings"]:
            actor = {}
            actor["uri"] = result["s"]["value"]

            filme['Músicos'].append(actor['uri'])
    else:
        print("Error:", response.status_code)
        print(response.text)


f = open("filmes.json", "w", encoding='UTF-8')
json.dump(filmes, f, ensure_ascii=False)
f.close()  

f = open("atores.json", "w", encoding='UTF-8')
json.dump(atores, f, ensure_ascii=False)
f.close()  

f = open("atores.json", "r", encoding='UTF-8')
atores = json.load(f)
f.close()    

for actor in atores:
    #print(filme['Titulo'])
    sparql_queryFilmes = f"""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select distinct ?s where {{
    ?s dbo:starring <{actor["uri"]}>.
}}
"""
    # Define the headers
    headersFilmes = {
        "Accept": "application/sparql-results+json"
    }

    # Define the parameters
    paramsFilmes = {
        "query": sparql_queryFilmes,
        "format": "json"
    }

    response = requests.get(sparql_endpoint, params=paramsFilmes, headers=headersFilmes)

    if response.status_code == 200:
        results = response.json()
        actor["Filmes"] = []
        

        for result in results["results"]["bindings"]:
            filme = {}
            filme["uri"] = result["s"]["value"]

            actor['Filmes'].append(filme['uri'])
             

    else:
        print("Error:", response.status_code)
        print(response.text)

f = open("atores.json", "w", encoding='UTF-8')
json.dump(atores, f, ensure_ascii=False)
f.close()
