from django import forms

class PDFUploadForm(forms.Form):
    pdf = forms.FileField(
        label="Upload a PDF",
        help_text="Please upload a valid PDF file."
    )
