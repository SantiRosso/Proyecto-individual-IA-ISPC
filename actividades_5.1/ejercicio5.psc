INICIO
    LEER unidadesDeLeche
    LEER esJubilado
    montoParcial = unidadesDeLeche * 1000
    IMPRIMIR "unidadesDeLeche", unidadesDeLeche, "esJubilado", esJubilado
    
    SI unidadesDeLeche <= 12 Y NO esJubilado ENTONCES
        IMPRIMIR "unidadesDeLeche <= 12 y NO esJubilado"
        montoAPagar = montoParcial
    SINO SI unidadesDeLeche > 12 Y unidadesDeLeche <= 24 Y NO esJubilado ENTONCES
        IMPRIMIR "(unidadesDeLeche > 12 y unidadesDeLeche <= 24) y NO esJubilado"
        montoAPagar = montoParcial * 0.9
    SINO SI unidadesDeLeche > 24 Y NO esJubilado ENTONCES
        IMPRIMIR "unidadesDeLeche > 24 y NO esJubilado"
        montoAPagar = montoParcial * 0.85
    SINO SI unidadesDeLeche <= 12 Y esJubilado ENTONCES
        IMPRIMIR "unidadesDeLeche <= 12 y esJubilado"
        montoAPagar = montoParcial * 0.9
    SINO SI unidadesDeLeche > 12 Y unidadesDeLeche <= 24 Y esJubilado ENTONCES
        IMPRIMIR "(unidadesDeLeche > 12 y unidadesDeLeche <= 24) y esJubilado"
        montoAPagar = montoParcial * 0.8
    SINO SI unidadesDeLeche > 24 Y esJubilado ENTONCES
        IMPRIMIR "unidadesDeLeche > 24 y esJubilado"
        montoAPagar = montoParcial * 0.75
    FIN SI
    
    IMPRIMIR "El monto sin descuento es:", montoParcial
    IMPRIMIR "El monto total a pagar es:", montoAPagar
FIN
