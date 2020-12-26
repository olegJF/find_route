from django.test import TestCase

from cities.models import City
from trains.models import Train


class AllTestsCase(TestCase):

    def setUp(self) -> None:
        self.city_A = City.objects.create(name='A')
        self.city_B = City.objects.create(name='B')
        self.city_C = City.objects.create(name='C')
        self.city_D = City.objects.create(name='D')
        self.city_E = City.objects.create(name='E')
        lst = [
            Train(name='t1', from_city=self.city_A, to_city=self.city_B,
                  travel_time=9),
            Train(name='t2', from_city=self.city_B, to_city=self.city_D,
                  travel_time=8),
            Train(name='t3', from_city=self.city_A, to_city=self.city_C,
                  travel_time=7),
            Train(name='t4', from_city=self.city_C, to_city=self.city_B,
                  travel_time=6),
            Train(name='t5', from_city=self.city_B, to_city=self.city_E,
                  travel_time=3),
            Train(name='t6', from_city=self.city_B, to_city=self.city_A,
                  travel_time=11),
            Train(name='t7', from_city=self.city_A, to_city=self.city_C,
                  travel_time=10),
            Train(name='t8', from_city=self.city_E, to_city=self.city_D,
                  travel_time=5),
            Train(name='t9', from_city=self.city_D, to_city=self.city_E,
                  travel_time=4)
        ]
        Train.objects.bulk_create(lst)
