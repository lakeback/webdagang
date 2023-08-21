from django.shortcuts import render,HttpResponse
from app01.wordtest.word_tools import chaogangword
# Create your views here.

def index(request):
    #return HttpResponse('欢迎使用')
    #print(request.method)
    grade_choice =  {
        '1':'七上',
        "2":'七下',
        "3":'八上',
        "4":'八下',
        "5": '九',
    }
    grade_list=[
        {'grade': 1, 'grade_name': '七上'},
        {'grade': 2, 'grade_name': '七下'},
        {'grade': 3, 'grade_name': '八上'},
        {'grade': 4, 'grade_name': '八下'},
        {'grade': 5, 'grade_name': '九'},
    ]
    if request.method == "GET":
        return render(request,'index.html',{'grade_list':grade_list})
    else:
        grade = request.POST.get('grade')
        unit = request.POST.get('unit')
        text = request.POST.get('corpus')
        chaogang = chaogangword(text, grade, unit)
        #print(request.POST)
        #print(chaogang)

        grade_name = grade_choice[grade]
        # print(grade)
        # print(grade_name)
        #grade_choice = grade_list
        print(grade)
        print(grade_name)
        return render(request,'index.html',{'chaogang':chaogang,'grade_input':grade,'grade_name':grade_name,'grade_list':grade_list,'unit':unit,'corpus':text})



