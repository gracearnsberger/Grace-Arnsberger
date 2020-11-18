from django.db import models

#pick which city you want to save
city_choices = [
    ('Bora Bora','Bora Bora'),
    ('Kauai','Kauai'),
    ('Miami','Miami'),
    ('Barcelona','Barcelona'),
    ('Valparaiso','Valparaiso'),
    ('Sydney','Sydney'),
    ('Cape Town','Cape Town'),
    ('Singapore','Singapore'),
    ('Dubai','Dubai'),
    ('Los Angeles','Los Angeles'),
]

city_rating = [
    ('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
]


#fields for form on savecities.html page

class savecities(models.Model):
    city_name = models.CharField(max_length=75, choices=city_choices)
    why_here = models.CharField(max_length=200, blank=False)
    date_saved = models.DateField()
    rate_city = models.CharField(max_length=75, choices=city_rating)

    objects = models.Manager()

#return city name

    def __str__(self):
        return self.city_name