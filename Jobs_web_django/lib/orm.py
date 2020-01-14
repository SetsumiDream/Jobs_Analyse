import random

from django.core.cache import cache
from django.db import models

from common import keys


def get(cls, *args, **kwargs):
    pk = kwargs.get('id') or kwargs.get('pk')

    if pk is not None:
        key = keys.OBJECT_KEY % (cls.__name__, pk)
        model_obj = cache.get(key)
        if isinstance(model_obj, cls):
            return model_obj

    model_obj = cls.objects.get(*args, **kwargs)
    key = keys.OBJECT_KEY % (cls.__name__, model_obj.pk)
    cache.set(key, model_obj, 86400 * 14 * (random.random() + 1))

    return model_obj


def get_or_create(cls, defaults=None, **kwargs):
    pk = kwargs.get('id') or kwargs.get('pk')

    if pk is not None:
        key = keys.OBJECT_KEY % (cls.__name__, pk)
        model_obj = cache.get(key)

        if isinstance(model_obj, cls):
            return model_obj

    model_obj, _ = cls.objects.get_or_create(**kwargs)

    key = keys.OBJECT_KEY % (cls.__name__, model_obj.pk)
    cache.set(key, object, 86400 * 14 * random.random() + 1)
    return model_obj


def save_with_cache(model_save_func):
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        model_save_func(force_insert=False, force_update=False, using=None, update_fields=None)
        key = keys.OBJECT_KEY % (self.__class__.__name__, self.pk)
        cache.set(key, self, 86400 * 14 * random.random() + 1)
    return save


def to_dict1(self, *ignore_fields):
    attr_dict = {}
    for field in self._meta.get_fields():
        name = field.attname
        if name not in ignore_fields:
            attr_dict[field.attname] = getattr(self, field.attname, None)
    return attr_dict


def patch_model():

    models.Model.get = classmethod(get)
    models.Model.get_or_create = classmethod(get_or_create)

    models.Model.save = save_with_cache(models.Model.save)

    models.Model.to_dict1 = to_dict1
