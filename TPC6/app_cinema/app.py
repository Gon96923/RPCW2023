from flask import Flask,render_template,url_for
from datetime import datetime
import requests

app = Flask(__name__)

#dat do sistema no formato ISO
data_hora_atual = datetime.now()
data_iso_formatada = data_hora_atual.strftime('%Y-%m-%dT%H:%M:%S')

# GraphDB endpoint
graphdb_endpoint = "http://epl.di.uminho.pt:7200/repositories/cinema2024"

#pedido/rota atendido pela aplicação
@app.route('/')
def index():
    return render_template('index.html', data = {"data": data_iso_formatada}) #linha 21 no index.html



@app.route('/filmes')
def filmes():
    sparql_query = """
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where{
    ?s a tp:Film ;
        tp:title ?title .
}
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('filmes.html', data = dados)
    else:
        return render_template('empty.html',data = data_iso_formatada)



@app.route('/filmes/<nome>')
def filme(nome):
    sparql_query = f'''
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where {{
    ?s a tp:Film .
    ?s tp:title "{nome}" .
    optional {{ ?s tp:duration ?dur . }} 
    optional {{ ?s tp:hasActor ?actor . }} 
    optional {{ ?s tp:hasCountry ?coun . }}
    optional {{ ?s tp:hasDirector ?dir .}}  
    optional {{ ?s tp:hasScreenwriter ?scwr . }} 
    optional {{ ?s tp:hasGenre ?gen . }} 
    optional {{ ?s tp:hasMusic ?mus . }}
    optional {{ ?s tp:hasComposer ?comp . }}
    optional {{ ?s tp:hasProducer ?pr . }}
    optional {{ ?s tp:hasWriter ?wr . }}
    optional {{ ?s tp:date ?date . }}
    optional {{ ?s tp:hasBook ?book . }}
    optional {{ ?s tp:description ?description .
    
}}
'''

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        dic = {
            'title': nome,
            'duracao': [],
            'actor': [],
            'coun': [],
            'dir': [],
            'scwr': [],
            'gen': [],
            'mus': [],
            'pr': [],
            'wr': [],
            'date': [],
            'book': [],
            'comp': [],
            'description': []
        }

        for d in dados:
            if 'dur' in d:
                dic['duracao'] = d['dur']['value']
            if 'date' in d:
                dic['date'] = d['date']['value']
            if 'actor' in d and d['actor']['value'] not in dic['actor']:
                dic['actor'].append(d['actor']['value'])
            if 'coun' in d and d['coun']['value'] not in dic['coun']:
                dic['coun'].append(d['coun']['value'])
            if 'dir' in d and d['dir']['value'] not in dic['dir']:
                dic['dir'].append(d['dir']['value'])
            if 'scwr' in d and d['scwr']['value'] not in dic['scwr']:
                dic['scwr'].append(d['scwr']['value'])
            if 'gen' in d and d['gen']['value'] not in dic['gen']:
                dic['gen'].append(d['gen']['value'])
            if 'mus' in d and d['mus']['value'] not in dic['mus']:
                dic['mus'].append(d['mus']['value'])
            if 'pr' in d and d['pr']['value'] not in dic['pr']:
                dic['pr'].append(d['pr']['value'])
            if 'wr' in d and d['wr']['value'] not in dic['wr']:
                dic['wr'].append(d['wr']['value'])
            if 'book' in d and d['book']['value'] not in dic['book']:
                dic['book'].append(d['book']['value'])
            if 'comp' in d and d['comp']['value'] not in dic['mus']:
                dic['comp'].append(d['comp']['value'])
            if 'description' in d and d['description']['value'] not in dic['description']:
                dic['description'] = d['description']['value']

        
        return render_template('filme.html', data = dic)
    else:
        return render_template('empty.html',data = data_iso_formatada)


@app.route('/actors')
def actors():
    sparql_query = """
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where{
    ?s a tp:Actor ;
        tp:name ?name ;
        tp:birthDate ?birthDate.
}
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('actors.html', data = dados)
    else:
        return render_template('empty.html',data = data_iso_formatada)
    
@app.route('/actors/<nome>')
def actor(nome):
    sparql_query = f"""
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where{{
    ?s a tp:Actor ;
        tp:name "{nome}" ;
        tp:birthDate ?birthDate.
    ?s tp:acted ?film.
    ?film tp:title ?title.

}}
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']

        list = []

        for d in dados:
            date = d['birthDate']['value']
            if 'film' in d:
                list.append(d['title']['value'])
        return render_template('actor.html', date = date,list = list,nome = nome)
    else:
        return render_template('empty.html',data = data_iso_formatada)

@app.route('/directors')
def directors():
    sparql_query = """
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where{
    ?s a tp:Director ;
        tp:name ?name ;
        tp:birthDate ?birthDate.
        
}
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('directors.html', data = dados)
    else:
        return render_template('empty.html',data = data_iso_formatada)

