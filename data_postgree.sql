SET client_encoding = 'UTF8';


-- 1. CURSOS (base para várias FK)
INSERT INTO cursos (cur_id, cur_nome, cur_quant_periodos, cur_turno)
VALUES
(1, 'Sistemas de Informação', 8, 'Integral'),
(2, 'Engenharia Civil', 10, 'Integral'),
(3, 'Engenharia Elétrica', 10, 'Integral'),
(4, 'Matemática', 8, 'Tarde')
ON CONFLICT (cur_id) DO NOTHING;

-- 2. ALUNO_PCD (depende de cursos)
INSERT INTO aluno_pcd (
    alu_id, alu_nome, alu_cpf, alu_genero, alu_email_pessoal, alu_email_institucional,
    alu_telefone, alu_endereco_cep, alu_endereco_descricao, alu_endereco_cidade, alu_matricula,
    alu_deficiencias, alu_curso, alu_periodo_academico, alu_data_nascimento, alu_ativo, alu_usuario, permissao
)
VALUES
(2, 'aluno_01', '48913276007', 'M', 'aluno_01@g.com.br', 'aluno_01@lala.br', '8890044-4432', '69443-201',
 'rua vinte, bairro 10', 'RB', '201000300942', 'n/a', 1, '5', '2025-08-08', true, NULL, 2),
(3, 'aluno_02', '01826384050', 'M', 'aluno_01@g.com.br', 'aluno_01@lala.br', '8890044-4432', '69443-201',
 'rua vinte, bairro 10', 'RB', '201000300942', 'n/a', 3, '6', '2025-08-08', true, NULL, 2),
(4, 'aluno_03', '47218937009', 'M', 'aluno_01@g.com.br', 'aluno_01@lala.br', '8890044-4432', '69443-201',
 'rua vinte, bairro 10', 'RB', '201000300942', 'n/a', 4, '7', '2025-08-08', true, NULL, 2),
(1, 'aluno_04', '10945268040', 'M', 'aluno_01@g.com.br', 'aluno_01@lala.br', '8890044-4432', '69443-201',
 'rua vinte, bairro 10', 'RB', '201000300942', 'n/a', 2, '5', '2025-08-08', true, NULL, 2)
ON CONFLICT (alu_id) DO NOTHING;

-- 3. MONITOR (depende de cursos)
INSERT INTO monitor (mon_id, mon_nome, mon_cpf, mon_genero, mon_email_pessoal, mon_email_institucional,
    mon_telefone, mon_endereco_cep, mon_endereco_descricao, mon_endereco_cidade,
    mon_matricula, mon_curso, mon_periodo_academico, mon_ativo, mon_usuario, permissao
)
VALUES
(1, 'monitor_1', '01826384050', 'M', 'monitor_1@email.com', 'monitor_1@universidade.edu',
 '(11)91234-5678', '12345678', 'Rua das Flores, 123', 'SP', '20201234567', 1, '5', true, NULL, 2),
(2, 'monitor_2', '47218937009', 'F', 'monitor_2@email.com', 'monitor_2@universidade.edu',
 '(21)99876-5432', '87654321', 'Av. Central, 456', 'RJ', '20206543210', 2, '3º período', true, NULL, 2)
ON CONFLICT (mon_id) DO NOTHING;

-- 4. TUTOR (depende de cursos)
INSERT INTO tutor (tut_id, tut_nome, tut_cpf, tut_genero, tut_email_pessoal, tut_email_institucional,
    tut_telefone, tut_endereco_cep, tut_endereco_descricao, tut_endereco_cidade,
    tut_matricula, tut_curso, tut_periodo_academico, tut_ativo, tut_usuario, permissao
)
VALUES
(1, 'tutor_1', '01826384050', 'F', 'tutor_1@email.com', 'tutor_1@universidade.edu',
 '(11)91234-5678', '01234567', 'Rua A, 123', 'SP', '20201234567', 1, '4º período', true, NULL, 2),
(2, 'tutor_2', '47218937009', 'M', 'tutor_1@email.com', 'tutor_1@universidade.edu',
 '(21)97654-3210', '76543210', 'Av. B, 456', 'RJ', '20206543210', 2, '6º período', true, NULL, 2)
ON CONFLICT (tut_id) DO NOTHING;

-- 9. INTERPRETE (independente)
INSERT INTO interprete (int_id, int_nome, int_cpf, int_genero, int_email_pessoal, int_email_institucional,
    int_telefone, int_ativo, int_usuario, permissao
)
VALUES 
(1, 'interprete_1', '10945268040', 'M', 'interprete_1@email.com', 'interprete_1@universidade.edu', '(31)99876-5432', true, NULL, 2),
(2, 'interprete_2', '76103459020', 'F', 'interprete_2@email.com', 'interprete_2@universidade.edu', '(41)98765-1234', true, NULL, 2)
ON CONFLICT (int_id) DO NOTHING;

