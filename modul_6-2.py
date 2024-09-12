

class Vehicle:
    def __init__(self, __model, __engine_power, __color, owner):
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.owner = owner
        __COLOR_VARIANTS=['blue', 'red', 'green', 'black', 'white']
        self.__COLOR_VARIANTS = __COLOR_VARIANTS

    def get_model(self, __model):
        pass

    def get_horsepower(self, __engine_power):
        pass

    def get_color(self, __color):
        pass

    def get_owner(self, owner):
        pass

    def set_color(self, new_color):
        c=[]
        for i in range(len(self.__COLOR_VARIANTS)):
            c.append(self.__COLOR_VARIANTS[i].upper())

        if new_color.upper() in c:
            self.__color = new_color
        else:
            print (f"Нельзя сменить цвет на: {new_color.upper ()}"
                   f'\n{'-' * 40}')
        return self.__color

    def print_info(self):
        print (f"Модель: {self.__model}"
               f"\nМощность двигателя: {self.__engine_power}"
               f"\nЦвет машины: {self.__color}"
               f"\nВладелец: {self.owner} "
               f'\n{'-' * 40}')


class Sedan (Vehicle):
    def __init__(self, __model, __engine_power, __color, owner, __PASSENGERS_LIMIT):
        super ().__init__ (__model, __engine_power, __color, owner)
        self.__PASSENGERS_LIMIT = __PASSENGERS_LIMIT
        print (f'Седан {__PASSENGERS_LIMIT} мест')


car = Vehicle ('Жигуль', '50000', 'голубой', 'Лили')
car.print_info ()
car.owner = 'Фируз'
car.print_info ()
car.set_color ("red")
car.print_info ()
car.set_color ("re")
car.print_info ()
car.set_color ("rekk")
car.print_info ()
car.set_color ("white")
car.print_info ()
sedan = Sedan ('Жигуль', '50000', 'голубой', 'Лили', 5)
car.print_info ()
sedan.owner = 'Тошка картошка'
sedan.print_info ()
sedan.set_color ("MMM")
sedan.set_color ('BLue')
sedan.print_info ()