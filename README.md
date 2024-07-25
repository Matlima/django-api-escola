# Django REST Framework Application: Escola

## Descrição

Esta é uma aplicação web desenvolvida usando Django e Django REST Framework (DRF). A aplicação serve como uma API backend para gerenciar dados de um sistema específico. 
Abaixo estão listados os principais pontos implementados, os endpoints disponíveis e as ferramentas utilizadas no desenvolvimento.

## Funcionalidades Implementadas

- **Autenticação e Autorização**: Implementação de JWT (JSON Web Tokens) para autenticação segura dos estudantess.
- **CRUD Completo**: Criação, leitura, atualização e exclusão de registros para múltiplas entidades.
- **Filtros e Pesquisa**: Funcionalidades de filtragem e pesquisa avançadas para endpoints.
- **Paginação**: Implementação de paginação para gerenciar grandes conjuntos de dados.
- **Validações Personalizadas**: Validações de dados personalizadas para garantir a integridade dos dados.
- **Permissões Personalizadas**: Controle de acesso baseado em permissões personalizadas.
- **Documentação da API**: Documentação da API gerada automaticamente usando o Swagger e o Redoc.

## Endpoints Disponíveis

### estudantes

- **`GET /estudante/`**: Lista todos os estudantess.
- **`GET /estudante/{id}/`**: Detalhes de um estudantes específico.
- **`GET /estudante/{id}/matriculas`**: Detalhes de todas as matriculas um estudantes específico.
- **`POST /estudante/`**: Cria um novo estudantes.
- **`PUT /estudante/{id}/`**: Atualiza um estudantes específico.
- **`DELETE /estudante/{id}/`**: Exclui um estudantes específico.

### Cursos (exemplo de entidade)

- **`GET /cursos/`**: Lista todos os Cursos.
- **`GET /cursos/{id}/`**: Detalhes de um curso específico.
- **`GET /cursos/{id}/matriculas`**: Detalhes de todas as matriculas no curso específico.
- **`POST /cursos/`**: Cria um novo curso.
- **`PUT /cursos/{id}/`**: Atualiza um curso específico.
- **`DELETE /cursos/{id}/`**: Exclui um curso específico.

  ### Matricula (exemplo de entidade)

- **`GET /matricula/`**: Lista todas as Matriculas.
- **`GET /matricula/{id}/`**: Detalhes de uma matricula específica.
- **`POST /matricula/`**: Cria uma nova matricula.
- **`PUT /matricula/{id}/`**: Atualiza uma matricula específica.
- **`DELETE /matricula/{id}/`**: Exclui uma matricula específica.

## Ferramentas Utilizadas

- **Django**: Framework web de alto nível para o desenvolvimento rápido de aplicações web.
- **Django REST Framework**: Toolkit poderoso e flexível para construir APIs web.
- **Django REST Framework Basic Authentication**: Implementação de Basic Authentication para autenticação.
- **SQLite**: Sistema de gerenciamento de banco de dados relacional utilizado no backend.
- **Swagger**: Ferramenta para gerar documentação interativa da API.
- **Redoc**: Ferramenta para gerar documentação estática e amigável da API.
- **GitHub Actions**: Para integração e entrega contínua (CI/CD).

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Matlima/django-api-escola
   cd sua-aplicacao
   ```
   
2. Configure o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
Crie um arquivo .env na raiz do projeto e adicione as variáveis necessárias, como configurações do banco de dados e chave secreta do Django.

5. Aplique as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

6. Execute a aplicação:
   ```bash
   python manage.py runserver
   ```

## Uso
Após iniciar o servidor, a API estará disponível em http://127.0.0.1:8000/. Utilize ferramentas como Postman ou cURL para interagir com os endpoints da API.

## Contribuição
- Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

## Licença
- Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

***

Feito com ❤️ por Matheus Lima

