# Problema

Escola de musica:
- alunos;
- instrumentos;
- cursos;

A fazer:
1. analisar o dataset;
2. criar uma ontologia (classes,object properties,data properties);
3. criar uma script para povoar a ontologia;
4. criar um repositorio no graphDB com a ontologia.

# Solução

Foram criadas 3 **Classes** nesta ontologia:
- Aluno
- Curso
- Instrumento

Foram criadas os **Object Properties**:
- ensinaInstrumento: Curso -> Instrumento
- noCurso: Aluno -> Curso
- tocaInstrumento: Aluno -> Instrumento

A classe **Aluno** contém as **Data Properties**:
- alunoAnoCurso
- alunoDataDeNascimento
- alunoId
- alunoNome

Individuos desta classe são identificados com _alunoId_.

A classe **Curso** contém as **Data Properties**:
- cursoDesignacao
- cursoDuracao
- cursoId
- cursoInstrumento

Individuos desta classe são identificados com _cursoId_.

A classe **Instrumento** contém as **Data Properties**:
- instrumentoId
- instrumentoNome

Individuos desta classe são identificados com _instrumentoNome_.

Ficheiros:

- [Base de dados](https://github.com/Gon96923/RPCW2024/blob/main/TPC2/db.json)
- [Ontologia com um individuo de cada classe](https://github.com/Gon96923/RPCW2024/blob/main/TPC2/escola_de_musica.ttl)
- [Script para povoar ontologia](https://github.com/Gon96923/RPCW2024/blob/main/TPC2/geraTTL.py)
- [Ontologia povoada final](https://github.com/Gon96923/RPCW2024/blob/main/TPC2/escolaMusica.ttl) 
