import os
import tempfile
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render  # Import render function
from .utils import save_structured_data_to_db
from restaurantmenu.PDFreader import extract_text_from_pdf
from restaurantmenu.AIreader import process_with_anthropic_api
from .forms import PDFUploadForm


@csrf_exempt
def upload_and_process_pdf(request):
    if request.method == "POST":
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data["pdf"]

            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file.write(pdf_file.read())
                temp_file_path = temp_file.name

            try:
                # Extract text and process
                extracted_text = extract_text_from_pdf(temp_file_path)
                if not extracted_text:
                    return JsonResponse({"error": "Failed to extract text from PDF"}, status=400)

                # Process with the external API
                structured_data_json = process_with_anthropic_api(extracted_text)
                if not structured_data_json:
                    return JsonResponse({"error": "Failed to process data with API"}, status=500)

                # Convert JSON to Python object and save to DB
                structured_data = json.loads(structured_data_json)
                if save_structured_data_to_db(structured_data):
                    return JsonResponse({"message": "Data processed and saved successfully"})
                else:
                    return JsonResponse({"error": "Failed to save data to database"}, status=500)

            finally:
                # Delete the temporary file after processing
                if os.path.exists(temp_file_path):
                    os.remove(temp_file_path)

        return JsonResponse({"error": "Invalid form submission"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


def upload_pdf_form(request):
    form = PDFUploadForm()
    return render(request, "restaurantmenu/upload_pdf.html", {"form": form})
