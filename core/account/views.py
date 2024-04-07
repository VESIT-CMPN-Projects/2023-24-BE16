import os
from django.shortcuts import render,redirect

from account.models import User
from .forms import SignUpForm,LoginForm
from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout as auth_logout
from PIL import Image
import pytesseract
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages




# Create your views here.
def index(request):
    return render(request, 'index.html')

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            # Extract text from uploaded documents and save in User model
            for field_name in form.files:
                image_field_name = f"{field_name}_image"
                text_field_name = f"{field_name}_text"

                uploaded_image = form.cleaned_data.get(image_field_name)
                entered_text = form.cleaned_data.get(text_field_name)

                if uploaded_image and entered_text:
                    image_path = os.path.join(settings.MEDIA_ROOT, str(uploaded_image))
                    extracted_text = extract_text_from_image(image_path)

                    # Check if the extracted text matches the entered text
                    if extracted_text.strip().lower() != str(entered_text).strip().lower():
                        # Delete the user and associated documents if verification fails
                        user.delete()
                        form.add_error(image_field_name, 'Verification failed. The provided document does not match the entered information.')
                        return render(request, 'register.html', {'form': form, 'msg': msg})

                    # Save the extracted text in the User model
                    setattr(user, text_field_name, extracted_text)
                    user.save()
                    user.approve_yn = False  # Set approval status to True

            
            msg = 'User created successfully.'
            return redirect('account:login_view')
        else:
            msg = 'Form is not valid.'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and user.is_approved:  # Check if user is approved
                login(request, user)
                if user.is_admin:
                    return redirect('adminhome')
                elif user.is_user:
                    return redirect('homeApp:homePage')
            else:
                msg = 'Your account is not approved yet. Please wait for admin approval.'
        else:
            msg = 'Error validating form'

    return render(request, 'login.html', {'form': form, 'msg': msg})



# def admin(request):
#     return render(request,'adminHome/home.html')


# def userPerson(request):
#     return render(request,'homeApp/home.html')

@login_required
def custom_logout(request):
    auth_logout(request)
    # You can customize the redirect URL after logout
    return redirect('homeApp:homePage')

def user_list(request):
    # Fetch the list of users from the database
    user_list = User.objects.all()
    # Pass the user list to the template
    context = {'user_list': user_list}
    return render(request, 'user_list.html', context)


@login_required
def approve_user(request, user_id):
    if request.user.is_admin:  # Assuming you have an 'is_admin' field in your User model
        user = User.objects.get(id=user_id)
        user.is_approved = True
        user.save()
        messages.success(request, 'User approved successfully.')
    else:
        messages.error(request, 'You do not have permission to approve users.')

    return redirect('account:user_list')






