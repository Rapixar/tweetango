# Generated by Django 2.2 on 2020-12-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(null=True)),
                ('image', models.FileField(blank=True, upload_to='images/')),
            ],
        ),
    ]
