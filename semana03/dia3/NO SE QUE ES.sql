DELIMITER $$

CREATE PROCEDURE listar_alumnos()
BEGIN
    SELECT * FROM tbl_alumno;
END $$

DELIMITER ;


CALL listar_alumnos();

--PROCEDIMIENTO PARA MATRICULAR A UN ALUMNO
--REGISTRAR LA TABLA TBL_MATRICULA
--REGISTRAR LA TABLA TBL_MATRICULA_CURSO CON TODOS LOS CURSOS
DELIMITER$$
CREATE PROCEDURE sp_matricular_alumno(IN alu_id INT, IN niv_id INT, IN mod_id INT)
BEGIN
        --variables
        DECLARE mat_id INT;
        --REGISTRAR MATRICULA
        insert into tbl_matricula(alumno_id,nivel_id,modulo_id) 
        values(alu_id,niv_id,mod_id);

        select max(matricula_id) into mat_id from tbl_matricula;

        --registrar las matriculas_cursos

        bucle: LOOP

        END LOOP;

        FOR select curso_id as cur_id from tbl_curso DO
             insert into tbl_matricula_curso(matricula_id,curso_id)
             values(mat_id,cur_id)
        END FOR
END $$