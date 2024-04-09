from flask import Flask,render_template,url_for,request
from datetime import datetime
import requests

app = Flask(__name__)

#dat do sistema no formato ISO
data_hora_atual = datetime.now()
data_iso_formatada = data_hora_atual.strftime('%Y-%m-%dT%H:%M:%S')

# GraphDB endpoint
graphdb_endpoint = "http://localhost:7200/repositories/avalia"




@app.route('/api/alunos')
def alunos():
    if "curso" in request.args:
        curso = request.args['curso']
        sparql_query = f"""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX tp: <http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/>
select ?nome where {{
	?ID rdf:type tp:Aluno.
    ?ID tp:alunoNome ?nome.
    ?ID tp:inCurso tp:{curso}.
}}
ORDER BY ?nome
"""
    else:
        if "groupBy" in request.args:
            groupBy = request.args['groupBy']
            if groupBy == 'curso':
                sparql_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX tp: <http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/>
select ?Curso (count(distinct ?ID) as ?Nmero_de_Alunos) where {
	?ID rdf:type tp:Aluno.
    ?ID tp:inCurso ?Curso.
}
GROUP BY ?Curso
"""
            elif groupBy == 'projeto':
                sparql_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX tp: <http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/>
select ?Nota (count(distinct ?ID) as ?Nmero_de_Alunos) where {
	?ID rdf:type tp:Aluno.
    ?ID tp:hasProjeto ?p.
    ?p tp:projetoNota ?Nota.
}
GROUP BY ?Nota
"""
            elif groupBy == 'recurso':
                sparql_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX tp: <http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/>
select ?ID ?Nome ?Curso ?Nota where {
	?ID rdf:type tp:Aluno.
    ?ID tp:hasExame ?exame.
    ?exame tp:exameTipo "recurso".
    ?exame tp:exameNota ?Nota.
    ?ID tp:alunoNome ?Nome.
    ?ID tp:inCurso ?Curso.

}
ORDER BY ?Nome
"""
        else:
            sparql_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX tp: <http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/>
select ?ID ?Nome ?Curso where { 
    ?ID rdf:type tp:Aluno.
    ?ID tp:alunoNome ?Nome.
    ?ID tp:inCurso ?Curso.
}
ORDER BY ?Nome
"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
        
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']#devolve um dicionário(a parte que quer)

        for d in dados:
            for key,value in d.items():
                d[key] = value['value'].replace('http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/','')
        return dados



@app.route('/api/alunos/:<id>')
def aluno(id):
    sparql_query = f'''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX tp: <http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/>
select * where {{
    ?ID a tp:Aluno .
    ?ID tp:alunoId "{id}" .
    ?ID tp:alunoNome ?Nome .
    ?ID tp:inCurso ?Curso .
    ?ID tp:hasTPC ?TPC .
    ?ID tp:hasProjeto ?Projeto .
    ?ID tp:hasExame ?Exame .
}}
'''

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']#devolve um dicionário(a parte que quer)

        for d in dados:
            for key,value in d.items():
                d[key] = value['value'].replace('http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/','')
        return dados
    
    
@app.route('/api/alunos/tpc')
def tpc():
    sparql_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX tp: <http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/>
select ?ID ?Nome ?Curso (count(distinct ?TPC) as ?TPC_Count) where {
	?ID rdf:type tp:Aluno.
    ?ID tp:alunoNome ?Nome.
    ?ID tp:inCurso ?Curso.
    ?ID tp:hasTPC ?TPC.
}
group BY ?Nome ?ID ?Curso
order by ?Nome

"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']#devolve um dicionário(a parte que quer)

        for d in dados:
            for key,value in d.items():
                d[key] = value['value'].replace('http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/','')
        return dados
    

@app.route('/api/alunos/avaliados')
def avaliados():
    sparql_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX tp: <http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/>
select ?ID ?Nome ?Curso ?Nota_Exame ?Nota_Projeto ?Nota_TPC where {
	?ID rdf:type tp:Aluno.
    ?ID tp:alunoNome ?Nome.
    ?ID tp:inCurso ?Curso.
    ?ID tp:hasProjeto ?proj.
    ?proj tp:projetoNota ?Nota_Projeto.
    ?ID tp:hasExame ?exame.
    ?exame tp:exameNota ?Nota_Exame.
    ?ID tp:hasTPC ?TPC.
    ?TPC tp:tpcNota ?Nota_TPC.
}
order by ?Nome
limit 100

"""

    resposta = requests.get(graphdb_endpoint, 
                            params={'query': sparql_query},
                            headers={'Accept': 'application/sparql-results+json'})
    
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']#devolve um dicionário(a parte que quer)



        for d in dados:
            for key,value in d.items():
                d[key] = value['value'].replace('http://www.semanticweb.org/gvale/ontologies/2024/3/avalia/','')
                if key == 'Nota_Projeto' and float(d[key]) < 10:
                    d["notaFinal"] = "R"

        for d in dados:
            if "notaFinal" not in d:
                nota = 0
                for key,value in d.items():
                    if key == "Nota_TPC":
                        nota += float(value)
                    if key == "Nota_Projeto":
                        nota += 0.4*float(value)
                    if key == "Nota_Exame":
                        nota += 0.4*float(value)
                if nota >= 10:
                    d["notaFinal"] = nota
                else:
                    d["notaFinal"] = "R"
            else:
                d["notaFinal"] = "R"                
        return dados    

    
if __name__ == '__main__':
    app.run(debug=True) #debug=True para atualizar a página automaticamente quando altera o código