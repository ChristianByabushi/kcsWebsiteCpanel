# Generated by Django 4.1.7 on 2023-03-31 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='backgrounddescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subdescription', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/projectimage/')),
                ('createAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'backgrounddescription',
                'ordering': ('-createAt',),
            },
        ),
    ]
