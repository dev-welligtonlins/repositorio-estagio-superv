-- Criar banco de dados (PostgreSQL 9.5+ suporta IF NOT EXISTS)
SET client_encoding = 'UTF8';

SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'estagio_lbs6' AND pid <> pg_backend_pid();

DROP DATABASE estagio_lbs6;

CREATE DATABASE estagio_lbs6 WITH 
    OWNER = root
    ENCODING = 'UTF8'
    TEMPLATE template0;

-- TABELA: CURSOS
CREATE TABLE IF NOT EXISTS cursos (
    cur_id SERIAL PRIMARY KEY,
    cur_nome VARCHAR(255) NOT NULL,
    cur_quant_periodos INT NOT NULL,
    cur_turno VARCHAR(20) NOT NULL CHECK (cur_turno IN ('Manhã','Tarde','Noite','Integral'))
);

-- TABELA: DISCIPLINAS
CREATE TABLE IF NOT EXISTS disciplinas (
    dis_id SERIAL PRIMARY KEY,
    dis_nome VARCHAR(255) NOT NULL,
    dis_curso INT REFERENCES cursos(cur_id),
    dis_carga_horaria INT NOT NULL
);

-- TABELA: ALUNO_PCD
CREATE TABLE IF NOT EXISTS aluno_pcd (
    alu_id SERIAL PRIMARY KEY,
    alu_nome VARCHAR(255) NOT NULL,
    alu_cpf CHAR(25) NOT NULL,
    alu_genero CHAR(1) NOT NULL,
    alu_email_pessoal VARCHAR(255) NOT NULL,
    alu_email_institucional VARCHAR(255) NOT NULL,
    alu_telefone VARCHAR(255) NOT NULL,
    alu_endereco_cep VARCHAR(255),
    alu_endereco_descricao VARCHAR(255),
    alu_endereco_cidade CHAR(2),
    alu_matricula CHAR(25) NOT NULL,
    alu_deficiencias VARCHAR(255),
    alu_curso INT REFERENCES cursos(cur_id),
    alu_periodo_academico VARCHAR(255) NOT NULL,
    alu_data_nascimento DATE NOT NULL,
    alu_ativo BOOLEAN,
    alu_usuario INT,
    permissao INT
);

-- TABELA: MONITOR
CREATE TABLE IF NOT EXISTS monitor (
    mon_id SERIAL PRIMARY KEY,
    mon_nome VARCHAR(255) NOT NULL,
    mon_cpf CHAR(25) NOT NULL,
    mon_genero CHAR(1) NOT NULL,
    mon_email_pessoal VARCHAR(255) NOT NULL,
    mon_email_institucional VARCHAR(255) NOT NULL,
    mon_telefone VARCHAR(255) NOT NULL,
    mon_endereco_cep VARCHAR(255),
    mon_endereco_descricao VARCHAR(255),
    mon_endereco_cidade CHAR(2),
    mon_matricula CHAR(25) NOT NULL,
    mon_curso INT REFERENCES cursos(cur_id),
    mon_periodo_academico VARCHAR(255) NOT NULL,
    mon_ativo BOOLEAN,
    mon_usuario INT,
    permissao INT
);

-- TABELA: TUTOR
CREATE TABLE IF NOT EXISTS tutor (
    tut_id SERIAL PRIMARY KEY,
    tut_nome VARCHAR(255) NOT NULL,
    tut_cpf CHAR(25) NOT NULL,
    tut_genero CHAR(1) NOT NULL,
    tut_email_pessoal VARCHAR(255) NOT NULL,
    tut_email_institucional VARCHAR(255) NOT NULL,
    tut_telefone VARCHAR(255) NOT NULL,
    tut_endereco_cep VARCHAR(255),
    tut_endereco_descricao VARCHAR(255),
    tut_endereco_cidade CHAR(2),
    tut_matricula CHAR(25) NOT NULL,
    tut_curso INT REFERENCES cursos(cur_id),
    tut_periodo_academico VARCHAR(255) NOT NULL,
    tut_ativo BOOLEAN,
    tut_usuario INT,
    permissao INT
);

-- TABELA: ADMINISTRADOR
CREATE TABLE IF NOT EXISTS administrador (
    adm_id SERIAL PRIMARY KEY,
    adm_nome VARCHAR(255) NOT NULL,
    adm_cpf CHAR(25) NOT NULL,
    adm_email VARCHAR(255) NOT NULL,
    adm_usuario INT,
    permissao INT
);

-- TABELA: AVISOS
CREATE TABLE IF NOT EXISTS avisos (
    avi_id SERIAL PRIMARY KEY,
    avi_titulo VARCHAR(255) NOT NULL,
    avi_descricao VARCHAR(255),
    avi_data TIMESTAMP NOT NULL,
    avi_arquivos TEXT,
    avi_administrador INT REFERENCES administrador(adm_id),
    avi_mostrar BOOLEAN
);

