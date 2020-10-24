# Generated by Django 3.1.2 on 2020-10-24 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boxer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(default='gear second', max_length=100)),
                ('weight', models.IntegerField(default=60)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(default='what is', max_length=150)),
                ('pub_date', models.DateTimeField(default='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(default='life or death', max_length=150)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
        ),
    ]