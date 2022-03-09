# Generated by Django 4.0.2 on 2022-03-09 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='last name')),
                ('country', models.CharField(blank=True, max_length=30, null=True, verbose_name='country')),
                ('address1', models.CharField(blank=True, max_length=255, null=True, verbose_name='address')),
                ('address2', models.CharField(blank=True, max_length=255, null=True, verbose_name='address')),
                ('city', models.CharField(blank=True, max_length=30, null=True, verbose_name='city')),
                ('state', models.CharField(blank=True, max_length=30, null=True, verbose_name='state')),
                ('zip_code', models.CharField(blank=True, max_length=30, null=True, verbose_name='zip code')),
                ('phone', models.CharField(blank=True, max_length=13, null=True, verbose_name='phone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
    ]