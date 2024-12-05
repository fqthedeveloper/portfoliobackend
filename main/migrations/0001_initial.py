# Generated by Django 5.1.3 on 2024-12-03 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='badges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('badges', models.ImageField(upload_to='badges/')),
                ('alt_text', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Banners',
            },
        ),
        migrations.CreateModel(
            name='certifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('certifications', models.ImageField(upload_to='certifications/')),
                ('alt_text', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'certification',
            },
        ),
    ]
