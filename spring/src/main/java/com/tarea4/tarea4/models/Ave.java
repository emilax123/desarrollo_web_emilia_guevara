package com.tarea4.tarea4.models;

import  jakarta.persistence.*;

@Entity
@Table 
public class Ave{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "nombre", length = 50)
    private String nombre;

    public Long getId(){
        return id;
    }

    public String getNombre(){
        return nombre;
    }
}