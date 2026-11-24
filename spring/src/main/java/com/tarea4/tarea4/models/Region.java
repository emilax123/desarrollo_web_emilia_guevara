package com.tarea4.tarea4.models;

import jakarta.persistence.*;

@Entity
@Table
public class Region{
    @Id;
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "nombre", length = 30)

    public Long getId(){
        return id;
    }

    public String getNombre(){
        return nombre;
    }
}