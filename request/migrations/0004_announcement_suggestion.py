# Generated by Django 4.1.3 on 2023-02-03 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_church'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Contenu ')),
                ('content', models.CharField(max_length=200, verbose_name='Contenu ')),
                ('illustration', models.ImageField(blank=True, default=None, null=True, upload_to='images/illustrations/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='Contenu ')),
                ('skills', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('church', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='church', to='request.church')),
            ],
        ),
    ]
