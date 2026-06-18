from django.db import models


class Gear(models.Model):
    MATERIAL_CHOICES = [
        ('16MnCr5', '16MnCr5'),
        ('42CrMo4', '42CrMo4'),
        ('C45', 'C45'),
        ('GG25', 'Grauguss GG25'),
    ]

    module = models.FloatField(help_text='Modul m in mm')
    tooth_count = models.IntegerField(help_text='Zähnezahl z')
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES, default='16MnCr5')
    created_at = models.DateTimeField(auto_now_add=True)

    def pitch_diameter(self):
        # Teilkreisdurchmesser: d = m * z
        return self.module * self.tooth_count

    def addendum_diameter(self):
        # Kopfkreisdurchmesser: da = m * (z + 2)
        return self.module * (self.tooth_count + 2)

    def root_diameter(self):
        # Fußkreisdurchmesser: df = m * (z - 2.5)
        return self.module * (self.tooth_count - 2.5)

    def __str__(self):
        return f'm={self.module}, z={self.tooth_count} ({self.material})'
