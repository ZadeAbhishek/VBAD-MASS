# Generated by Django 4.0.2 on 2022-05-11 09:24

import VbadApp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('notice', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherName', models.CharField(max_length=100)),
                ('testno', models.IntegerField(default=0)),
                ('TestName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionNumber', models.CharField(max_length=50)),
                ('question', models.TextField()),
                ('TeacherAnswer', models.TextField()),
                ('answer', models.TextField()),
                ('tdifdSimilarity', models.CharField(max_length=50)),
                ('vectorSimilarity', models.CharField(max_length=50)),
                ('keywordSimilarity', models.CharField(max_length=50)),
                ('GrammerSimilarity', models.CharField(max_length=50)),
                ('finalResult', models.CharField(max_length=10)),
                ('total', models.CharField(max_length=50)),
                ('studentname', models.ForeignKey(default=VbadApp.models.No_name, null=True, on_delete=django.db.models.deletion.CASCADE, to='VbadApp.students', verbose_name='Studentname')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('Answer', models.TextField()),
                ('keyword', models.CharField(max_length=1000)),
                ('Teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VbadApp.teachers')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VbadApp.questions')),
                ('studentname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VbadApp.students')),
            ],
        ),
    ]