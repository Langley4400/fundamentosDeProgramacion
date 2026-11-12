#include <stdio.h>

struct Alumno {
    char nombre[30];
    float promedio;
    void (*saludar)(struct Alumno*);
};

void saludar(struct Alumno *a){
    printf("Hola, Soy %s\n", a->nombre);
}

int main(){
    struct Alumno a1 = {"Ana", 9.2, saludar};
    struct Alumno a2 = {"Luis", 5.5, saludar};
    a1.saludar(&a1);
    a2.saludar(&a2);
    return 0;
}