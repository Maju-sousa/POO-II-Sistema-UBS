# Sistema de Agendamentos UBS

Sistema desktop (PySide6) para cadastro de pacientes, profissionais, UBS
e agendamento de consultas, persistindo os dados em um banco **PostgreSQL**
que roda dentro de um **container Docker**.

## Arquitetura

- **Interface**: PySide6 (GUI desktop)
- **ORM**: SQLAlchemy
- **Banco de dados**: PostgreSQL 16, rodando em container Docker
- **Estrutura do projeto**:

```

 📄 main.py            -> ponto de entrada da aplicação
 📄 gerenciador.py      -> regras de negócio + acesso ao banco via ORM
 📄 modelos.py          -> definição das tabelas (Paciente, Profissional, UBS, Consulta)
 📄 banco.py            -> configuração da conexão com o PostgreSQL
 📄 criar_banco.py      -> script para criar as tabelas no banco
 📄 threads.py          -> execução assíncrona das operações (não trava a UI)
 📄 docker-compose.yml  -> sobe o PostgreSQL em container
 📂 interface
   📄 __init__.py
   📄 componentes.py    -> cards, modais e widgets reutilizáveis
   📄 estilos.py        -> folha de estilos (QSS)
   📄 janela_principal.py -> tela principal e lógica de UI
```

## Como rodar

### 1. Subir o banco de dados (Docker)

É necessário ter o [Docker](https://www.docker.com/) instalado.

Na raiz do projeto, execute:

```bash
docker compose up -d
```

Isso vai baixar a imagem do PostgreSQL 16 (se ainda não tiver) e subir um
container chamado `ubs_postgres`, escutando na porta `5432`, com:

- usuário: `ubs_user`
- senha: `ubs_senha`
- banco: `ubs_db`

Para verificar se o container está rodando:

```bash
docker ps
```

Para parar o container:

```bash
docker compose down
```

### 2. Instalar as dependências Python

Recomenda-se usar um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac

pip install -r requirements.txt
```

### 3. Criar as tabelas no banco

Com o container do Docker já rodando, execute:

```bash
python criar_banco.py
```

Isso cria as tabelas `pacientes`, `profissionais`, `ubs` e `consultas`
dentro do banco PostgreSQL que está no container.

### 4. Executar o sistema

```bash
python main.py
```

## Configuração da conexão

Por padrão, o sistema conecta no banco usando estes valores (definidos em
`banco.py`), que já correspondem ao `docker-compose.yml`:

| Variável     | Valor padrão |
|--------------|--------------|
| `DB_USER`    | ubs_user     |
| `DB_PASSWORD`| ubs_senha    |
| `DB_HOST`    | localhost    |
| `DB_PORT`    | 5432         |
| `DB_NAME`    | ubs_db       |

Se quiser usar outras credenciais, basta definir essas variáveis de
ambiente antes de rodar o sistema, sem precisar alterar o código.

## Modelagem do banco

- **pacientes**: `cpf` (chave primária), `nome`, `nascimento`, `telefone`
- **profissionais**: `id` (chave primária), `nome`, `especialidade`
- **ubs**: `id` (chave primária), `nome`, `endereco`
- **consultas**: `id` (chave primária), `paciente_cpf` (FK -> pacientes),
  `profissional_id` (FK -> profissionais), `ubs_id` (FK -> ubs), `data`,
  `horario`, `status`

A tabela `consultas` referencia as demais por **chave estrangeira** (e não
por nome em texto), evitando redundância e dependências transitivas —
mantendo o esquema em conformidade com a 3ª Forma Normal (3FN).