@app.route('/directors/<nome>')
def director(nome):
    sparql_query = f"""
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where{{
    ?s a tp:Director ;
        tp:name "{nome}" ;
        tp:birthDate ?birthDate.
    ?s tp:directed ?film.
    ?film tp:title ?title.
}}
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']

        list = []

        for d in dados:
            date = d['birthDate']['value']
            if 'film' in d:
                list.append(d['title']['value'])
        return render_template('director.html', date = date,list = list,nome = nome)
    else:
        return render_template('empty.html',data = data_iso_formatada)

@app.route('/screenwriters')
def screenwriters():
    sparql_query = """
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where{
    ?s a tp:Screenwriter ;
        tp:name ?name ;
        tp:birthDate ?birthDate.
}
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('screenwriters.html', data = dados)
    else:
        return render_template('empty.html',data = data_iso_formatada)

@app.route('/screenwriters/<nome>')
def screenwriter(nome):
    sparql_query = f"""
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where{{
    ?s a tp:Screenwriter ;
        tp:name "{nome}" ;
        tp:birthDate ?birthDate.
    ?s tp:screenwrited ?film.
    ?film tp:title ?title.
}}
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']

        list = []

        for d in dados:
            date = d['birthDate']['value']
            if 'film' in d:
                list.append(d['title']['value'])
        return render_template('screenwriter.html', date = date,list = list,nome = nome)
    else:
        return render_template('empty.html',data = data_iso_formatada)
    
@app.route('/musicians')
def musicians():
    sparql_query = """
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where{
    ?s a tp:Musician ;
        tp:name ?name ;
        tp:birthDate ?birthDate.
}
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('musicians.html', data = dados)
    else:
        return render_template('empty.html',data = data_iso_formatada)

@app.route('/musicians/<nome>')
def musician(nome):
    sparql_query = f"""
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where{{
    ?s a tp:Musician ;
        tp:name "{nome}" ;
        tp:birthDate ?birthDate.
    ?s tp:composed ?film.
    ?film tp:title ?title.
}}
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']

        list = []

        for d in dados:
            date = d['birthDate']['value']
            if 'film' in d:
                list.append(d['title']['value'])
        return render_template('musician.html', date = date,list = list,nome = nome)
    else:
        return render_template('empty.html',data = data_iso_formatada)
    
@app.route('/producers')
def producers():
    sparql_query = """
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where{
    ?s a tp:Producer ;
        tp:name ?name ;
        tp:birthDate ?birthDate.
}
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('producers.html', data = dados)
    else:
        return render_template('empty.html',data = data_iso_formatada)

@app.route('/producers/<nome>')
def producer(nome):
    sparql_query = f"""
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where{{
    ?s a tp:Producer ;
        tp:name "{nome}" ;
        tp:birthDate ?birthDate.
    ?s tp:produced ?film.
    ?film tp:title ?title.
}}
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']

        list = []

        for d in dados:
            date = d['birthDate']['value']
            if 'film' in d:
                list.append(d['title']['value'])
        return render_template('producer.html', date = date,list = list,nome = nome)
    else:
        return render_template('empty.html',data = data_iso_formatada)
    
@app.route('/writers')
def writers():
    sparql_query = """
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where{
    ?s a tp:Writer ;
        tp:name ?name ;
        tp:birthDate ?birthDate.
}
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('writers.html', data = dados)
    else:
        return render_template('empty.html',data = data_iso_formatada)

@app.route('/writers/<nome>')
def writer(nome):
    sparql_query = f"""
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where{{
    ?film a tp:Film .
    ?film tp:hasWriter ?wr .
    ?wr tp:name "{nome}" .
    ?wr tp:birthDate ?date.
    ?film tp:title ?title.
}}
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']

        list = []
        date = ''

        for d in dados:
            date = d['date']['value']
            if 'film' in d:
                list.append(d['title']['value'])
        return render_template('writer.html', list = list,nome = nome)
    else:
        return render_template('empty.html',date=date,data = data_iso_formatada)
    
@app.route('/books')
def books():
    sparql_query = """
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where{
    ?s a tp:Book .
}
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('books.html', data = dados)
    else:
        return render_template('empty.html',data = data_iso_formatada)
    
@app.route('/genres')
def genres():
    sparql_query = """
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where{
    ?s a tp:Genre .
}
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('genres.html', data = dados)
    else:
        return render_template('empty.html',data = data_iso_formatada)

@app.route('/genres/<nome>')
def genre(nome):
    sparql_query = f"""
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select * where{{
    ?film a tp:Film .
    ?film tp:hasGenre tp:{nome} .
    ?film tp:title ?title.
}}
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']

        list = []

        for d in dados:
            if 'film' in d:
                list.append(d['title']['value'])
        return render_template('genre.html',list = list,nome = nome)
    else:
        return render_template('empty.html',data = data_iso_formatada)

if __name__ == '__main__':
    app.run(debug=True) #debug=True para atualizar a página automaticamente quando altera o código
