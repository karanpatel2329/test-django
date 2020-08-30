from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user=CustomUser(name="karan",
                        emails="pkaran4252@gmail.com",
                        is_staff=True,
                        is_superuser=True,
                        phone="8523697412",
                        gender="Male"
                        )
        user.set_password("1234")
        user.save()
    dependenices=[

    ]
    operations=[
        migrations.RunPython(seed_data),
    ]