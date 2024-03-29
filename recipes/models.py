from django.db import models

# Create your model


class Recipe(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Ingredients(models.Model):
    ingredients = models.TextField(null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


    def __str__(self):
        return self.ingredients


class Step(models.Model):
    steps = models.TextField(null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.steps
        




