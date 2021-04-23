class Libro:
    __ISBN = 19022008
    __Titulo = "the life of a programmer"
    __Autor_principal = "mariano"
    __Numero_De_paginas = 45
    __Editorial = "soto"
    __Tipo_pasta = "cuero"
    __Calificacion = 3



    def default(self, a):
        if a:
            Libro.__ISBN = 19022008
            Libro.__Titulo = "the life of a programmer"
            Libro.__Autor_principal = "mariano"
            Libro.__Numero_De_paginas = 45
            Libro. __Editorial = "soto"
            Libro.__Tipo_pasta = "cuero"
            Libro. __Calificacion = 3

    def setVariables(self,isbn,titulo,autor,nump,editorial,tipoPasta,Calificacion):
          self.__ISBN=isbn
          self.__Titulo=titulo
          self.__Autor_principal=autor
          self.__Numero_De_paginas=nump
          self.__Editorial=editorial
          self.__Tipo_pasta=tipoPasta
          self.__Calificacion=Calificacion

    def imprimir_info(self):
        print(f"{Libro.__Titulo} con ISBN {Libro.__ISBN} creado por el autor {Libro.__Autor_principal} tiene calificacion de {Libro.__Calificacion} estrellas")

    def sumarpaginas():
        return Libro.__Numero_De_paginas+Libro.__Numero_De_paginas