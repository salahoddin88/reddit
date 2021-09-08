from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from category.models import Category
from question_answer.models import Question, Answer
from user_profile.models import UserProfile
from comment.models import Comment
from django.contrib import messages
from datetime import datetime



""" Home page view function """
def homePage(request):
    navigation_categories = Category.objects.filter(status=True).order_by('-id')[:5]
    categories = Category.objects.filter(status=True)
    questions = Question.objects.filter(status=True).order_by('-id')[:5]
    return render(request, 'home.html', {
                                        'navigation_categories':navigation_categories,
                                        'categories' : categories,
                                        'questions':questions})
                                        

def categoryQuestion(request, category_id):
    navigation_categories = Category.objects.filter(status=True).order_by('-id')[:5]
    categories = Category.objects.filter(status=True)
    questions = Question.objects.filter(status=True, category_id=category_id)
    return render(request, 'category-question.html', {
        'navigation_categories': navigation_categories,
        'categories' : categories,
        'questions' : questions
    })
    
def QuestionDetails(request, question_id):
    navigation_categories = Category.objects.filter(status=True).order_by('-id')[:5]
    answersObjects = Answer.objects.filter(question_id=question_id)
    answers = {}
    for key, answer in enumerate(answersObjects):
        try:
            userProfileObject = UserProfile.objects.get(user=answer.user)
        except UserProfile.DoesNotExist:
            userProfileObject = {}
        
        answers[key] = {
            'answer' : answer,
            'user_profile' : userProfileObject
        }
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        question = {}
    return render(request, 'question-details.html', {
        'navigation_categories': navigation_categories,
        'question':question,
        'answers' : list(answers.values())
    })


def SaveComment(request):
    questionId = request.POST.get('question_id')
    answerId = request.POST.get('answer_id')
    comment = request.POST.get('comment')
    image = request.FILES.get('image')
    if comment:
        Comment.objects.create(
            answer_id=answerId,
            comments=comment,
            added_date=datetime.now(),
            user=request.user,
            image = image
        )
        messages.success(request, 'Comment added successfully')
    else:
        messages.error(request, 'Comment can not be empty')
    
    return redirect('QuestionDetails', question_id=questionId)