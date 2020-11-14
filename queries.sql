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

SELECT * FROM
medico m natural join consulta c natural join prescricao p natural join instituicao i
WHERE c.nome_instituicao = i.nome and m.nome != i.nome and p.substancia = 'Calcitrin' and i.tipo = 'farmacia' and c.data = '2020-11-03';


--------------------------------------------------------------------
--4.

SELECT num_doente
FROM consulta 
WHERE num_doente IN (SELECT num_doente FROM analise a WHERE date_trunc('month', a.data) = date_trunc('month', CURRENT_DATE))
AND num_doente NOT IN (SELECT num_doente FROM prescricao p WHERE date_trunc('month', p.data) = date_trunc('month', CURRENT_DATE));