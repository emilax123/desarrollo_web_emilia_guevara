package com.tarea4.tarea4.models;

import jakarta.persistence.*;

@Entity
@Table
public class Comuna{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "nombre", length = 30)
    private String nombre;
}