
# Create your views here.
# village_info_system/grievance/views.py

from django.shortcuts import render, redirect
from .forms import GrievanceForm
from googletrans import Translator
from langdetect import detect,LangDetectException

def translate_to_english(text):
    translator = Translator()
    return translator.translate(text, dest='en').text

def translate_form_data(data, target_language):
    translated_data = {}
    for field_name, value in data.items():
        try:
            # Check if the text is not None and has a length greater than 5
            if value and len(value.strip()) > 5:
                # Detect language of the input text
                detected_language = detect(value)

                # Translate to English if the detected language is Hindi or Marathi
                if detected_language in ['hi', 'mr']:
                    translated_data[field_name] = translate_to_english(value)
                else:
                    translated_data[field_name] = value
            else:
                # If text is None or very short, keep the original value
                translated_data[field_name] = value if value else ''
        except LangDetectException:
            # Handle the LangDetectException by keeping the original value
            translated_data[field_name] = value if value else ''

    return translated_data


def grievance_form(request):
    if request.method == 'POST':
        form = GrievanceForm(request.POST, request.FILES)
        if form.is_valid():
            target_language = request.POST.get('target_language', 'en')
            translated_data = translate_form_data(form.cleaned_data, target_language)

            grievance = form.save(commit=False)
            grievance.user = request.user  # Associate the grievance with the logged-in user
            for field_name, value in translated_data.items():
                setattr(grievance, field_name, value)
            grievance.save()

            return redirect('homeApp:homePage')
    else:
        form = GrievanceForm()

    return render(request, 'complaintApp/grievance_form.html', {'form': form})


