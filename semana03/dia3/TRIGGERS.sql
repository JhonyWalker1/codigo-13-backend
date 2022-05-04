--TRIGGER DISPARADORES

select alumno_nombre,
CONCAT(REPLACE(lower(alumno_nombre),' ',''), '@tecsup.edu.pe') as alum
from tbl_alumno

DELIMITER $$

CREATE TRIGGER tg_correo_alumno
BEFORE INSERT
ON tbl_alumno FOR EACH ROW
BEGIN
        set NEW.alumno_email = CONCAT(REPLACE(lower(NEW.alumno_nombre),' ',''), '@tecsup.edu.pe');
END
$$

DELIMITER ;

insert into tbl_alumno (alumno_nombre, alumno_celular,alumno_github) values 
('Juan Perez','999999999','https://www.github.com/juanperez');

select * from tbl_alumno