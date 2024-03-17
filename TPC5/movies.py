import requests
import json



# Define the DBpedia SPARQL endpoint
sparql_endpoint = "http://dbpedia.org/sparql"

# Define the SPARQL query
sparql_query = """
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select distinct ?s ?label ?time where {
    ?s a dbo:Film.
    optional{
        ?s rdfs:label ?label.
        filter(lang(?label)="en").
    }
    optional{?s dbo:runtime ?time .}    
}
"""

# Define the headers
headers = {
    "Accept": "application/sparql-results+json"
}

# Define the parameters
params = {
    "query": sparql_query,
    "format": "json"
}

# Send the SPARQL query using requests
response = requests.get(sparql_endpoint, params=params, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    results = response.json()
    filmesl = []

    for result in results["results"]["bindings"]:
        movie = {}
        movie["uri"] = result["s"]["value"]
        if "label" in result.keys():
            movie["Titulo"] = result["label"]["value"]
        if "time" in result.keys():
            movie["Duracao"] = result["time"]["value"]
            if float(result["time"]["value"]) <= 2400:
                movie["Tipo"] = "Curta metragem"

        filmesl.append(movie)

    f = open("filmes.json", "w", encoding='UTF-8')
    json.dump(filmesl, f, ensure_ascii=False)
    f.close()
        
else:
    print("Error:", response.status_code)
    print(response.text)
