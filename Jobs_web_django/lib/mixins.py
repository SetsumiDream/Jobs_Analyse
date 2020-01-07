class ModelMixin:
    def to_dict(self):
        attr_dict = {}
        for field in self._meta.get_fields():
            attr_dict[field.attname] = getattr(self, field.attname, None)
        return attr_dict