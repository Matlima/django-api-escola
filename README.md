# Django REST Framework Application

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

### Autenticação

- **`POST /estudantes/`**: Endpoint para cadastrar estudante.
- **`GET /estudantes/`**: Endpoint para os registros de estudantes.
- **`POST /cursos/`**: Endpoint para cadastrar cursos.
- **`GET /cursos/`**: Endpoint para os registros de cursos

### estudantes

- **`GET /api/estudante/`**: Lista todos os estudantess.
- **`GET /api/estudante/{id}/`**: Detalhes de um estudantes específico.
- **`POST /api/estudante/`**: Cria um novo estudantes.
- **`PUT /api/estudante/{id}/`**: Atualiza um estudantes específico.
- **`DELETE /api/estudante/{id}/`**: Exclui um estudantes específico.

### Cursos (exemplo de entidade)

- **`GET /api/cursos/`**: Lista todos os Cursos.
- **`GET /api/cursos/{id}/`**: Detalhes de um produto específico.
- **`POST /api/cursos/`**: Cria um novo produto.
- **`PUT /api/cursos/{id}/`**: Atualiza um produto específico.
- **`DELETE /api/cursos/{id}/`**: Exclui um produto específico.

## Ferramentas Utilizadas

- **Django**: Framework web de alto nível para o desenvolvimento rápido de aplicações web.
- **Django REST Framework**: Toolkit poderoso e flexível para construir APIs web.
- **Django REST Framework SimpleJWT**: Implementação de JWT para autenticação.
- **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional utilizado no backend.
- **Docker**: Plataforma para desenvolver, enviar e executar aplicações em containers.
- **Swagger**: Ferramenta para gerar documentação interativa da API.
- **Redoc**: Ferramenta para gerar documentação estática e amigável da API.
- **GitHub Actions**: Para integração e entrega contínua (CI/CD).

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sua-aplicacao.git
   cd sua-aplicacao
   ```


## Contribuição
- Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

## Licença
- Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

