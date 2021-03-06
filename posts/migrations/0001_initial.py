# Generated by Django 2.0.7 on 2019-02-13 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_auto_20190213_0506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField(default='')),
                ('author', models.ForeignKey(on_delete='CASCADE', to='accounts.User')),
            ],
        ),
    ]
