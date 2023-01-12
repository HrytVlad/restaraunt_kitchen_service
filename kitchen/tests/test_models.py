from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import Cook, DishType, Dish


class ModuleTests(TestCase):

    def test_dish_type_str(self):

        dish_type = DishType.objects.create(
            name="Test name",
        )

        self.assertEqual(
            str(dish_type),
            f"{dish_type.name}")

    def test_cook_str(self):
        cooke = get_user_model().objects.create_user(
            username="test",
            password="test21234",
            first_name="test test",
            last_name="test test"
        )

        self.assertEqual(str(cooke),
                         f"{cooke.username}"
                         f" {cooke.first_name} {cooke.last_name}")

    def test_dish_str(self):
        name = Dish(
            name="test",
            price=13,
            dish_type=DishType("test")
        )

        self.assertEqual(str(name), f"{name.name} (price: {name.price}, dish type: {name.dish_type.name})")
