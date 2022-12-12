from rest_framework import serializers
from application_form.models import Application_form,Alredy_registered_user

class Application_formSerializer(serializers.ModelSerializer):
  class Meta:
    model=Application_form
    fields = '__all__'


class Alredy_registered_userSerializer(serializers.ModelSerializer):
  class Meta:
    model=Alredy_registered_user
    fields = '__all__'