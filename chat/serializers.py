from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User        # From the Admin database





# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name','last_name', 'is_staff', 'date_joined']

