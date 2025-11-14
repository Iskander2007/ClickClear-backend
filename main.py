import os
import django

# подключаем Django-окружение
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from meta.models import District

districts = [
    "Алмалинский",
    "Бостандыкский",
    "Ауэзовский",
    "Медеуский",
    "Турксибский",
    "Жетысуский",
    "Наурызбайский",
]

created, skipped = 0, 0
for name in districts:
    obj, is_new = District.objects.get_or_create(name=name)
    if is_new:
        created += 1
    else:
        skipped += 1

print(f"✅ Добавлено {created}, пропущено (уже были): {skipped}")
