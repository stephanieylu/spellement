from django.db import models

class Element(models.Model):
    """Model representing an element."""
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=2)
    number = models.CharField(max_length=3, blank=True)
    mass = models.CharField(max_length=20, blank=True)

    ELEMENT_STATE = (
        ('s', 'Solid'),
        ('g', 'Gas'),
        ('l', 'Liquid'),
        ('u', 'Unknown'),
        ('f', 'Fictional')
    )
    
    state = models.CharField(
        max_length=1,
        choices = ELEMENT_STATE,
    )

    class Meta:
        ordering = ['number']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name} ({self.symbol})'
