# Generated by Django 2.2.13 on 2020-06-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_blogpost_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='a'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
