from django.db import models

# Create your model


class Recipe(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200),
    description = models.TextField()


class Ingredient(models.Model):
    ingredients = models.TextField(null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)




