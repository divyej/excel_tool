import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException
from .forms import ExcelFileForm
import logging 

def upload_excel(request):
    if request.method == 'POST':
        form = ExcelFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']

            # Check if the file extension is valid
            if not uploaded_file.name.endswith('.xlsx'):
                return HttpResponseBadRequest('Invalid file format. Please upload an XLSX file.')

            try:
                workbook = load_workbook(uploaded_file, read_only=True)
                worksheet = workbook.active
                data = []
                for row in worksheet.iter_rows():
                    data.append([cell.value for cell in row])

                # Assuming you have an upload_excel.html template
                return render(request, 'display_excel.html', {'data': data, 'form': form, 'uploaded_file': uploaded_file})

            except InvalidFileException:
                return HttpResponseBadRequest('Invalid Excel file format')
        else:
            return render(request, 'upload_excel.html', {'form': form})
    else:
        form = ExcelFileForm()
    return render(request, 'upload_excel.html', {'form': form})
def save_excel_data(request):
    if request.method == "POST":
        if "save_button" in request.POST:
            # Extract headers from the first row
            headers = [cell for cell in request.POST.getlist("headers[]")]

            # Extract data from the remaining rows
            data = request.POST.getlist("data[]")

            # Calculate the number of columns based on the headers
            num_columns = len(headers)

            # Create a list of dictionaries where each dictionary represents a row
            rows = [dict(zip(headers, data[i:i+num_columns])) for i in range(0, len(data), num_columns)]

            # Convert the data to JSON
            json_data = json.dumps(rows)

            # Display JSON data in json_display.html
            return render(request, 'json_display.html', {'json_data': json_data})

    return render(request, 'upload_excel.html')