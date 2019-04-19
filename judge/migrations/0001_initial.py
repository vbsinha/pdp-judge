# Generated by Django 2.2 on 2019-04-19 10:31

import datetime
from django.db import migrations, models
import django.db.models.deletion
import functools
import judge.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unnamed Contest', max_length=50, unique=True)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('penalty', models.DecimalField(decimal_places=3, default=0.0, max_digits=4)),
                ('public', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('rank', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('code', models.CharField(default='UNSET', max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(default='Name not set', max_length=50)),
                ('statement', models.TextField(default='The problem statement is empty.', max_length=2500)),
                ('input_format', models.CharField(default='No input format specified.', max_length=1000)),
                ('output_format', models.CharField(default='No output format specified.', max_length=500)),
                ('difficulty', models.PositiveSmallIntegerField(default=0)),
                ('time_limit', models.DurationField(default=datetime.timedelta(seconds=10))),
                ('memory_limit', models.PositiveIntegerField(default=200000)),
                ('file_format', models.CharField(default='.py,.cpp,.c', max_length=100)),
                ('start_code', models.FileField(null=True, upload_to=judge.models.start_code_name)),
                ('max_score', models.PositiveSmallIntegerField(default=0)),
                ('compilation_script', models.FileField(default='./default/compilation_script.sh', upload_to=functools.partial(judge.models.compilation_test_upload_location, *(), **{'is_compilation': True}))),
                ('test_script', models.FileField(default='./default/test_script.sh', upload_to=functools.partial(judge.models.compilation_test_upload_location, *(), **{'is_compilation': False}))),
                ('setter_solution', models.FileField(null=True, upload_to=judge.models.setter_sol_name)),
                ('contest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='judge.Contest')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=32, primary_key=True, serialize=False)),
                ('file_type', models.CharField(choices=[('.none', 'NOT_SELECTED'), ('.py', 'PYTHON'), ('.c', 'C'), ('.cpp', 'CPP')], default='.none', max_length=5)),
                ('submission_file', models.FileField(upload_to=judge.models.submission_upload_location)),
                ('timestamp', models.DateTimeField()),
                ('judge_score', models.PositiveSmallIntegerField(default=0)),
                ('ta_score', models.PositiveSmallIntegerField(default=0)),
                ('final_score', models.FloatField(default=0.0)),
                ('linter_score', models.FloatField(default=0.0)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.Person')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('public', models.BooleanField()),
                ('id', models.CharField(default=uuid.uuid4, max_length=32, primary_key=True, serialize=False)),
                ('inputfile', models.FileField(default='./default/inputfile.txt', upload_to=functools.partial(judge.models.testcase_upload_location, *(), **{'is_input': True}))),
                ('outputfile', models.FileField(default='./default/outputfile.txt', upload_to=functools.partial(judge.models.testcase_upload_location, *(), **{'is_input': False}))),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionTestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verdict', models.CharField(choices=[('F', 'Fail'), ('P', 'Pass'), ('R', 'Running'), ('TE', 'TLE'), ('ME', 'OOM'), ('CE', 'COMPILATION_ERROR'), ('RE', 'RUNTIME_ERROR'), ('NA', 'NOT_AVAILABLE')], default='NA', max_length=2)),
                ('memory_taken', models.PositiveIntegerField()),
                ('time_taken', models.DurationField()),
                ('message', models.TextField(default='')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.Submission')),
                ('testcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.TestCase')),
            ],
        ),
        migrations.CreateModel(
            name='ContestPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.BooleanField()),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.Contest')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=32, primary_key=True, serialize=False)),
                ('comment', models.FileField(default='./default/comment.yml', upload_to=judge.models.comment_upload_location)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.Person')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.Problem')),
            ],
        ),
    ]
