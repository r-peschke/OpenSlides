# Generated by Django 2.2 on 2019-04-30 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("motions", "0024_state_restriction_3")]

    operations = [
        migrations.AddField(
            model_name="motion",
            name="category_weight",
            field=models.IntegerField(default=10000),
        )
    ]
