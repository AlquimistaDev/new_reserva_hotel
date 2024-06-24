SELECT 
    a.numero_habitacion, 
    a.capacidad, 
    b.descripcion AS orientacion, 
    c.tipo_cama, 
    d.estado_hab
FROM 
    hotel_mpc.tbl_habitacion a
    JOIN hotel_mpc.TBL_ORIENTACION b ON a.id_orientacion = b.id_orientacion
    JOIN hotel_mpc.TBL_TIPO_CAMA c ON a.id_tipo_cama = c.id_tipo_cama
    JOIN hotel_mpc.TBL_ESTADO_HABITACION d ON a.id_estado_hab = d.id_estado_hab
WHERE 
    a.ID_estado_hab = 2;