# Generated by Django 4.0 on 2023-11-16 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessagePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='名無し', max_length=100, verbose_name='名前')),
                ('message', models.TextField(verbose_name='本文')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='コメント日')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.photopost', verbose_name='対象記事')),
            ],
        ),
    ]