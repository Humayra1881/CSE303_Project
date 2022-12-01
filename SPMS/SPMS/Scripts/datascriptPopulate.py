import pandas as pd
import os
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SPMV2.settings")
import django
django.setup()
from spmapp.models import *
course = Course_T(courseID="", courseName="", numOfCredits="", program_id="",
                  courseType="")
course.save()
plolist = list(PLO_T.objects.filter(program=2))
colist = []
colist.append(CO_T(coNum="CO1", course=course, plo=plolist[0]))
colist.append(CO_T(coNum="CO2", course=course, plo=plolist[1]))
colist.append(CO_T(coNum="CO3", course=course, plo=plolist[2]))
colist.append(CO_T(coNum="CO4", course=course, plo=plolist[3]))
colist[0].save()
colist[1].save()
colist[2].save()
colist[3].save()
faculties = []
faculties.append(Faculty_T.objects.get(pk=4201))
faculties.append(Faculty_T.objects.get(pk=4202))
faculties.append(Faculty_T.objects.get(pk=4203))

dept = Department_T.objects.get(pk="ACN")
program = Program_T.objects.get(pk=2)









dataframes=[]
def updatedatabase(d, sem, y):
    df1 = pd.read_excel("Tally Sheet For Autumn 2021 (9)", sheet_name="Marks") #pandas.read_excel(io, sheet_name=0, *, header=0, names=None, index_col=None, usecols=None, squeeze=None, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, parse_dates=False, date_parser=None, thousands=None, decimal='.', comment=None, skipfooter=0, convert_float=None, mangle_dupe_cols=True, storage_options=None)
    df2 = pd.read_excel("Tally Sheet For Spring 2021 (1)", sheet_name="Marks")
    df3 = pd.read_excel("Tally Sheet For Summer 2021 (11)", sheet_name="Marks")
    df4 = pd.read_excel("CSE303 OBE Mark Sheet Sample", sheet_name="Marks")

    
    dataframes=[df1,df2,df3,df4]
    df=pd.contact(dataframes)
    data = df.values.tolist()



    comid = data[0][5:11]
    cofin = data[0][13:17]
    colab = data[0][19]

    midmarks = data[2][5:11]
    finmarks = data[2][13:17]
    labmark = data[2][19]

    data = data[3:][:]

    for i in data:
        i[1] = int(i[1]) + d
        i[3] = int(int(i[3]))

    currentstudents = list(Student_T.objects.all())
    newstudents = []

    sections = []

    for i in data:
        if i[1] not in currentstudents:
            newstudents.append(i[1])

        if i[3] not in sections:
            sections.append(i[3])

    sections.sort()
    # Students

    for i in newstudents:
        student = Student_T(studentID=i, department=dept, program=program)
        student.save()

    # Sections

    sectionlist = []

    for i in sections:
        faculty = faculties[i - 1]
        section = Section_T(sectionNum=i, course=course, faculty=faculty, semester=sem, year=y)
        section.save()
        sectionlist.append(section)

    # Registration
    reglist = []

    for i in data:
        st = Student_T.objects.get(pk=i[1])
        reg = Registration_T(student=st, section=sectionlist[i[3] - 1], semester=sem, year=y)
        reg.save()
        reglist.append(reg)

    # Assessment
    assessmentlist = []
    for i in range(1, len(sectionlist) + 1):
        for j in range(1, len(comid) + 1):

            coid = []

            for k in colist:
                if k.coNum == comid[j - 1]:
                    coid = k
                    break

            assessment = Assessment_T(assessmentName="Mid", questionNum=j, totalMarks=midmarks[j - 1], co=coid,
                                      section=sectionlist[i - 1], weight=30)
            assessment.save()
            assessmentlist.append(assessment)

        for j in range(1, len(cofin) + 1):

            coid = []

            for k in colist:
                if k.coNum == cofin[j - 1]:
                    coid = k
                    break
            assessment = Assessment_T(assessmentName="Final", questionNum=j, totalMarks=finmarks[j - 1], co=coid,
                                      section=sectionlist[i - 1], weight=40)

            assessment.save()
            assessmentlist.append(assessment)

        coid = []

        for k in colist:
            if k.coNum == colab:
                coid = k
                break

        assessment = Assessment_T(assessmentName="Lab", questionNum=1, totalMarks=labmark, co=coid,
                                  section=sectionlist[i - 1], weight=30)
        assessment.save()
        assessmentlist.append(assessment)

    # Evaluation

    evlist = []

    for i in range(0, len(data)):
        marks = data[i][5:11]
        marks.extend(data[i][13:17])
        marks.append(data[i][19])

        num = 11 * (data[i][3] - 1)

        for j in range(0, len(marks)):
            tmark = assessmentlist[num+j].totalMarks
            omark = random.randint(0,int(tmark))
            ev = Evaluation_T(obtainedMarks=omark, assessment=assessmentlist[num+j], registration=reglist[i])
            ev.save()
            evlist.append(ev)


updatedatabase(0, "Spring", 2020)
updatedatabase(100, "Summer", 2020)
updatedatabase(200, "Autumn", 2020)
