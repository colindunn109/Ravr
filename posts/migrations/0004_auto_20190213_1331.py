# Generated by Django 2.0.7 on 2019-02-13 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]
