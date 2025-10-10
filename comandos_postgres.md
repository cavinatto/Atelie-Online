<br>

# <center> Comandos postgres </center>
<br>

### - Entrar no Postgres pelo terminal

<p><span style="color: #40916c;">docker exec -it atelie-online-db-1 psql -U postgres -d atelie_db </span></p>

##### resposta

<p>psql (15.14 (Debian 15.14-1.pgdg13+1)) <br>
Type "help" for help.<br>
atelie_db=#</p>

### - Existência de tabelas já criadas

<p><span style="color: #40916c;">\dt</span></p>

##### resposta se já tiver

List of relations
 Schema |   Name   | Type  |  Owner   
------------+--------+--------+----------
 public | usuarios | table | postgres
(1 row)

##### resposta se não tiver

Did not find any relations.
### - Criando tabela

<p><span style="color: #40916c;">CREATE TABLE usuarios (<br>
     id SERIAL PRIMARY KEY,<br>
     nome VARCHAR(100) NOT NULL,<br>
     email VARCHAR(120) UNIQUE NOT NULL,<br>
     senha_hash VARCHAR(128) NOT NULL,<br>   
     is_admin BOOLEAN DEFAULT FALSE,<br>
     data_criacao TIMESTAMP DEFAULT NOW()<BR>
 );
 </span></p>

 resposta - CREATE TABLES

 ##### resposta se não tiver

CREATE TABLE

### - Mostrar estrutura de uma tabela (no caso usuarios)

<p><span style="color: #40916c;">\d usuarios</span></p>

##### resposta
<table>
    <thead>
        <tr>
            <th>Column</th>
            <th>Type</th>
            <th>Collation</th>
            <th>Nullable</th>
            <th>Default</th>;
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>id </td>
            <td>integer</td>
            <td> </td>
            <td>not null</td>
            <td>nextval('usuarios_id_seq'::regclass)</td>
        </tr>
                <tr>
            <td>nome </td>
            <td>character varying(100) </td>
            <td> </td>
            <td>not null</td>
            <td> </td>
        </tr>
                <tr>
            <td> email   </td>
            <td>character varying(120)</td>
            <td> </td>
            <td>not null</td>
            <td> </td>
        </tr>
                <tr>
            <td>senha_hash  </td>
            <td>character varying(128)</td>
            <td> </td>
            <td>not null</td>
            <td>nextval('usuarios_id_seq'::regclass)</td>
        </tr>
                <tr>
            <td>is_admin  </td>
            <td>boolean</td>
            <td> </td>
            <td> </td>
            <td>false</td>
        </tr>
                <tr>
            <td>data_criacao </td>
            <td>timestamp without time zone </td>
            <td> </td>
            <td> </td>
            <td>now()</td>
        </tr>
    </tbody>
</table>

Indexes:
&nbsp;&nbsp;&nbsp;&nbsp;"usuarios_pkey" PRIMARY KEY, btree (id)
&nbsp;&nbsp;&nbsp;&nbsp;"usuarios_email_key" UNIQUE CONSTRAINT, btree (email)

### - Deletar tabela

<p><span style="color: #40916c;">DROP TABLE usuarios;</span></p>

##### resposta se não tiver

ERROR:  table "usuarios_errado" does not exist

### - Erro por falta de tabela no postgres

<p><span style="color: #40916c;">sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedTable) relation "servicos" does not exist
LINE 2: FROM servicos</span></p>

### - Dicionando valores

<p><span style="color: #40916c;">CREATE ROLE admin1 WITH LOGIN PASSWORD 'senha_segura1';<br>
ALTER ROLE admin1 WITH SUPERUSER;</span></p>

### - Ver dados da tabela

<p><span style="color: #40916c;">SELECT * FROM clientes;</span></p>

<br>
<p><span style="color: #d5390eff;">ATENÇÂO</p>

### para criar a tabela deve criadas

#### mostrar containers em execução

<p><span style="color: #40916c;">docker ps</p>

#### resposta 

vê o que foi criado
ver o nome da imagem
ex:CONTAINER ID   IMAGE               COMMAND                  CREATED       STATUS       PORTS                    NAMES
a9d29f416a53   atelie-online-web   "python app.py"          7 hours ago   Up 7 hours   0.0.0.0:5000->5000/tcp   atelie-online-web-1

### para criar table

<p><span style="color: #40916c;">docker compose exec web python criar_tabela.py</p>

#### resposta

Tabelas criadas com sucesso!

Cria tabelas não existentes, não apaga nem sobresceve
depois é só entrar no postgre e dar \dt para conferir

### verificar tabelas que outros criaram

<p><span style="color: #40916c;">docker exec -it atelie-online-db-1 psql -U postgres -d atelie_db</p>

<p><span style="color: #40916c;">\dt public.*</p>