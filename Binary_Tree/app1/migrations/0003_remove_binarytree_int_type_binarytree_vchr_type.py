# Generated by Django 5.0.1 on 2024-02-02 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_binarytree_bln_child_binarytree_int_parent_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='binarytree',
            name='int_type',
        ),
        migrations.AddField(
            model_name='binarytree',
            name='vchr_type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
