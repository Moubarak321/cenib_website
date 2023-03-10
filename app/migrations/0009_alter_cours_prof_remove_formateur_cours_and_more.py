# Generated by Django 4.1.2 on 2022-12-29 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_formateur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='prof',
            field=models.CharField(choices=[('Lana', 'Lana'), ('Antonio', 'Antonio'), ('Brandon', 'Brandon'), ('Prince MENSAH', 'Prince MENSAH'), ('David ZOUNON', 'David ZOUNON'), ('Ansbert ABALLOT', 'Ansbert ABALLOT'), ('Moubarak BENON', 'Moubarak BENON')], default='', max_length=50),
        ),
        migrations.RemoveField(
            model_name='formateur',
            name='cours',
        ),
        migrations.AlterField(
            model_name='formateur',
            name='nom',
            field=models.CharField(choices=[('Lana', 'Lana'), ('Antonio', 'Antonio'), ('Brandon', 'Brandon'), ('Prince MENSAH', 'Prince MENSAH'), ('David ZOUNON', 'David ZOUNON'), ('Ansbert ABALLOT', 'Ansbert ABALLOT'), ('Moubarak BENON', 'Moubarak BENON')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='formateur',
            name='cours',
            field=models.ManyToManyField(to='app.cours'),
        ),
    ]
