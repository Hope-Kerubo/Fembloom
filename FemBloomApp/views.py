from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question
from .forms import QuizForm
from FemBloomApp.models import Signup


# Create your views here.
def index(request):
    return render(request, 'index.html')

def modules(request):
    return render(request, 'modules.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def feature(request):
    return render(request, 'feature.html')

def blog(request):
    return render(request, 'blog.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def hf(request):
    return render(request, 'hf.html')

def signup(request):
    if request.method == 'POST':
        mysignup=Signup(
            Fullname=request.POST['fullname'],
            EmailAddress=request.POST['email'],
            Password=request.POST['password'],
            ConfirmPassword=request.POST['confirm-password'],
        )
        mysignup.save()
        return redirect('/signin')
    else:
        return render(request, 'signup.html')


def signin(request):
    return render(request, 'signin.html')

def user_dash(request):
    return render(request, 'user_dash.html')

def donation(request):
    return render(request, 'donation.html')

def donatemoney(request):
    return render(request, 'donatemoney.html')

def donateproducts(request):
    return render(request, 'donateproducts.html')

def sponsorevents(request):
    return render(request, 'sponsorevents.html')

def selection(request):
    return render(request, 'selection.html')

def m1(request):
    return render(request, 'm1.html')

def m2(request):
    return render(request, 'm2.html')

def m3(request):
    return render(request, 'm3.html')

def m4(request):
    return render(request, 'm4.html')


def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.prefetch_related('options').all()

    if request.method == "POST":
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            score = 0
            for question in questions:
                selected_option_ids = form.cleaned_data[f'question_{question.id}']
                correct_option_ids = list(question.options.filter(is_correct=True).values_list('id', flat=True))

                # Check if selected options match the correct options
                if set(selected_option_ids) == set(correct_option_ids):
                    score += 1

            print(f"Quiz: {quiz.title}")
            print(f"Questions: {questions}")

            return render(request, 'quiz_result.html', {
                'quiz': quiz,
                'score': score,
                'total': len(questions),
            })
    else:
        form = QuizForm(questions=questions)

    return render(request, 'quiz_detail.html', {'quiz': quiz, 'form': form})





