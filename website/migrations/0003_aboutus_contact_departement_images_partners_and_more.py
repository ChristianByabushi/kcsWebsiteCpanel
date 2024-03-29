# Generated by Django 4.1.7 on 2023-03-31 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_backgrounddescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptionKcs', models.TextField()),
                ('paragraphahDescription', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/about/')),
            ],
            options={
                'verbose_name_plural': 'About-us',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('updateAt', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
                'ordering': ('-createAt',),
            },
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=50)),
                ('description', models.TextField(default='')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateField(auto_now=True)),
                ('img', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'images',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('foundation', models.BooleanField(default='')),
                ('description', models.TextField()),
                ('image_ou_logo', models.ImageField(null=True, upload_to='images/partners/')),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Partenaires',
            },
        ),
        migrations.CreateModel(
            name='ProjectOnWebsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projecttitle', models.TextField(default='')),
                ('description', models.TextField()),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='images/projects/')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classIcon', models.CharField(max_length=30)),
                ('titleService', models.CharField(max_length=100)),
                ('paragrapheDescription', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Socialmediaslinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(null=True)),
                ('linkedin', models.URLField()),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('twitter', models.URLField()),
                ('messageforsocialmedia', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'SocialMedia',
                'ordering': ('-createAt',),
            },
        ),
        migrations.CreateModel(
            name='teamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=60)),
                ('designation', models.CharField(max_length=60)),
                ('facebook', models.URLField(null=True)),
                ('linkedin', models.URLField(null=True)),
                ('twitter', models.URLField(null=True)),
                ('image', models.ImageField(upload_to='images/teamMembers/')),
            ],
            options={
                'verbose_name_plural': 'teamMembers',
            },
        ),
        migrations.AlterField(
            model_name='backgrounddescription',
            name='image',
            field=models.ImageField(upload_to='images/projects/'),
        ),
        migrations.CreateModel(
            name='usersDepartement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departementConcernded', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Departement', to='website.departement')),
                ('userConcerned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userConcerned', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'utilisateursDepartements',
            },
        ),
        migrations.CreateModel(
            name='projectsImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/projects/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.projectonwebsite')),
            ],
            options={
                'verbose_name_plural': 'IProjectsEtImages',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
                ('message', models.TextField(null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/news')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.departement')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Nouvelles',
                'ordering': ('-created_at',),
            },
        ),
    ]
