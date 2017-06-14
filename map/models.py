# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from django.dispatch import receiver
from reversion import revisions as reversion
# from django.core.exceptions import ValidationError
# from django.db.models import signals
# from django.core.mail import send_mail
# from inventory.models import Assets, Users, Models, Categories
# from django.db.models import Prefetch
# from autoslug import AutoSlugField
# from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFill
# from imagekit.models import ImageSpecField
# import os

from uuid import uuid4
class Country(models.Model):
    gadmid = models.IntegerField()
    iso = models.CharField(max_length=5)
    name = models.CharField(max_length=54)
    iso2 = models.CharField(max_length=4)
    www = models.CharField(max_length=2)
    sqkm = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    class Meta:
        default_related_name = 'Country'
        get_latest_by = "created_at"
        ordering = ['updated_at']

    def __str__ (self):
        return self.name


# Auto-generated `LayerMapping` dictionary for Country model
country_mapping = {
    'gadmid': 'GADMID',
    'iso': 'ISO',
    'name': 'NAME',
    'iso2': 'ISO2',
    'www': 'WWW',
    'sqkm': 'SQKM',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

reversion.register(Country)

class Province(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=75)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    class Meta:
        default_related_name = 'provinces'
        get_latest_by = "created_at"
        ordering = ['updated_at']

    def __str__ (self):
        return self.name


# Auto-generated `LayerMapping` dictionary for Province model
province_mapping = {
    'id': 'ID',
    'name': 'NAME',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}
reversion.register(Province)






class County(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=75)
    type = models.CharField(max_length=50)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    # schools = models.ManyToManyField(School, through='CountySchool', related_name='CountySchools')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    # slug = AutoSlugField(populate_from='name',unique=True,max_length=255)
    class Meta:
        default_related_name = 'counties'
        get_latest_by = "created_at"
        ordering = ['updated_at']
    #
    # @models.permalink
    # def get_absolute_url(self):
    #     return ('county', (), {
    #         'slug': self.slug,
    #         'id': self.id,
    #     })

    def __str__ (self):
        return self.name

    # Auto-generated `LayerMapping` dictionary for County model
county_mapping = {
    # 'id': 'ID',
    'name': 'NAME',
    'type': 'TYPE',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}
reversion.register(County)




class Division(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=75)
    type = models.CharField(max_length=50)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_related_name = 'divisions'
        get_latest_by = "created_at"
        ordering = ['updated_at']

    def __str__ (self):
        return self.name


# Auto-generated `LayerMapping` dictionary for Division model
division_mapping = {
    'id': 'ID',
    'name': 'NAME',
    'type': 'TYPE',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}
reversion.register(Division)


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=25)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_related_name = 'locations'
        get_latest_by = "created_at"
        ordering = ['updated_at']

    def __str__ (self):
        return self.name


# Auto-generated `LayerMapping` dictionary for Location model
location_mapping = {
    'id': 'ID',
    'name': 'NAME',
    'type': 'TYPE',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

reversion.register(Location)


class Sublocation(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=75)
    type = models.CharField(max_length=25)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_related_name = 'sublocations'
        get_latest_by = "created_at"
        ordering = ['updated_at']

    def __str__ (self):
        return self.name


# Auto-generated `LayerMapping` dictionary for Sublocation model
sublocation_mapping = {
    'id': 'ID',
    'name': 'NAME',
    'type': 'TYPE',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}
reversion.register(Sublocation)


class Activity(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        default_related_name = 'activities'
        get_latest_by = "created_at"
        ordering = ['updated_at']

    def __str__ (self):
        return self.name

    def clean (self, *args, **kwargs):
        # add custom validation here
        if not self.name or not self.description:
            error_message = "Activity Name or Description cannot be blank"
            raise ValidationError({
                'name': error_message,
                'description': error_message,

            })
        super(Activity, self).clean(*args, **kwargs)

    def save (self, *args, **kwargs):
        self.full_clean()
        super(Activity, self).save(*args, **kwargs)


reversion.register(Activity)


class Component(models.Model):  # training, delivery, installation, repair, call center
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        default_related_name = 'components'
        get_latest_by = "created_at"
        ordering = ['updated_at']

    def __str__ (self):
        return self.name

    def clean (self, *args, **kwargs):
        # add custom validation here
        if not self.name or not self.description:
            error_message = "Component Name or Description cannot be blank"
            raise ValidationError({
                'name': error_message,
                'description': error_message,

            })
        super(Component, self).clean(*args, **kwargs)

    def save (self, *args, **kwargs):
        self.full_clean()
        super(Component, self).save(*args, **kwargs)


reversion.register(Component)
