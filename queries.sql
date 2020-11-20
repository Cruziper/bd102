---------------------------------------------------------------------
--1.

SELECT nome
FROM concelho
NATURAL JOIN
    (SELECT num_concelho, MAX(sum_vendas)
    FROM
        (SELECT num_concelho, COUNT(num_concelho) as sum_vendas
        FROM venda_farmacia v
        NATURAL JOIN instituicao i
        WHERE v.inst = i.nome and data_registo = CURRENT_DATE
        GROUP BY num_concelho) as vendas
    GROUP BY num_concelho) as max_vendas;


---------------------------------------------------------------------
--2.

SELECT regiao, nome AS medico
FROM medico
NATURAL JOIN
	(SELECT nome AS regiao, num_cedula
	 FROM regiao
	 NATURAL JOIN
		(SELECT t4.*
		 FROM (SELECT num_regiao, num_cedula, n_presc,
      		 		  ROW_NUMBER() OVER (PARTITION BY num_regiao ORDER BY n_presc DESC) as seqnum
     		   FROM (SELECT num_regiao, num_cedula, COUNT(num_cedula) AS n_presc
					 FROM (SELECT *
				  		   FROM instituicao
				  		   JOIN (SELECT *
								 FROm prescricao
								 NATURAL JOIN consulta
						   		 WHERE consulta.data BETWEEN '2019-01-01' AND '2019-06-30') AS t1
				  		   ON instituicao.nome = t1.nome_instituicao) as t2
					 GROUP BY num_regiao, num_cedula) as t3
      		  ) AS t4
		 WHERE seqnum = 1) AS t5) AS t6;


--------------------------------------------------------------------
--3.

SELECT nome_medico, num_cedula FROM
concelho c natural join 
    (SELECT nome_medico, num_cedula, num_concelho FROM
    instituicao i natural join
        (SELECT num_cedula, m.nome as nome_medico, nome_instituicao FROM
        medico m natural join consulta c natural join prescricao p
        where p.substancia = 'Aspirina' and date_part('year', c.data) = date_part('year', CURRENT_DATE)) as num_p
    where i.nome = num_p.nome_instituicao and i.tipo = 'farmacia') as t
where c.nome = 'Arouca';

--------------------------------------------------------------------
--4.

SELECT num_doente
FROM consulta 
WHERE num_doente IN (SELECT num_doente FROM analise a WHERE date_part('month', a.data) = date_part('month', CURRENT_DATE))
AND num_doente NOT IN (SELECT num_doente FROM prescricao p WHERE date_part('month', p.data) = date_part('month', CURRENT_DATE));