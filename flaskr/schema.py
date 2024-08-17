instructions = [
    "SET FOREIGN_KEY_CHECKS=0;",
    "DROP TABLE IF EXISTS user;",
    "DROP TABLE IF EXISTS admin;",
    "DROP TABLE IF EXISTS datospersonales;",
    "DROP TABLE IF EXISTS nivelsocioeconomico;",
    "DROP TABLE IF EXISTS nivelmotivacional;",
    "DROP TABLE IF EXISTS nivelautoestima;",
    "DROP TABLE IF EXISTS nivelbienestarpsicologico;",
    "DROP TABLE IF EXISTS nivelhabitosestudio;",
    "DROP TABLE IF EXISTS nivelestrategiasaprendizaje;",
    "DROP TABLE IF EXISTS calidadinstitucion;",
    "DROP TABLE IF EXISTS datab;",
    "DROP TABLE IF EXISTS alumno;",
    "DROP TABLE IF EXISTS materias;",
    "DROP TABLE IF EXISTS semestre;",
    "DROP TABLE IF EXISTS inscripcion;",
    "DROP TABLE IF EXISTS evaluacion;",
    "SET FOREIGN_KEY_CHECKS=1;",
    """
        CREATE TABLE user(
            user_id INT NOT NULL UNIQUE,
            email VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(500) NOT NULL,
            username VARCHAR(50) UNIQUE NOT NULL,
            bloque VARCHAR(10) NOT NULL,
            preparatoria VARCHAR(50) NOT NULL,
            seccion VARCHAR(10) NOT NULL,
            semestre INT NOT NULL,
            admin INT DEFAULT 0,
            created_at TIMESTAMP NOT NULL DEFAULT (NOW()),
            PRIMARY KEY(user_id)
        )
    """,
    """
        CREATE TABLE datospersonales(
            dp_id INT NOT NULL UNIQUE,
            sexo INT NOT NULL, 
            edad INT NOT  NULL,
            escuelaprocedencia INT NOT NULL,  
            foraneo INT NOT NULL,
            trabajas INT NOT NULL,
            becado INT NOT NULL,
            discapacidad INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT (NOW()),
            FOREIGN KEY(dp_id) REFERENCES user(user_id),
            PRIMARY KEY(dp_id)
        )
    """,
    """
        CREATE TABLE nivelsocioeconomico(
            ns_id INT NOT NULL UNIQUE,
            nivel_estudios_jh INT NOT NULL,
            numero_banos INT NOT NULL,
            numero_autos INT NOT NULL,
            internet INT NOT NULL,
            numero_pt INT NOT NULL,
            numero_cd INT NOT NULL,
            promedio INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT (NOW()),
            FOREIGN KEY(ns_id) REFERENCES user(user_id),
            PRIMARY KEY(ns_id)
        )
    """,
    """
        CREATE TABLE nivelmotivacional(
            nm_id INT NOT NULL UNIQUE,
            p1 INT NOT NULL,
            p2 INT NOT NULL,
            p3 INT NOT NULL,
            p4 INT NOT NULL,
            p5 INT NOT NULL,
            p6 INT NOT NULL,
            p7 INT NOT NULL,
            p8 INT NOT NULL,
            p9 INT NOT NULL,
            p10 INT NOT NULL,
            promedio INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT (NOW()),
            FOREIGN KEY(nm_id) REFERENCES user(user_id),
            PRIMARY KEY(nm_id)
        )
    """,
    """
        CREATE TABLE nivelautoestima(
            na_id INT NOT NULL UNIQUE,
            p1 INT NOT NULL,
            p2 INT NOT NULL,
            p3 INT NOT NULL,
            p4 INT NOT NULL,
            p5 INT NOT NULL,
            p6 INT NOT NULL,
            p7 INT NOT NULL,
            p8 INT NOT NULL,
            p9 INT NOT NULL,
            p10 INT NOT NULL,
            promedio INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT (NOW()),
            FOREIGN KEY(na_id) REFERENCES user(user_id),
            PRIMARY KEY(na_id)
        )
    """,
    """
        CREATE TABLE nivelbienestarpsicologico(
            nbp_id INT NOT NULL UNIQUE,
            p1 INT NOT NULL,
            p2 INT NOT NULL,
            p3 INT NOT NULL,
            p4 INT NOT NULL,
            p5 INT NOT NULL,
            p6 INT NOT NULL,
            p7 INT NOT NULL,
            p8 INT NOT NULL,
            p9 INT NOT NULL,
            p10 INT NOT NULL,           
            promedio INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT (NOW()),
            FOREIGN KEY(nbp_id) REFERENCES user(user_id),
            PRIMARY KEY(nbp_id)
        )
    """,
    """
        CREATE TABLE nivelhabitosestudio(
            nhe_id INT NOT NULL UNIQUE,
            p1 INT NOT NULL,
            p2 INT NOT NULL,
            p3 INT NOT NULL,
            p4 INT NOT NULL,
            p5 INT NOT NULL,
            p6 INT NOT NULL,
            p7 INT NOT NULL,
            p8 INT NOT NULL,
            p9 INT NOT NULL,
            p10 INT NOT NULL,
            promedio INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT (NOW()),
            FOREIGN KEY(nhe_id) REFERENCES user(user_id),
            PRIMARY KEY(nhe_id)
        )
    """,
    """
        CREATE TABLE nivelestrategiasaprendizaje(
            nea_id INT NOT NULL UNIQUE,
            p1 INT NOT NULL,
            p2 INT NOT NULL,
            p3 INT NOT NULL,
            p4 INT NOT NULL,
            p5 INT NOT NULL,
            promedio INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT (NOW()),
            FOREIGN KEY(nea_id) REFERENCES user(user_id),
            PRIMARY KEY(nea_id)
        )
    """,
    """
        CREATE TABLE calidadinstitucion(
            ci_id INT NOT NULL UNIQUE,
            p1 INT NOT NULL,
            p2 INT NOT NULL,
            p3 INT NOT NULL,
            p4 INT NOT NULL,
            p5 INT NOT NULL,
            clase INT NOT NULL,
            promedio INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT (NOW()),
            FOREIGN KEY(ci_id) REFERENCES user(user_id),
            PRIMARY KEY(ci_id)
        )
    """,
    """
        CREATE TABLE datab(
            db_id INT NOT NULL UNIQUE,
            sexo INT NOT NULL, 
            edad INT NOT  NULL,
            escuelaprocedencia INT NOT NULL,  
            foraneo INT NOT NULL,
            trabajas INT NOT NULL,
            becado INT NOT NULL,
            discapacidad INT NOT NULL,
            ns INT NOT NULL,
            nm INT NOT NULL,
            na INT NOT NULL,
            nbp INT NOT NULL,
            nhe INT NOT NULL,
            nea INT NOT NULL,
            ci INT NOT NULL,
            clase INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT (NOW()),
            FOREIGN KEY(db_id) REFERENCES user(user_id),
            PRIMARY KEY(db_id)
        )
    """,
    """ 
        CREATE TABLE alumno(
            alumno_id int not null,
            username varchar(50) not null,
            semestre int not null,
            create_at timestamp default (now()),
            primary key (alumno_id)
        )
    """,
    """
        CREATE TABLE materias(
            materias_id int not null auto_increment,
            nombre varchar(100),
            primary key (materias_id)
        )
    """,
    """ 
    CREATE TABLE semestre(
        semestre_id int not null,
        primary key (semestre_id)
    )
    """,
    """
    CREATE TABLE inscripcion(
        inscripcion_id int not null auto_increment,
        alumno_id int not null,
        materias_id int not null,
        semestre_id int not null,
        FOREIGN KEY (alumno_id) REFERENCES alumno(alumno_id),
        FOREIGN KEY (materias_id) REFERENCES materias(materias_id),
        FOREIGN KEY (semestre_id) REFERENCES semestre(semestre_id),
        primary key (inscripcion_id)
    )
    """,
    """
    CREATE TABLE evaluacion(
        evaluacion_id int not null auto_increment,
        inscripcion_id int not null,
        valor1 int not null,
        valor2 int not null,
        valor3 int not null,
        valor4 int not null,
        foreign key (inscripcion_id) references inscripcion(inscripcion_id),
        primary key (evaluacion_id)
    )
    """,
    """insert into semestre(semestre_id) values (1);""",
    """insert into semestre(semestre_id) values (2);""",
    """insert into semestre(semestre_id) values (3);""",
    """insert into semestre(semestre_id) values (4);""",
    """insert into semestre(semestre_id) values (5);""",
    """insert into semestre(semestre_id) values (6);""",
    """insert into materias(nombre) values ("Algebra");""",
    """insert into materias(nombre) values ("Química I");""",
    """insert into materias(nombre) values ("Lenguaje y Procesos Comunicativos");""",
    """insert into materias(nombre) values ("Lengua Extranjera I");""",
    """insert into materias(nombre) values ("Habilidades Digitales");""",
    """insert into materias(nombre) values ("Historia Universal");""",
    """insert into materias(nombre) values ("Psicología en la Adolescencia I");""",
    """insert into materias(nombre) values ("Lógica y Argumentación");""",
    """insert into materias(nombre) values ("Geometría Plana y Trigonometría Plana");""",
    """insert into materias(nombre) values ("Química II");""",
    """insert into materias(nombre) values ("Lenguaje y Medios de Expresión");""",
    """insert into materias(nombre) values ("Lengua Extranjera II");""",
    """insert into materias(nombre) values ("Sistematización de Datos");""",
    """insert into materias(nombre) values ("Historia del Siglo XX");""",
    """insert into materias(nombre) values ("Psicología en la Adolescencia II");""",
    """insert into materias(nombre) values ("Filosofía Práctica");""",
    """insert into materias(nombre) values ("Geometría Analítica");""",
    """insert into materias(nombre) values ("Biología I: Del Átomo al Hombre");""",
    """insert into materias(nombre) values ("Lenguaje y Procesos de Escritura para la Investigación");""",
    """insert into materias(nombre) values ("Lengua Extranjera III");""",
    """insert into materias(nombre) values ("Manejo de Datos y Comunicaciones");""",
    """insert into materias(nombre) values ("Historia de la Identidad Mexicana");""",
    """insert into materias(nombre) values ("Funciones");""",
    """insert into materias(nombre) values ("Biología II: Del Hombre a la Biosfera");""",
    """insert into materias(nombre) values ("Lenguaje y Difusión para la Investigación");""",
    """insert into materias(nombre) values ("Lengua Extranjera IV");""",
    """insert into materias(nombre) values ("Entornos de Desarrollo a Través de Tecnologías Digitales");""",
    """insert into materias(nombre) values ("Historia de la Sociedad Mexicana");""",
    """insert into materias(nombre) values ("Cálculo");""",
    """insert into materias(nombre) values ("Física I");""",
    """insert into materias(nombre) values ("Narrativa Literaria");""",
    """insert into materias(nombre) values ("Lengua Extranjera V");""",
    """insert into materias(nombre) values ("Innovación de Aplicaciones");""",
    """insert into materias(nombre) values ("Introducción a la Economía");""",
    """insert into materias(nombre) values ("Análisis de Eventos");""",
    """insert into materias(nombre) values ("Física II");""",
    """insert into materias(nombre) values ("Expresión Literaria");""",
    """insert into materias(nombre) values ("Lengua Extranjera VI");""",
    """insert into materias(nombre) values ("Desarrollo de Habilidades Digitales a Través de Dispositivos Autónomos");""",
    """insert into materias(nombre) values ("Problemas Socioeconómicos de México");""",
]