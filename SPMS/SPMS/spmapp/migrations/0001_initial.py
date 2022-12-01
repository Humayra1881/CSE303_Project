# Generated by Django 3.2 on 2021-05-22 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment_T',
            fields=[
                ('assessmentID', models.AutoField(primary_key=True, serialize=False)),
                ('assessmentName', models.CharField(max_length=30)),
                ('questionNum', models.IntegerField()),
                ('totalMarks', models.FloatField()),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Course_T',
            fields=[
                ('courseID', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=50, null=True)),
                ('numOfCredits', models.DecimalField(decimal_places=1, max_digits=2)),
                ('courseType', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Department_T',
            fields=[
                ('departmentID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('departmentName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_T',
            fields=[
                ('firstName', models.CharField(max_length=30, null=True)),
                ('lastName', models.CharField(max_length=30, null=True)),
                ('dateOfBirth', models.DateField(null=True)),
                ('gender', models.CharField(max_length=6, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=30, null=True)),
                ('employeeType', models.CharField(max_length=1, null=True)),
                ('facultyID', models.IntegerField(primary_key=True, serialize=False)),
                ('startDate', models.DateField(null=True)),
                ('rank', models.CharField(max_length=50, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.department_t')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Program_T',
            fields=[
                ('programID', models.AutoField(primary_key=True, serialize=False)),
                ('programName', models.CharField(max_length=70)),
                ('department', models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='spmapp.department_t')),
            ],
        ),
        migrations.CreateModel(
            name='School_T',
            fields=[
                ('schoolID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('schoolName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VC_T',
            fields=[
                ('firstName', models.CharField(max_length=30, null=True)),
                ('lastName', models.CharField(max_length=30, null=True)),
                ('dateOfBirth', models.DateField(null=True)),
                ('gender', models.CharField(max_length=6, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=30, null=True)),
                ('employeeType', models.CharField(max_length=1, null=True)),
                ('vcID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('startDate', models.CharField(default='N/A', max_length=15)),
                ('endDate', models.CharField(default='N/A', max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student_T',
            fields=[
                ('studentID', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50, null=True)),
                ('lastName', models.CharField(max_length=50, null=True)),
                ('dateOfBirth', models.DateField(null=True)),
                ('gender', models.CharField(max_length=6, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('enrollmentDate', models.DateField(null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.department_t')),
                ('program', models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='spmapp.program_t')),
            ],
        ),
        migrations.CreateModel(
            name='Section_T',
            fields=[
                ('sectionID', models.AutoField(primary_key=True, serialize=False)),
                ('sectionNum', models.IntegerField()),
                ('semester', models.CharField(max_length=15)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.course_t')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.faculty_t')),
            ],
        ),
        migrations.CreateModel(
            name='Registration_T',
            fields=[
                ('registrationID', models.AutoField(primary_key=True, serialize=False)),
                ('semester', models.CharField(max_length=15)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.section_t')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.student_t')),
            ],
        ),
        migrations.CreateModel(
            name='PrereqCourse_T',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Course', to='spmapp.course_t')),
                ('preReqCourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PreRequisite', to='spmapp.course_t')),
            ],
        ),
        migrations.CreateModel(
            name='PLO_T',
            fields=[
                ('ploID', models.AutoField(primary_key=True, serialize=False)),
                ('ploNum', models.CharField(max_length=5)),
                ('details', models.CharField(max_length=50)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.program_t')),
            ],
        ),
        migrations.CreateModel(
            name='Head_T',
            fields=[
                ('firstName', models.CharField(max_length=30, null=True)),
                ('lastName', models.CharField(max_length=30, null=True)),
                ('dateOfBirth', models.DateField(null=True)),
                ('gender', models.CharField(max_length=6, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=30, null=True)),
                ('employeeType', models.CharField(max_length=1, null=True)),
                ('headID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('startDate', models.CharField(default='N/A', max_length=15)),
                ('endDate', models.CharField(default='N/A', max_length=15)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.department_t')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Evaluation_T',
            fields=[
                ('evaluationID', models.AutoField(primary_key=True, serialize=False)),
                ('obtainedMarks', models.FloatField()),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.assessment_t')),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.registration_t')),
            ],
        ),
        migrations.AddField(
            model_name='department_t',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.school_t'),
        ),
        migrations.CreateModel(
            name='Dean_T',
            fields=[
                ('firstName', models.CharField(max_length=30, null=True)),
                ('lastName', models.CharField(max_length=30, null=True)),
                ('dateOfBirth', models.DateField(null=True)),
                ('gender', models.CharField(max_length=6, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=30, null=True)),
                ('employeeType', models.CharField(max_length=1, null=True)),
                ('deanID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('startDate', models.CharField(default='N/A', max_length=15)),
                ('endDate', models.CharField(default='N/A', max_length=15)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.school_t')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='course_t',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.program_t'),
        ),
        migrations.CreateModel(
            name='CO_T',
            fields=[
                ('coID', models.AutoField(primary_key=True, serialize=False)),
                ('coNum', models.CharField(max_length=4)),
                ('thresold', models.FloatField(default=40)),
                ('course', models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='spmapp.course_t')),
                ('plo', models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='spmapp.plo_t')),
            ],
        ),
        migrations.AddField(
            model_name='assessment_t',
            name='co',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.co_t'),
        ),
        migrations.AddField(
            model_name='assessment_t',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.section_t'),
        ),
    ]
