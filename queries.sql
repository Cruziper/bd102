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

SELECT num_regiao, num_p.nome FROM
regiao r natural join
    (SELECT m.nome, num_regiao, COUNT(num_cedula) as prescricoes FROM
    medico m natural join prescricao natural join instituicao i natural join consulta c
    where i.nome = c.nome_instituicao and m.nome != i.nome and data between '2019-01-01' and '2019-06-30'
    GROUP BY m.nome, num_regiao) as num_r
WHERE r.nome != num_r.nome
GROUP BY num_regiao;


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