# Generated by Django 3.2.4 on 2021-06-26 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Alloy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metals_Composition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carbon', models.DecimalField(decimal_places=2, default=10, max_digits=5)),
                ('silicon', models.DecimalField(decimal_places=2, default=10, max_digits=5)),
                ('manganese', models.DecimalField(decimal_places=2, default=10, max_digits=5)),
                ('phosphorus', models.DecimalField(decimal_places=2, default=10, max_digits=5)),
                ('nickel', models.DecimalField(decimal_places=2, default=10, max_digits=5)),
                ('chromium', models.DecimalField(decimal_places=2, default=10, max_digits=5)),
                ('molybdenum', models.DecimalField(decimal_places=2, default=10, max_digits=5)),
                ('sulfur', models.DecimalField(decimal_places=2, default=10, max_digits=5)),
                ('cooling_rate', models.DecimalField(decimal_places=2, default=10, max_digits=5)),
                ('tempering_temperature', models.DecimalField(decimal_places=2, default=10, max_digits=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
