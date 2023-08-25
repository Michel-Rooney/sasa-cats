from django.db import models


class Cat(models.Model):
    BREED = (
        ('siamese', 'Siamese'),
        ('persian', 'Persian'),
        ('maine_coon', 'Maine Coon'),
        ('ragdoll', 'Ragdoll'),
        ('bengal', 'Bengal'),
        ('sphynx', 'Sphynx'),
        ('abyssinian', 'Abyssinian'),
        ('british_shorthair', 'British Shorthair'),
        ('scottish_fold', 'Scottish Fold'),
        ('siberian', 'Siberian'),
        ('norwegian_forest', 'Norwegian Forest'),
        ('devon_rex', 'Devon Rex'),
        ('burmese', 'Burmese'),
        ('oriental', 'Oriental'),
        ('cornish_rex', 'Cornish Rex'),
        ('egyptian_mau', 'Egyptian Mau'),
        ('himalayan', 'Himalayan'),
        ('exotic_shorthair', 'Exotic Shorthair'),
        ('turkish_van', 'Turkish Van'),
        ('manx', 'Manx'),
        ('singapura', 'Singapura'),
    )

    cover = models.ImageField(upload_to='cats/cover/')
    name = models.CharField(max_length=20)
    description = models.TextField()
    history = models.TextField()
    breed = models.CharField(max_length=20, choices=BREED)
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return self.name
