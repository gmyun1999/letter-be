# Generated by Django 5.0.6 on 2024-10-04 05:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lucky_letter", "0002_lettergroup_letter_letter_group_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="LetterRelation",
            fields=[
                (
                    "id",
                    models.CharField(max_length=36, primary_key=True, serialize=False),
                ),
                ("target_letter_id", models.CharField(max_length=36)),
                ("reply_letter_id", models.CharField(max_length=36)),
            ],
            options={
                "db_table": "LetterRelation",
            },
        ),
        migrations.DeleteModel(
            name="LetterGroup",
        ),
        migrations.RemoveIndex(
            model_name="letter",
            name="Letter_letter__0a681e_idx",
        ),
        migrations.RemoveField(
            model_name="letter",
            name="letter_group_id",
        ),
    ]
