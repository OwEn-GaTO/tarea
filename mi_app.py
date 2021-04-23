import mi_modulo as mm

libro2=mm.Libro
libro1 = mm.Libro
libro1.setVariables(libro1,13041993,"my life","jose gonsalez", 45,"marvel","cuero",5)
libro1.default(libro1,False)
print("libro 1: ")
libro1.imprimir_info(libro1)
print("libro 2: ")
libro2.default(libro2,True)
libro2.imprimir_info(libro2)
suma=mm.Libro.sumarpaginas()
print(f"la suma de las pagunas es: {suma}")
