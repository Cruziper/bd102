--regiao (num_regiao, nome (regiao), num_habitantes)

insert into regiao values(1, 'Norte', 3689);
insert into regiao values(2, 'Centro', 2327);
insert into regiao values(3, 'Lisboa', 504718);
insert into regiao values(4, 'Alentejo', 166706);
insert into regiao values(5, 'Algarve', 451006);
insert into regiao values(6, 'Madeira', 267785);
insert into regiao values(7, 'Açores', 246746);


--concelho (num_concelho, num_regiao, nome (concelho), num_habitantes)

insert into concelho values(65, 3,'Cascais', 210889);
insert into concelho values(1, 2,'Abrantes', 39325);
insert into concelho values(67, 2,'Castelo Branco', 225916);
insert into concelho values(93, 4,'Évora', 56596);
insert into concelho values(210, 1,'Porto', 214349);
insert into concelho values(257, 3,'Sintra', 381728);
insert into concelho values(306, 2,'Viseu', 99274);
insert into concelho values(105, 6,'Funchal', 111541);


--instituicao (nome (instituicao), tipo, num_regiao, num_concelho)

insert into instituicao values('A', 'farmacia', 3, 65);
insert into instituicao values('B', 'laboratorio', 2, 1);
insert into instituicao values('C', 'clinica', 2, 67);
insert into instituicao values('D', 'hospital', 4, 93);
insert into instituicao values('E', 'laboratorio', 1, 210);
insert into instituicao values('F', 'clinica', 3, 257);
insert into instituicao values('G', 'farmacia', 2, 306);
insert into instituicao values('H', 'hospital', 6, 105);


--medico (num_cedula, nome (medico), especialidade)

insert into medico values(1, 'Joaquim', 'Cardiologia');
insert into medico values(2, 'Alberto', 'Pediatria');
insert into medico values(3, 'Jose', 'Dermatologia');
insert into medico values(4, 'Carolina', 'Cardiologia');
insert into medico values(5, 'Carlota', 'Neurocirurgia');
insert into medico values(6, 'Joao', 'Pediatria');
insert into medico values(7, 'Catarina', 'Dermatologia');
insert into medico values(8, 'Pedro', 'Neurocirurgia');


--consulta (num_cedula, num_doente, data, nome_instituicao)

insert into consulta values(1, 2, '2020-12-03', 'A');
insert into consulta values(3, 1, '2020-12-22', 'B');
insert into consulta values(5, 3, '2020-12-13', 'C');
insert into consulta values(1, 5, '2020-12-13', 'A');
insert into consulta values(4, 6, '2020-12-27', 'D');
insert into consulta values(6, 3, '2020-12-06', 'B');
insert into consulta values(7, 8, '2020-12-22', 'G');
insert into consulta values(5, 7, '2020-12-05', 'C');


--prescricao (num_cedula, num_doente, data, substancia, quant)

insert into prescricao values(1, 2, '2020-12-03', 'Calcitrin', 2);
insert into prescricao values(3, 1, '2020-12-22', 'Ibuprofeno', 1);
insert into prescricao values(5, 3, '2020-12-13', 'Carbonato de Calcio', 5);
insert into prescricao values(5, 3, '2020-12-13', 'Paracetamol', 3);
insert into prescricao values(4, 6, '2020-12-27', 'Gliclazida', 3);
insert into prescricao values(6, 3, '2020-12-06', 'Diazepam', 6);
insert into prescricao values(3, 1, '2020-12-22', 'Amoxicilina', 4);
insert into prescricao values(5, 7, '2020-12-05', 'Sulfadiazina', 5);


--analise (num_analise, especialidade, num_cedula, num_doente, data, data_registo, nome, quant, inst)

insert into analise values(1, 'Cardiologia', 1, 2, '2020-12-03', '2020-12-03', 'A', 2, 'A');
insert into analise values(2, 'Dermatologia', 3, 1, '2020-12-22', '2020-12-22', 'B', 1, 'B');
insert into analise values(3, 'Cardiologia', 4, 6, '2020-12-27', '2020-12-27', 'C', 3, 'D');
insert into analise values(4, 'Dermatologia', 3, 1, '2020-12-22', '2020-12-22', 'D', 4, 'B');


--venda_farmacia (num_venda, data_registo, substancia, quant, preco, inst)

insert into venda_farmacia values(1, '2020-12-03', 'Calcitrin', 2, 8, 'A');
insert into venda_farmacia values(2, '2020-12-22', 'Ibuprofeno', 1, 7, 'B');
insert into venda_farmacia values(3, '2020-12-13', 'Carbonato de Calcio', 5, 15, 'C');
insert into venda_farmacia values(4, '2020-12-13', 'Paracetamol', 3, 12, 'D');
insert into venda_farmacia values(5, '2020-12-27', 'Gliclazida', 3, 10, 'E');
insert into venda_farmacia values(6, '2020-12-06', 'Diazepam', 6, 30, 'F');
insert into venda_farmacia values(7, '2020-12-22', 'Amoxicilina', 4, 25, 'G');
insert into venda_farmacia values(8, '2020-12-05', 'Sulfadiazina', 5, 28, 'H');


--prescricao_venda (num_cedula, num_doente, data, substancia, num_venda)

insert into prescricao_venda values(1, 2, '2020-12-03', 'Calcitrin', 1);
insert into prescricao_venda values(3, 1, '2020-12-22', 'Ibuprofeno', 2);
insert into prescricao_venda values(5, 3, '2020-12-13', 'Carbonato de Calcio', 3);
insert into prescricao_venda values(5, 3, '2020-12-13', 'Paracetamol', 4);
insert into prescricao_venda values(4, 6, '2020-12-27', 'Gliclazida', 5);
insert into prescricao_venda values(6, 3, '2020-12-06', 'Diazepam', 6);
insert into prescricao_venda values(3, 1, '2020-12-22', 'Amoxicilina', 7);
insert into prescricao_venda values(5, 7, '2020-12-05', 'Sulfadiazina', 8);
