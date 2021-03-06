# Generated by Django 2.1 on 2018-08-14 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0018_auto_20180813_1330"),
    ]

    operations = [
        migrations.CreateModel(
            name="DistrictCollection",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID",),),
                (
                    "district",
                    models.CharField(
                        choices=[
                            ("tvm", "Thiruvananthapuram"),
                            ("ptm", "Pathanamthitta"),
                            ("alp", "Alappuzha"),
                            ("ktm", "Kottayam"),
                            ("idk", "Idukki"),
                            ("mpm", "Malappuram"),
                            ("koz", "Kozhikode"),
                            ("wnd", "Wayanad"),
                            ("knr", "Kannur"),
                            ("ksr", "Kasaragod"),
                            ("pkd", "Palakkad"),
                            ("tcr", "Thrissur"),
                            ("ekm", "Ernakulam"),
                            ("kol", "Kollam"),
                        ],
                        max_length=15,
                    ),
                ),
                ("collection", models.TextField(verbose_name="Details of collected items"),),
            ],
        ),
    ]
