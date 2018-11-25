from rest_framework import serializers

# https://stackoverflow.com/questions/38245414/django-rest-framework-how-to-include-all-fields-and-a-related-field-in-mo
# generic hyperlinked serializer to support extra_fields


class CustomSerializer(serializers.HyperlinkedModelSerializer):

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CustomSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields
