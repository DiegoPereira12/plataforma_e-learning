# Plataforma E-learning (em construção) 🚧

Criar uma aplicação Server-Side que irá permitir gerir uma 'mini' solução de e-learning, 
que terá cursos, alunos e matrículas. Essa aplicação deverá ter as APIs expostas para que uma aplicação WEB
possa consumir os recursos.

### 1) API Básica

A modelagem do projeto terá os seguintes modelos.

- Course (name, description, holder_image, duration, date_created, date_updated) :heavy_check_mark:
- Student (name, nickname, phone, avatar, date_created, date_updated) :heavy_check_mark:
- Enrollment (student, course, date_enroll, date_close, score, status) / * Status = (Aprovado, Reprovado, Andamento) :heavy_check_mark:
  
A API deverá fornecer recursos para:
- Listar todos os cursos do catalogo :heavy_check_mark:
- Cadastrar e atualizar novos cursos :heavy_check_mark:
- Excluir cursos existentes :heavy_check_mark:
- Listar todos os alunos :hammer_and_wrench:
- Cadastrar/Editar novos alunos :hammer_and_wrench:
- Matricular um aluno em um curso
- Remover o aluno de um curso

Regras de négocios a ser implementadas:
- Um usuário pode desistir de um curso e informar uma justificativa
- Um usuário não pode estar matriculado em mais de uma curso ao mesmo tempo (matrícula em andamento - ativa)
- Um usuário não pode ser considerado aprovado se ele obter uma nota menor que 6 ao concluir uma matrícula
- Um curso pode notificar (pode ser um print) os usuários que estão matriculados que o curso irá ser expirado em X dias.
- Um curso pode notificar o usuário dono do curso que novas matrículas foram iniciadas ou concluídas


### 2) Filtros

Um recurso importante das APIs é a capacitade de prover filtros para que o front-end possa criar suas soluções otimizando
recursos e dando flexibilidade para os usuários. Sendo assim, a API deverá ser possível:

- Filtrar quais matrículas foram reprovadas
- Filtrar todas as matrículas de um determinado aluno
- Filtrar todas as matrículas de um determinado curso
- Filtrar as matrículas que foram concluídas em um determinado período;
- Filtrar as matrículas que foram iniciadas em um determinado período;
- Filtrar alunos cadastrados em um determinado período;

