package com.tarea4.tarea4.models;

import jakarta.persistence.*;

@Entity
@Table
public class Voluntario{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long Id;

    @Column(name = "nombre", length = 60)
    
    @Column(name = "email", length = 30)

    @Column(name = "telefono", length = 15)

    @Column(name = "fecha_ingreso")
}