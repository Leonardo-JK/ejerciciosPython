class Timer:
    def __init__(self, hora=0, minutos=0, segundos=0):
        self.__hora = hora
        self.__minutos = minutos
        self.__segundos = segundos
        #
        # Escribir código aquí.
        #

    def __str__(self):
        h = str(self.__hora)
        m = str(self.__minutos)
        s = str(self.__segundos)
        if self.__hora < 10:
            h = "0" + str(self.__hora)
        if self.__minutos < 10:
            m = "0" + str(self.__minutos)
        if self.__segundos < 10:
            s = "0" + str(self.__segundos)
        
        return h + ":" + m + ":" + s
        #
        # Escribir código aquí.
        #

    def next_second(self):
        self.__segundos += 1
        if self.__segundos == 60:
            self.__segundos = 0
            self.__minutos += 1
        if self.__minutos == 60:
            self.__minutos = 0
            self.__hora +=1
        if self.__hora == 24:
            self.__hora = 0
        
        #
        # Escribir código aquí.
        #

    def prev_second(self):
        self.__segundos -= 1
        if self.__segundos == -1:
            self.__segundos = 59
            self.__minutos -= 1
        if self.__minutos == -1:
            self.__minutos = 59
            self.__hora -= 1
        if self.__hora == -1:
            self.__hora = 23
        
        #
        # Escribir código aquí.
        #


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)