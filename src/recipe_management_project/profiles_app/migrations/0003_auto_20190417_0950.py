# Generated by Django 2.1.7 on 2019-04-17 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_app', '0002_recipemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('following_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='following_by', to=settings.AUTH_USER_MODEL)),
                ('following_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='following_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='followingmodel',
            unique_together={('following_to', 'following_by')},
        ),
    ]