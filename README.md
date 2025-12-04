# checklistComFastAPI

O presente projeto consiste em uma check-list, em que o usuário pode registrar, excluir, acessar e atualizar sua lista de tarefas. Desenvolvida em Linguagem Python (3.12.7), utiliza a ORM *SQLAlchemy* e o banco de dados *SQLite*.

Para a configuração do ambiente, em nome das boas práticas, utilizou-se o gerenciador de projetos e ambientes *poetry* e ferramentas de análise estática e formatação de código.

Com o framework *FastAPI* (0.123.4), realizou-se operações CRUD, criou-se endpoints e schemas e aplicou-se injenções de dependência.

Utilizou-se o *Pydantic* e *SQLAlquemy* para modelagem de dados, e *Alembic* para para configurar as migrações de bancos de dados.

Também, investiu-se em um desenvolvimento orientado a testes, utilizando *pytest* e coverage, além de um pipeline de integração contínua com o *GitHub Actions*.

Finalmente, fez-se a conteinerização do projeto com *Docker* e um deploy com *Fly.io*.

Utilizou-se a arquitetura MVC (Model-View-Controller) para separar os dados e regras de negócio (Model) da interface com a qual o usuário interage (View). A intermediação destes é feita pelo Controller, que recebe as requisições do usuário, solicita a sua execução ao Model e atualiza a View com a resposta.

## Configurações iniciais:

```bash:
docker compose up --build
```

Para parar a execução, pressione Ctrl+C.

## Configuração do ambiente (Linux/Unix)

* pyenv (version 2.6.13)

```bash:
cd ~
curl -fsSL https://pyenv.run | bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
nano .bashrc
```

No arquivo ".bashrc", insira as linhas

```bash:
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init - bash)"
```
Salve o arquivo (Ctrl+S).

De volta ao terminal, para aplicar as mudanças, digite

```bash:
source .bashrc
```

* pipx (version 1.8.0)

```bash:
pip install pipx
```

* poetry (version 2.2.1)

```bash:
pipx install poetry
pipx ensurepath
```

Feche e abra novamente o terminal. Digite:

```bash:
poetry new [nome-do-pacote]
pyenv local [python-version]
poetry install
```

Para instalar módulos,

```bash:
poetry add fastapi[standard] # exemplo de módulo
```

Para rodar a aplicação,

```bash:
poetry env info --path
```

Forneça o diretório como interpretador. Feche e abra novamente o terminal. 

Para subir o servidor,

```bash:
cd checklist
task run
```