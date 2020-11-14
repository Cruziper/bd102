drop table if exists regiao cascade;
drop table if exists concelho cascade;
drop table if exists instituicao cascade;
drop table if exists medico cascade;
drop table if exists consulta cascade;
drop table if exists prescricao cascade;
drop table if exists analise cascade;
drop table if exists venda_farmacia cascade;
drop table if exists prescricao_venda cascade;

drop type if exists nome_regiao;
drop type if exists nome_concelho;
drop type if exists tipo;

create type nome_regiao as ENUM ('Norte', 'Centro', 'Lisboa', 'Alentejo', 'Algarve', 'Madeira', 'Açores');
create type nome_concelho as ENUM ('Abrantes', 'Águeda', 'Aguiar da Beira', 'Alandroal', 'Albergaria-a-Velha', 'Albufeira', 'Alcácer do Sal', 'Alcanena', 'Alcobaça', 'Alcochete', 'Alcoutim', 'Alenquer', 'Alfândega da Fé', 'Alijó', 'Aljezur', 'Aljustrel', 'Almada', 'Almeida', 'Almeirim', 'Almodôvar', 'Alpiarça', 'Alter do Chão', 'Alvaiázere', 'Alvito', 'Amadora', 'Amarante', 'Amares', 'Anadia', 'Angra do Heroísmo', 'Ansião', 'Arcos de Valdevez', 'Arganil', 'Armamar', 'Arouca', 'Arraiolos', 'Arronches', 'Arruda dos Vinhos', 'Aveiro', 'Avis', 'Azambuja', 'Baião', 'Barcelos', 'Barrancos', 'Barreiro', 'Batalha', 'Beja', 'Belmonte', 'Benavente', 'Bombarral', 'Borba', 'Boticas', 'Braga', 'Bragança', 'Cabeceiras de Basto', 'Cadaval', 'Caldas da Rainha', 'Calheta (Madeira)', 'Calheta (São Jorge)', 'Caminha', 'Campo Maior', 'Cantanhede', 'Carrazeda de Ansiães', 'Carregal do Sal', 'Cartaxo', 'Cascais', 'Castanheira de Pêra', 'Castelo Branco', 'Castelo de Paiva', 'Castelo de Vide', 'Castro Daire', 'Castro Marim', 'Castro Verde', 'Celorico da Beira', 'Celorico de Basto', 'Chamusca', 'Chaves', 'Cinfães', 'Coimbra', 'Condeixa-a-Nova', 'Constância', 'Coruche', 'Corvo', 'Covilhã', 'Crato', 'Cuba', 'Câmara de Lobos', 'Elvas', 'Entroncamento', 'Espinho', 'Esposende', 'Estarreja', 'Estremoz', 'Évora', 'Fafe', 'Faro', 'Felgueiras', 'Ferreira do Alentejo', 'Ferreira do Zêzere', 'Figueira da Foz', 'Figueira de Castelo Rodrigo', 'Figueiró dos Vinhos', 'Fornos de Algodres', 'Freixo de Espada à Cinta', 'Fronteira', 'Funchal', 'Fundão', 'Gavião', 'Golegã', 'Gondomar', 'Gouveia', 'Grândola', 'Guarda', 'Guimarães', 'Góis', 'Horta', 'Idanha-a-Nova', 'Ílhavo', 'Lagoa (Algarve)', 'Lagoa (São Miguel)', 'Lagos', 'Lajes das Flores', 'Lajes do Pico', 'Lamego', 'Leiria', 'Lisboa', 'Loulé', 'Loures', 'Lourinhã', 'Lousã', 'Lousada', 'Mação', 'Macedo de Cavaleiros', 'Machico', 'Madalena', 'Mafra', 'Maia', 'Mangualde', 'Manteigas', 'Marco de Canaveses', 'Marinha Grande', 'Marvão', 'Matosinhos', 'Mealhada', 'Meda', 'Melgaço', 'Mesão Frio', 'Mira', 'Miranda do Corvo', 'Miranda do Douro', 'Mirandela', 'Mogadouro', 'Moimenta da Beira', 'Moita', 'Monção', 'Monchique', 'Mondim de Basto', 'Monforte', 'Montalegre', 'Montemor-o-Novo', 'Montemor-o-Velho', 'Montijo', 'Mora', 'Mortágua', 'Moura', 'Mourão', 'Murça', 'Murtosa', 'Mértola', 'Nazaré', 'Nelas', 'Nisa', 'Nordeste', 'Óbidos', 'Odemira', 'Odivelas', 'Oeiras', 'Oleiros', 'Olhão', 'Oliveira de Azeméis', 'Oliveira de Frades', 'Oliveira do Bairro', 'Oliveira do Hospital', 'Ourique', 'Ourém', 'Ovar', 'Paços de Ferreira', 'Palmela', 'Pampilhosa da Serra', 'Paredes', 'Paredes de Coura', 'Pedrógão Grande', 'Penacova', 'Penafiel', 'Penalva do Castelo', 'Penamacor', 'Penedono', 'Penela', 'Peniche', 'Peso da Régua', 'Pinhel', 'Pombal', 'Ponta Delgada', 'Ponta do Sol', 'Ponte da Barca', 'Ponte de Lima', 'Ponte de Sor', 'Portalegre', 'Portel', 'Portimão', 'Porto', 'Porto Moniz', 'Porto Santo', 'Porto de Mós', 'Povoação', 'Praia da Vitória', 'Proença-a-Nova', 'Póvoa de Lanhoso', 'Póvoa de Varzim', 'Redondo', 'Reguengos de Monsaraz', 'Resende', 'Ribeira Brava', 'Ribeira Grande', 'Ribeira de Pena', 'Rio Maior', 'Sabrosa', 'Sabugal', 'Salvaterra de Magos', 'Santa Comba Dão', 'Santa Cruz', 'Santa Cruz da Graciosa', 'Santa Cruz das Flores', 'Santa Maria da Feira', 'Santa Marta de Penaguião', 'Santana', 'Santarém', 'Santiago do Cacém', 'Santo Tirso', 'São Brás de Alportel', 'São João da Madeira', 'São João da Pesqueira', 'São Pedro do Sul', 'São Roque do Pico', 'São Vicente', 'Sardoal', 'Sátão', 'Seia', 'Seixal', 'Sernancelhe', 'Serpa', 'Sertã', 'Sesimbra', 'Setúbal', 'Sever do Vouga', 'Silves', 'Sines', 'Sintra', 'Sobral de Monte Agraço', 'Soure', 'Sousel', 'Tábua', 'Tabuaço', 'Tarouca', 'Tavira', 'Terras de Bouro', 'Tomar', 'Tondela', 'Torre de Moncorvo', 'Torres Novas', 'Torres Vedras', 'Trancoso', 'Trofa', 'Vagos', 'Vale de Cambra', 'Valença', 'Valongo', 'Valpaços', 'Velas', 'Vendas Novas', 'Viana do Alentejo', 'Viana do Castelo', 'Vidigueira', 'Vieira do Minho', 'Vila Flor', 'Vila Franca de Xira', 'Vila Franca do Campo', 'Vila Nova da Barquinha', 'Vila Nova de Cerveira', 'Vila Nova de Famalicão', 'Vila Nova de Foz Côa', 'Vila Nova de Gaia', 'Vila Nova de Paiva', 'Vila Nova de Poiares', 'Vila Pouca de Aguiar',' Vila Real', 'Vila Real de Santo António', 'Vila Velha de Ródão', 'Vila Verde', 'Vila Viçosa', 'Vila de Rei', 'Vila do Bispo', 'Vila do Conde', 'Vila do Porto', 'Vimioso', 'Vinhais', 'Viseu', 'Vizela', 'Vouzela');
create type tipo as ENUM ('farmacia', 'laboratorio', 'clinica', 'hospital');

