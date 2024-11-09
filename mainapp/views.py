from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
import random
from .models import trivia

# Create your views here.
correct_ans=dict()
def callques(request):
    i=0
    ques_id=[]
    while i<10:
        x=random.randint(1,50)
        if(x not in ques_id):
            ques_id.append(x)
            i+=1
    response=dict()
    for i in ques_id:
        questions=dict()
        question_db=trivia.objects.filter(id=i).values()
        questions[question_db[0]["ques"]]=[question_db[0]["option1"],question_db[0]["option2"],question_db[0]["option3"],question_db[0]["option4"]]
        response[i]=questions
    context={'title':'home','response':response}
    return render(request,'index.html',context=context)

def get_ans(request):
    if(request.POST):
        answers=request.POST
        answers=dict(answers)
        del answers["csrfmiddlewaretoken"]
    miss=10-len(answers)
    correct=0
    wrong=0
    for i in answers:
        j=int(i)
        question_db=trivia.objects.filter(id=j).values()
        if(question_db[0]["correct_ans"]==answers[i][0]):
            correct+=1
        else:
            wrong+=1

    score=((correct * 4)-(wrong))

    context={'title':'Result','correct':correct,'wrong':wrong,'miss':miss,'score':score}
    return render(request,'result.html',context)

# def add_ques(request):
#     ques_response=requests.get("https://opentdb.com/api.php?amount=50&category=18&type=multiple").json()

#     options=[]
#     for i in ques_response["results"]:
#         print(i["question"])
#         print(i["correct_answer"])
#         options=i["incorrect_answers"]
#         options.insert(random.randint(0,3),i["correct_answer"])
#         print(options)
#         ques_trivia=trivia(ques=i["question"],option1=options[0],option2=options[1],option3=options[2],option4=options[3],correct_ans=i["correct_answer"])
#         ques_trivia.save()
        
#         print()
#     return HttpResponse("added")
