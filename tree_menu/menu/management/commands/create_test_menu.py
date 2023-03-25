"""
Команда создает тестовое меню для демонстрации.
"""

from django.core.management.base import BaseCommand
from menu.models import Item, Menu


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:

        colors = {'red': 'Красная', 'black': 'Черный', 'white': 'Белый'}

        main_menu = Menu(title='main_menu2', slug='main_menu')
        main_menu.save()
        # 1 уровень
        main_cars = Item(title='Машины', slug='cars', menu=main_menu)
        main_cars.save()

        cars_mercedes = Item(title='Мерседес', slug='mercedes', menu=main_menu,
                             parent=main_cars)
        cars_mercedes.save()

        cars_bmv = Item(title='БМВ', slug='bmv', menu=main_menu,
                        parent=main_cars)
        cars_bmv.save()

        # 3 уровень
        for i in range(2020, 2023):
            mercedes_year = Item(title=f'{i}', slug=f'{i}', menu=main_menu,
                                 parent=cars_mercedes)
            mercedes_year.save()
            # 4 уровень
            for color in colors.keys():
                car_color = Item(title=colors[color], slug=color, menu=main_menu,
                                 parent=mercedes_year)
                car_color.save()

        # 3 уровень
        for i in range(2020, 2022):
            bmv_year = Item(title=f'{i}', slug=f'{i}', menu=main_menu,
                            parent=cars_bmv)
            bmv_year.save()
            # 4 уровень
            for color in colors.keys():
                car_color = Item(title=colors[color], slug=color, menu=main_menu,
                                 parent=bmv_year)
                car_color.save()

        # 1 уровень
        main_moto = Item(title='Мотоциклы', slug='motos', menu=main_menu)
        main_moto.save()

        moto_yamaha = Item(title='Ямаха', slug='yamaha', menu=main_menu,
                           parent=main_moto)
        moto_yamaha.save()

        moto_honda = Item(title='Хонда', slug='honda', menu=main_menu,
                          parent=main_moto)
        moto_honda.save()

        # 3 уровень
        for i in range(2020, 2022):
            yamaha_year = Item(title=f'{i}', slug=f'{i}', menu=main_menu,
                               parent=moto_yamaha)
            yamaha_year.save()
            # 4 уровень
            for color in colors.keys():
                moto_color = Item(title=colors[color], slug=color, menu=main_menu,
                                  parent=yamaha_year)
                moto_color.save()

        # 3 уровень
        for i in range(2020, 2022):
            honda_year = Item(title=f'{i}', slug=f'{i}', menu=main_menu,
                              parent=moto_honda)
            honda_year.save()
            # 4 уровень
            for color in colors.keys():
                moto_color = Item(title=colors[color], slug=color, menu=main_menu,
                                  parent=honda_year)
                moto_color.save()

        # 1 уровень
        main_planes = Item(title='Самолеты', slug='planes', menu=main_menu)
        main_planes.save()

        # 2 уровень
        plane_boeing = Item(title='Боинг', slug='boeing', menu=main_menu,
                            parent=main_planes)
        plane_boeing.save()

        # 3 уровень
        for i in range(2020, 2022):
            plane_year = Item(title=f'{i}', slug=f'{i}', menu=main_menu,
                              parent=plane_boeing)
            plane_year.save()
            # 4 уровень
            for color in colors.keys():
                plane_color = Item(title=colors[color], slug=color,
                                   menu=main_menu, parent=plane_year)
                plane_color.save()

        # 2 уровень
        plane_airbus = Item(title='Аэробус', slug='airbus', menu=main_menu,
                            parent=main_planes)
        plane_airbus.save()
        # 3 уровень
        for i in range(2020, 2022):
            plane_year = Item(title=f'{i}', slug=f'{i}', menu=main_menu,
                              parent=plane_airbus)
            plane_year.save()
            # 4 уровень
            for color in colors.keys():
                plane_color = Item(title=colors[color], slug=color,
                                   menu=main_menu, parent=plane_year)
                plane_color.save()
