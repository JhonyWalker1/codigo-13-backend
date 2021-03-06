
DELIMITER $$

DROP PROCEDURE IF EXISTS sp_matricular_alumno
 $$


CREATE PROCEDURE sp_matricular_alumno(IN alu_id INT, IN niv_id INT, IN mod_id INT)
BEGIN
    --variables locales
    DECLARE matId INT;
    DECLARE curId INT;
    DECLARE totalCursos INT;
    set matId = 0;
    set curId = 1;
    set totalCursos = 0;


    --insertar datos en la tabla matricula
    insert into tbl_matricula(alumno_id, nivel_id, modulo_id)
    values (alu_id, niv_id, mod_id);

    select max(matricula_id) into matId from tbl_matricula;

    select count(*) into totalCursos from tbl_curso;

    while curId <= totalCursos DO
        --insertar datos en la tabla matricula_detalle
        insert into tbl_matricula_curso(matricula_id, curso_id)
        values (matId, curId);

        set curId = curId + 1;

    end while;

END
$$

DELIMITER ;

call sp_matricular_alumno(5, 1, 1);


select * from tbl_matricula

select * from tbl_matricula_curso

select * from tbl_alumno