from django.shortcuts import render

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
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def user_dash(request):
    return render(request, 'user_dash.html')


from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question
from .forms import QuizForm


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

            return render(request, 'quiz_result.html', {
                'quiz': quiz,
                'score': score,
                'total': len(questions),
            })
    else:
        form = QuizForm(questions=questions)

    return render(request, 'quiz_detail.html', {'quiz': quiz, 'form': form})



