# Generated by Django 5.1.1 on 2024-09-29 19:12

import django.db.models.deletion
import phonenumber_field.modelfields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id_person",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("firstname", models.CharField(max_length=50)),
                ("lastname", models.CharField(max_length=50)),
                ("date_of_birth", models.DateField()),
                ("country", models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="user.person",
                    ),
                ),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("password", models.CharField(max_length=50)),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("account_token", models.CharField(max_length=250, unique=True)),
            ],
            bases=("user.person",),
        ),
    ]
