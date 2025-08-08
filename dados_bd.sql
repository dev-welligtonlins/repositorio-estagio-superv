use estagio;

#ADMINISTRADOR
insert ignore into ADMINISTRADOR (adm_id, adm_nome, adm_cpf, adm_email, adm_usuario, permissao) 
 values (1, "admin_visitante", "29748638049", "visitante@admin.com.br", 1, 1);
	

#AVISOS 
insert ignore into AVISOS (avi_id, avi_titulo, avi_descricao, avi_data, avi_arquivos, avi_administrador, avi_mostrar) 
values (1, "Novo semestre", "Voltas a aulas devem ser com a documentação em dia!", '2025-08-08', null, 1, true),
		(2, "Novo semestre", "Voltas a aulas devem ser com a documentação em dia!", '2025-08-08', null, 1, true),
        (3, "Novo semestre", "Voltas a aulas devem ser com a documentação em dia!", '2025-08-08', null, 1, true),
        (4, "Novo semestre", "Voltas a aulas devem ser com a documentação em dia!", '2025-08-08', null, 1, true);		
        
 #FEEDBACKS
insert ignore into FEEDBACKS (fee_id, fee_titulo, fee_descricao, fee_data, fee_arquivo, fee_acompanhamento)
values (1, 'Relatório Semanal', 'Relatório de desempenho da equipe', '2025-08-01 09:00:00', null, 1);
#(2, 'Plano de Aula', 'Plano de aula para a disciplina de Algoritmos', '2025-08-02 14:30:00', 'plano_algoritmos.pdf', 102),
#(3, 'Checklist de Tarefas', 'Lista de tarefas pendentes da semana', '2025-08-03 10:15:00', 'checklist_tarefas.pdf', 101),
#(4, 'Análise de Dados', 'Resumo da análise de desempenho acadêmico', '2025-08-04 16:00:00', 'analise_dados.xlsx', 103),
#(5, 'Reunião de Alinhamento', 'Resumo da reunião do dia 01/08', '2025-08-05 11:45:00', 'resumo_reuniao.txt', 101);

#ACOMPANHAMENTO
insert ignore into ACOMPANHAMENTO (aco_id, aco_semestre, aco_inicio, aco_fim, aco_aluno_pcd, aco_monitor, aco_tutor)
 values (1, '2023-1', '2023-02-01', '2023-06-30', 1, 1, 2),
		(2, '2023-2', '2023-08-01', '2023-12-15', 2, 2, 2),
		(3, '2024-1', '2024-02-05', '2024-06-25', 3, 1, 1);
 #ALUNOS
insert ignore into ALUNO_PCD (alu_id, alu_nome, alu_cpf, alu_genero, alu_email_pessoal, alu_email_institucional,
	alu_telefone, alu_endereco_cep, alu_endereco_descricao, alu_endereco_cidade, alu_matricula, alu_deficiencias,
    alu_curso, alu_periodo_academico, alu_data_nascimento, alu_ativo, alu_usuario, permissao)
values (2, "aluno_01", "48913276007", 'M', "aluno_01@g.com.br", "aluno_01@lala.br", "8890044-4432", "69443-201",
	"rua vinte, bairro 10", "RB", "201000300942", "n/a", 6, "5", '2025-08-08', true, null, 2),
    (3, "aluno_02", "01826384050", 'M', "aluno_01@g.com.br", "aluno_01@lala.br", "8890044-4432", "69443-201",
	"rua vinte, bairro 10", "RB", "201000300942", "n/a", 3, "6", '2025-08-08', true, null, 2),
    (4, "aluno_03", "47218937009", 'M', "aluno_01@g.com.br", "aluno_01@lala.br", "8890044-4432", "69443-201",
	"rua vinte, bairro 10", "RB", "201000300942", "n/a", 4, "7", '2025-08-08', true, null, 2),
    (5, "aluno_04", "10945268040", 'M', "aluno_01@g.com.br", "aluno_01@lala.br", "8890044-4432", "69443-201",
	"rua vinte, bairro 10", "RB", "201000300942", "n/a", 2, "5", '2025-08-08', true, null, 2);

#MONITORES
insert ignore into MONITOR (mon_id, mon_nome, mon_cpf, mon_genero, mon_email_pessoal, mon_email_institucional, mon_telefone, mon_endereco_cep, mon_endereco_descricao, mon_endereco_cidade, mon_matricula, mon_curso, mon_periodo_academico, mon_ativo, mon_usuario, permissao
) values
( 1, 'monitor_1', '01826384050', 'M', 'monitor_1@email.com', 'monitor_1@universidade.edu', 
'(11)91234-5678', '12345678', 'Rua das Flores, 123','SP', '20201234567', 1,'5', true, null, 2
),
( 2, 'monitor_2', '47218937009', 'F', 'monitor_2@email.com', 'monitor_2@universidade.edu', 
'(21)99876-5432', '87654321', 'Av. Central, 456', 'RJ', '20206543210', 2, '3º período', true, null, 2
);

#TUTORES
insert ignore into TUTOR (tut_id, tut_nome, tut_cpf, tut_genero, tut_email_pessoal, tut_email_institucional, tut_telefone, tut_endereco_cep, tut_endereco_descricao, tut_endereco_cidade,  tut_matricula,  tut_curso, tut_periodo_academico, tut_ativo, tut_usuario, permissao
) values
(1, 'tutor_1', '01826384050', 'F', 'tutor_1@email.com', 'tutor_1@universidade.edu',
'(11)91234-5678', '01234567', 'Rua A, 123', 'SP', '20201234567', 1, '4º período', true, null, 2
),
(2, 'tutor_2', '47218937009', 'M', 'tutor_1@email.com', 'tutor_1@universidade.edu',
'(21)97654-3210', '76543210', 'Av. B, 456', 'RJ', '20206543210', 2, '6º período', true, null,  2
);

#INTERPRETES
insert ignore into INTERPRETE(int_id, int_nome, int_cpf, int_genero, int_email_pessoal, int_email_institucional, int_telefone, int_ativo, int_usuario, permissao
) values 
(1, 'interprete_1', '10945268040', 'M', 'interprete_1@email.com', 'interprete_1@universidade.edu', '(31)99876-5432', true, null,  2),
(2, 'interprete_2', '76103459020', 'F', 'interprete_2@email.com', 'interprete_2@universidade.edu', '(41)98765-1234', true, null,  2
);


#CCET
insert ignore CURSOS (cur_id, cur_nome, cur_quant_periodos, cur_turno)
values  (1, "Sistemas de Informação", 8, 4),
		(2, "Engenharia Civil", 10, 4),
        (3, "Engenharia Elétrica", 10, 4),
        (4, "Matemática", 8, 2);

    
#DISCIPLINAS
insert ignore into DISCIPLINAS (dis_id, dis_nome, dis_curso, dis_carga_horaria)
values (1, 'Algoritmos e Estruturas de Dados', 1, 60),
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
(20, 'Empreendedorismo', 2, 40);