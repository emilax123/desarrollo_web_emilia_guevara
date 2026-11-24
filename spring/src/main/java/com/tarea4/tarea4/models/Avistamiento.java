package com.tarea4.tarea4.models;

import java.time.LocalDateTime;
import org.springframework.web.multipart.MultipartFile;

import jakarta.persistence.*;

@Entity
@Table
public class Avistamiento{
    @Id
    
    @GeneratedValue(
        strategy = GenerationType.IDENTITY,
    )
    private Long id;

    @NotNull
    private String title;

    public Avistamiento(){
    }

    public Avistamiento(String

    )

    public Long getId(){
        return id;
    }

    public String v
}
