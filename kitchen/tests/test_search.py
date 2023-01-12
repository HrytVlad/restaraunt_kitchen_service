from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from kitchen.models import DishType


class SearchTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="new_user",
            years_of_experience="3"
        )
        self.client.force_login(self.user)

    def test_search_dish_type_by_name(self):
        response = self.client.get(
            reverse("kitchen:dish-type-list") + "?name=Desserts"
        )
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(DishType.objects.filter(name__icontains="Desserts")),
        )
