from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Event
from .forms import QuizForm
from FemBloomApp.models import Signup
from django.contrib import messages
from .forms import DonationApplicationForm, InstitutionForm, SponsorEventForm
from .models import Institution, SponsorEvent
from django.http import JsonResponse


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
                # Get selected options from the form
                selected_option_ids = form.cleaned_data.get(f'question_{question.id}', [])
                if not isinstance(selected_option_ids, list):
                    selected_option_ids = [selected_option_ids]  # Convert single value to list

                # Fetch correct options from the database
                correct_option_ids = list(question.options.filter(is_correct=True).values_list('id', flat=True))

                # Debugging: Log the data being compared
                print(f"Question: {question.text}")
                print(f"Selected Option IDs: {selected_option_ids}")
                print(f"Correct Option IDs: {correct_option_ids}")

                # Compare selected options with correct options
                if set(selected_option_ids) == set(correct_option_ids):
                    score += 1

            # Debugging: Ensure proper scoring
            print(f"Final Score: {score} / {questions.count()}")

            return render(request, 'quiz_result.html', {
                'quiz': quiz,
                'score': score,
                'total': questions.count(),
            })
        else:
            print("Form is not valid:", form.errors)  # Debugging: Print form errors

    else:
        form = QuizForm(questions=questions)

    return render(request, 'quiz_detail.html', {'quiz': quiz, 'form': form})


def apply_donation(request):
    if request.method == 'POST':
        donation_form = DonationApplicationForm(request.POST)
        institution_form = InstitutionForm(request.POST)

        # Handle Donation Application
        if 'submit_donation' in request.POST:
            if donation_form.is_valid():
                # Process the donation application (e.g., save to database)
                # Save logic can go here
                messages.success(request, 'Donation application submitted successfully!')
                return redirect('donationsapplication')

        # Handle Adding a New Institution
        if 'add_institution' in request.POST:
            if institution_form.is_valid():
                institution_form.save()
                messages.success(request, 'Institution added successfully!')
                return redirect('donationsapplication')


    else:
        donation_form = DonationApplicationForm()
        institution_form = InstitutionForm()

    return render(request, 'donationsapplication.html', {
        'donation_form': donation_form,
        'institution_form': institution_form,
    })



def selection(request):
    # Example: If the request is a POST (e.g., after a form submission)
    if request.method == 'POST':
        # Add logic here to handle form submission or any condition
        # If a certain condition is met, redirect to the 'thank_you' page
        return redirect('thank_you')

    # Get all counties by fetching unique counties
    counties = Institution.objects.values('county').distinct()

    # Render the page with counties
    return render(request, 'selection.html', {
        'counties': counties,
    })


def get_institutions(request):
    county = request.GET.get('county')
    if county:
        # Fetch institutions for the selected county
        institutions = Institution.objects.filter(county__iexact=county)
        institution_list = [{"name": institution.name} for institution in institutions]
        return JsonResponse({"institutions": institution_list})
    else:
        return JsonResponse({"institutions": []})

def upcoming_events(request):
    events = Event.objects.all()  # Fetch all events from the database
    return render(request, 'events.html', {'events': events})

def sponsor_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Get the event by its ID
    if request.method == 'POST':
        form = SponsorEventForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save to the database, send an email)
            sponsor_name = form.cleaned_data['sponsor_name']
            sponsor_email = form.cleaned_data['sponsor_email']
            donation_amount = form.cleaned_data['donation_amount']
            message = form.cleaned_data['message']

            # You can save the sponsor details to a Sponsor model or process as needed
            SponsorEvent.objects.create(
                sponsor_name=sponsor_name,
                sponsor_email=sponsor_email,
                donation_amount=donation_amount,
                message=message)

            # Redirect to a thank you page or confirmation page
            return redirect('thank_you')  # Redirect to a thank you page (you can create this page)
    else:
        form = SponsorEventForm()

    return render(request, 'sponsorevents.html', {'form': form, 'event': event})



def thank_you(request):
    return render(request, 'thank_you.html')


