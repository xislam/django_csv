import csv
import io

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from webapp.models import ModelCSV


def home(request):
    documents = ModelCSV.objects.all()
    return render(request, 'index.html', {'documents': documents})


def csv_upload(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=';', quotechar="|"):
            _, created = ModelCSV.objects.update_or_create(
                code=column[0],
                name=column[1],
                level1=column[2],
                level2=column[3],
                level3=column[4],
                price=column[5],
                sp_price=column[6],
                quantity=column[7],
                property_fields=column[8],
                joint_purchases=column[9],
                unit_of_measure=column[10],
                picture=column[11],
                display_on_main_page=column[12],
                description=column[13],
            )
        fs = FileSystemStorage()
        filename = fs.save(csv_file.name, csv_file)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')

