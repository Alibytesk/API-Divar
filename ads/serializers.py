from rest_framework import serializers
from .models import Ad

class AdSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')
    class Meta:
        model = Ad
        fields = "__all__"
        read_only_fields = ('id', 'is_public', 'date_added')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['publisher'] = request.user
        return Ad.objects.create(**validated_data)