from flask import Flask,render_template,url_for
from datetime import datetime
import requests

app = Flask(__name__)

#dat do sistema no formato ISO
data_hora_atual = datetime.now()
data_iso_formatada = data_hora_atual.strftime('%Y-%m-%dT%H:%M:%S')

# GraphDB endpoint
graphdb_endpoint = "http://localhost:7200/repositories/tab_periodica"

#pedido/rota atendido pela aplicação
@app.route('/')
def index():
    return render_template('index.html', data = {"data": data_iso_formatada}) #linha 21 no index.html



@app.route('/elementos')
def elementos():
    sparql_query = """
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select * where{
    ?s a tp:Element ;
        tp:name ?nome ;
        tp:symbol ?simb ;
        tp:atomicNumber ?n ;
        tp:group ?g.

}
order by ?n
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']#devolve um dicionário(a parte que quer)
        return render_template('elementos.html', data = dados)
    else:
        return render_template('empty.html',data = data_iso_formatada)



@app.route('/elemento/<nome>')
def elemento(nome):
    sparql_query = f'''
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select * where {{
    ?s a tp:Element ;
        tp:name "{nome}" ;
        tp:symbol ?simb ;
        tp:atomicNumber ?n ;
        tp:group ?group .
    optional {{ ?s tp:block ?block . }} 
    optional {{ ?s tp:classification ?class . }} 
    optional {{ ?s tp:period ?period . }}
    optional {{ ?s tp:standardState ?state .}}  
    optional {{ ?s tp:atomicWeight ?w . }} 
    optional {{ ?s tp:color ?color . }} 
    
}}
'''

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']#devolve um dicionário(a parte que quer)
        return render_template('elemento.html', data = {'dados':dados, 'nome':nome})
    else:
        return render_template('empty.html',data = data_iso_formatada)
    


@app.route('/grupos')
def grupos():
    sparql_query = """
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select * where{
    ?groups a tp:Group .
}
order by ?groups
"""
#<a href="/grupo/{{entry.nome.value}}"></a>
    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']#devolve um dicionário(a parte que quer)
        return render_template('grupos.html', data = dados)
    else:
        return render_template('empty.html',data = data_iso_formatada)
    


@app.route('/grupo/<nome>')
def grupo(nome):
    sparql_query = f'''
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select * where{{
    ?s a tp:Group .
    optional {{ ?s tp:name ?name . }} 
    optional {{ ?s tp:number ?number . }}
    ?s tp:element ?elem .
    ?elem tp:name ?ln.
    ?elem tp:symbol ?sim.
    filter(str(?s) = "http://www.daml.org/2003/01/periodictable/PeriodicTable#{nome}")
}}

'''

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']#devolve um dicionário(a parte que quer)
        print(dados)
        print(nome)
        return render_template('grupo.html', data = {'dados':dados, 'nome':nome})
    else:
        return render_template('empty.html',data = data_iso_formatada)



if __name__ == '__main__':
    app.run(debug=True) #debug=True para atualizar a página automaticamente quando altera o código