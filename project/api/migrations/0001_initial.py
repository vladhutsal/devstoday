# Generated by Django 3.1.6 on 2021-03-17 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(blank=True, max_length=100)),
                ('author_name', models.CharField(max_length=50)),
                ('upvotes', models.IntegerField(default=0)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
