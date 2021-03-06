# Generated by Django 2.1.7 on 2019-03-07 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('Library', '0001_initial'), ('Library', '0002_auto_20190307_1310')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('biography', models.TextField(blank=True, null=True)),
                ('year_birth', models.IntegerField()),
                ('year_death', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('genre', models.CharField(choices=[('fiction', 'Fiction'), ('sci-fi', 'Science fiction'), ('classic', 'Classic literature'), ('romance', 'Romance')], max_length=20)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='book_covers/')),
                ('description', models.TextField(blank=True, null=True)),
                ('authors', models.ManyToManyField(related_name='books', to='Library.Author')),
            ],
        ),
    ]
