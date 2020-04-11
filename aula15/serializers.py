from rest_framework import serializers


class MyCustomSerializer(serializers.Serializer):
    choices = (
        ('M', 'masculino'),
        ('F', 'feminino'),
    )

    name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    text = serializers.CharField(max_length=500)
    sexo = serializers.ChoiceField(choices)

    def create(self, *args, **kwags):
        return self.validated_data

    def validate_email(self, value):
        if 'guilherme' in value.lower():
            raise serializers.ValidationError("Guilherme ta proibido!")
        return value

    def validate_text(self, value):
        if 'babanao' in value.lower():
            raise serializers.ValidationError("Seu boca suja!")
        return value