-- TABELA: ACOMPANHAMENTO
CREATE TABLE IF NOT EXISTS acompanhamento (
    aco_id SERIAL PRIMARY KEY,
    aco_semestre CHAR(6),
    aco_inicio DATE NOT NULL,
    aco_fim DATE,
    aco_aluno_pcd INT REFERENCES aluno_pcd(alu_id),
    aco_monitor INT,
    aco_tutor INT
);

-- TABELA: INTERPRETE
CREATE TABLE IF NOT EXISTS interprete (
    int_id SERIAL PRIMARY KEY,
    int_nome VARCHAR(255) NOT NULL,
    int_cpf CHAR(25) NOT NULL,
    int_genero CHAR(1) NOT NULL,
    int_email_pessoal VARCHAR(255) NOT NULL,
    int_email_institucional VARCHAR(255) NOT NULL,
    int_telefone VARCHAR(255) NOT NULL,
    int_ativo BOOLEAN,
    int_usuario INT,
    permissao INT
);

-- TABELA: ACOMPANHAMENTO_DISCIPLINA
CREATE TABLE IF NOT EXISTS acompanhamento_disciplina (
    asdis_id SERIAL PRIMARY KEY,
    asdis_disciplina INT REFERENCES disciplinas(dis_id),
    asdis_acompanhamento INT REFERENCES acompanhamento(aco_id)
);

-- TABELA: ACOMPANHAMENTO_INTERPRETE
CREATE TABLE IF NOT EXISTS acompanhamento_interprete (
    asint_id SERIAL PRIMARY KEY,
    asint_inicio DATE NOT NULL,
    asint_fim DATE,
    asint_interprete INT REFERENCES interprete(int_id),
    asint_acompanhamento INT REFERENCES acompanhamento(aco_id)
);

-- TABELA: ACOMPANHAMENTO_MONITORIA
CREATE TABLE IF NOT EXISTS acompanhamento_monitoria (
    asmon_id SERIAL PRIMARY KEY,
    asmon_inicio DATE NOT NULL,
    asmon_fim DATE,
    asmon_monitor INT REFERENCES monitor(mon_id),
    asmon_acompanhamento INT REFERENCES acompanhamento(aco_id)
);

-- TABELA: ACOMPANHAMENTO_TUTORIA
CREATE TABLE IF NOT EXISTS acompanhamento_tutoria (
    astut_id SERIAL PRIMARY KEY,
    astut_inicio DATE NOT NULL,
    astut_fim DATE,
    astut_tutor INT REFERENCES tutor(tut_id),
    astut_acompanhamento INT REFERENCES acompanhamento(aco_id)
);

-- TABELA: HORARIOS_DISCIPLINA
CREATE TABLE IF NOT EXISTS horarios_disciplina (
    hodis_id SERIAL PRIMARY KEY,
    hodis_dia VARCHAR(20) CHECK (hodis_dia IN ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado')),
    hodis_inicio TIME,
    hodis_fim TIME,
    hodis_disciplina INT REFERENCES acompanhamento_disciplina(asdis_id)
);

-- TABELA: FEEDBACKS
CREATE TABLE IF NOT EXISTS feedbacks (
    fee_id SERIAL PRIMARY KEY,
    fee_titulo VARCHAR(255) NOT NULL,
    fee_descricao VARCHAR(255) NOT NULL,
    fee_data TIMESTAMP NOT NULL,
    fee_arquivo TEXT,
    fee_acompanhamento INT REFERENCES acompanhamento(aco_id)
);

-- TABELA: LAUDOS
CREATE TABLE IF NOT EXISTS laudos (
    lau_id SERIAL PRIMARY KEY,
    lau_status VARCHAR(10) NOT NULL CHECK (lau_status IN ('Ativo', 'Inativo')),
    lau_numero VARCHAR(255) NOT NULL,
    lau_nome VARCHAR(255) NOT NULL,
    lau_arquivo TEXT NOT NULL,
    lau_aluno INT REFERENCES aluno_pcd(alu_id)
);

-- TABELA: RELATORIOS_MONITORIA
CREATE TABLE IF NOT EXISTS relatorios_monitoria (
    relm_id SERIAL PRIMARY KEY,
    relm_titulo VARCHAR(255) NOT NULL,
    relm_data TIMESTAMP NOT NULL,
    relm_verificado BOOLEAN,
    relm_arquivo TEXT,
    relm_monitoria INT REFERENCES acompanhamento_monitoria(asmon_id)
);

-- TABELA: RELATORIOS_TUTORIA
CREATE TABLE IF NOT EXISTS relatorios_tutoria (
    relt_id SERIAL PRIMARY KEY,
    relt_titulo VARCHAR(255) NOT NULL,
    relt_data TIMESTAMP NOT NULL,
    relt_verificado BOOLEAN,
    relt_arquivo TEXT,
    relt_tutoria INT REFERENCES acompanhamento_tutoria(astut_id)
);
