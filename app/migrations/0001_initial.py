# Generated by Django 4.1.7 on 2023-04-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dept",
            fields=[
                ("departno", models.IntegerField(primary_key=True, serialize=False)),
                ("dname", models.CharField(max_length=20)),
                ("loc", models.CharField(max_length=20)),
            ],
        ),
    ]