-- 5. ACOMPANHAMENTO (depende de aluno_pcd, monitor, tutor)
INSERT INTO acompanhamento (aco_id, aco_semestre, aco_inicio, aco_fim, aco_aluno_pcd, aco_monitor, aco_tutor)
VALUES 
(1, '2023-1', '2023-02-01', '2023-06-30', 1, 1, 2),
(2, '2023-2', '2023-08-01', '2023-12-15', 2, 2, 2),
(3, '2024-1', '2024-02-05', '2024-06-25', 3, 1, 1)
ON CONFLICT (aco_id) DO NOTHING;


-- 5.1 ACOMPANHAMENTO_MONITORIA
INSERT INTO acompanhamento_monitoria (asmon_id, asmon_inicio, asmon_fim, asmon_monitor, asmon_acompanhamento)
VALUES
(1, '2023-02-01', '2023-06-30', 1, 1),
(2, '2023-08-01', '2023-12-15', 2, 2),
(3, '2024-02-05', '2024-06-25', 1, 3)
ON CONFLICT (asmon_id) DO NOTHING;

-- 5.2 ACOMPANHAMENTO_TUTORIA
INSERT INTO acompanhamento_tutoria (astut_id, astut_inicio, astut_fim, astut_tutor, astut_acompanhamento)
VALUES
(1, '2023-02-01', '2023-06-30', 2, 1),
(2, '2023-08-01', '2023-12-15', 2, 2),
(3, '2024-02-05', '2024-06-25', 1, 3)
ON CONFLICT (astut_id) DO NOTHING;

-- 5.3 ACOMPANHAMENTO_INTERPRETE
INSERT INTO acompanhamento_interprete (asint_id, asint_inicio, asint_fim, asint_interprete, asint_acompanhamento)
VALUES
(1, '2023-02-01', '2023-06-30', 1, 1)
ON CONFLICT (asint_id) DO NOTHING;



-- 6. FEEDBACKS (depende de acompanhamento)
INSERT INTO feedbacks (fee_id, fee_titulo, fee_descricao, fee_data, fee_arquivo, fee_acompanhamento)
VALUES (1, 'Relatório Semanal', 'Relatório de desempenho da equipe', '2025-08-01 09:00:00', NULL, 1)
ON CONFLICT (fee_id) DO NOTHING;

-- 7. ADMINISTRADOR (independente)
INSERT INTO administrador (adm_id, adm_nome, adm_cpf, adm_email, adm_usuario, permissao) 
VALUES (1, 'admin_visitante', '29748638049', 'visitante@admin.com.br', 1, 1)
ON CONFLICT (adm_id) DO NOTHING;

-- 8. AVISOS (depende de administrador)
INSERT INTO avisos (avi_id, avi_titulo, avi_descricao, avi_data, avi_arquivos, avi_administrador, avi_mostrar) 
VALUES 
(66, 'Novo semestre', 'Voltas a aulas devem ser com a documentação em dia!', '2025-08-08', NULL, 1, true),
(67, 'Novo semestre', 'Voltas a aulas devem ser com a documentação em dia!', '2025-08-08', NULL, 1, true),
(68, 'Novo semestre', 'Voltas a aulas devem ser com a documentação em dia!', '2025-08-08', NULL, 1, true),
(69, 'Visitantes do site', 'O site foi feito como trabalho acadêmico e as informações são fictícias. A demo contém menos funcionalidades disponíveis (relatórios, login, feedback).', '2025-08-08', NULL, 1, true)
ON CONFLICT (avi_id) DO NOTHING;

-- 10. DISCIPLINAS (depende de cursos)
INSERT INTO disciplinas (dis_id, dis_nome, dis_curso, dis_carga_horaria)
VALUES
(1, 'Algoritmos e Estruturas de Dados', 1, 60),
(2, 'Banco de Dados I', 1, 60),
(3, 'Cálculo I', 2, 80),
(4, 'Física Geral', 2, 60),
(5, 'Programação Orientada a Objetos', 1, 60),
(6, 'Estrutura de Computadores', 1, 60),
(7, 'Matemática Discreta', 1, 60),
(8, 'Engenharia de Software I', 1, 60),
(9, 'Estatística Aplicada', 2, 60),
(10, 'Cálculo II', 2, 80),
(11, 'Lógica de Programação', 1, 60),
(12, 'Redes de Computadores', 1, 60),
(13, 'Sistemas Operacionais', 1, 60),
(14, 'Teoria da Computação', 1, 60),
(15, 'Desenvolvimento Web', 1, 60),
(16, 'Gestão de Projetos', 2, 40),
(17, 'Banco de Dados II', 1, 60),
(18, 'Cálculo Numérico', 2, 60),
(19, 'Inteligência Artificial', 1, 60),
(20, 'Empreendedorismo', 2, 40)
ON CONFLICT (dis_id) DO NOTHING;

-- 5.4 COMPANHAMENTO_DISCIPLINA
INSERT INTO acompanhamento_disciplina (asdis_id, asdis_disciplina, asdis_acompanhamento)
VALUES
(1, 1, 1),
(2, 6, 1),
(3, 4, 1),
(4, 12, 1),
(5, 11, 2),
(6, 2, 2),
(7, 3, 3),
(8, 7, 3)
ON CONFLICT (asdis_id) DO NOTHING;