create table regiao(
    num_regiao integer not null unique,
    nome nome_regiao not null,
    num_habitantes integer not null,
    constraint pk_regiao primary key(num_regiao)
);

create table concelho(
    num_concelho integer not null,
    num_regiao integer not null,
    nome nome_concelho not null,
    num_habitantes integer not null,
    constraint pk_concelho primary key(num_concelho, num_regiao),
    constraint fk_regiao foreign key(num_regiao) 
        references regiao
);

create table instituicao(
    nome char(100) not null,
    tipo tipo not null,
    num_regiao integer not null,
    num_concelho integer not null,
    constraint pk_instituicao primary key(nome),
    constraint fk_concelho foreign key(num_concelho, num_regiao) 
        references concelho
);

create table medico(
    num_cedula integer not null unique,
    nome char(100) not null,
    especialidade char(100) not null,
    constraint pk_medico primary key(num_cedula)
);

create table consulta(
    num_cedula integer not null,
    num_doente integer not null,
    data date not null,
    nome_instituicao char(100) not null,
    constraint pk_consulta primary key(num_cedula, num_doente, data),
    constraint fk_medico foreign key(num_cedula) 
        references medico,
    constraint fk_instituicao foreign key(nome_instituicao) 
        references instituicao
);

create table prescricao(
    num_cedula integer not null,
    num_doente integer not null,
    data date not null,
    substancia char(100) not null,
    quant integer not null,
    constraint pk_prescricao primary key(num_cedula, num_doente, data, substancia),
    constraint fk_consulta foreign key(num_cedula, num_doente, data) 
        references consulta
);

create table analise(
    num_analise integer not null unique,
    especialidade char(100) not null,
    num_cedula integer not null,
    num_doente integer not null,
    data date not null,
    data_registo date not null,
    nome char(100) not null,
    quant integer not null,
    inst char(100) not null,
    constraint pk_analise primary key(num_analise),
    constraint fk_consulta foreign key(num_cedula, num_doente, data) 
        references consulta,
    constraint fk_instituicao foreign key(nome) 
        references instituicao
);

create table venda_farmacia(
    num_venda integer not null unique,
    data_registo date not null,
    substancia char(100) not null,
    quant integer not null,
    preco integer not null,
    inst char(100) not null,
    constraint pk_venda_farmacia primary key(num_venda),
    constraint fk_instituicao foreign key(inst) 
        references instituicao
);

create table prescricao_venda(
    num_cedula integer not null,
    num_doente integer not null,
    data date not null,
    substancia char(100) not null,
    num_venda integer not null,
    constraint pk_prescricao_venda primary key(num_cedula, num_doente, data, substancia, num_venda),
    constraint fk_venda_farmacia foreign key(num_venda)
        references venda_farmacia,
    constraint fk_prescricao foreign key(num_cedula, num_doente, data, substancia) 
        references prescricao
);
