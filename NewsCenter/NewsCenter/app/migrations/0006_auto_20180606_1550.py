# Generated by Django 2.0.4 on 2018-06-06 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180606_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='declaration',
            name='id_news',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.News'),
        ),
        migrations.AlterField(
            model_name='declaration',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.User'),
        ),
        migrations.AlterField(
            model_name='interested',
            name='id_news',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.News'),
        ),
        migrations.AlterField(
            model_name='interested',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.User'),
        ),
    ]