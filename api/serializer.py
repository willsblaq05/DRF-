from rest_framework import serializers
from .models import user
class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers. IntegerField()
    city = serializers.CharField(max_length = 150)
 
    def create(self, validate_data):
        return user.objects.create(**validate_data)

    def update(self, instance,validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)
        instance.city = validated_data.get("city", instance.city)
        instance.save()
        return instance
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ["name", "age", "city"]