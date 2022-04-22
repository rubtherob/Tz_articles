import string

from django.contrib.auth.models import Group
from rest_framework import serializers
# Подключаем модель user
from .models import User



class UserRegistrSerializer(serializers.ModelSerializer):
    # Поле для повторения пароля
    password2 = serializers.CharField()

    # Настройка полей
    class Meta:
        # Поля модели которые будем использовать
        model = User
        # Назначаем поля которые будем использовать
        fields = ['email', 'password', 'password2']

    # Метод для сохранения нового пользователя
    def save(self, *args, **kwargs):
        # Создаём объект класса User
        user = User(
            email=self.validated_data['email'],  # Назначаем Email
        )
        # Проверяем на валидность пароль
        password = self.validated_data['password']
        # Проверяем на валидность повторный пароль
        password2 = self.validated_data['password2']
        # Проверяем совпадают ли пароли
        if password != password2:
            # Если нет, то выводим ошибку
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        has_no = set(password).isdisjoint
        if (len(password) < 8 or has_no(string.digits) or has_no(string.ascii_lowercase) or has_no(string.ascii_uppercase)):
            raise serializers.ValidationError({password: "Пароль должен состоять из 8 символов,с хотя бы 1 цифрой и маленькой и заглавной буквой"})
        # Сохраняем пароль
        user.set_password(password)
        # Сохраняем пользователя
        user.save()
        group = Group.objects.get(name="Subscriber")
        user.groups.add(group)
        # Возвращаем нового пользователя
        return user