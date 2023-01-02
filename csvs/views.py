from django.shortcuts import render
from .forms import CsvForm
from .models import Csv
import csv
from django.contrib.auth.models import User
from products.models import Product, Purchase
from django.core.files.storage import default_storage
from pprint import pprint
# Create your views here.

# def upload_file_view(request):
#     error_message = None
#     success_message = None
#     form = CsvForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         form = CsvForm()
#         #print("All is well !!!! ")
#         #try:
#         #print("All is well !!!! ")
#         obj = Csv.objects.get(activated=False)
#         print(f"All is well !!!! obj: {obj}")
#         print(f"All is well !!!! obj.file_name:  {obj.file_name}")
#         #with open(obj.file_name.path, 'r') as f:
#         pprint(f"All is well obj !!!! {dir(obj.file_name)}")
#         #f= default_storage.open(Csv.objects.name, 'r')
#         reader= obj.file_name.read().decode()
#         print(f"All is well !!!! reader: {reader}")
#             #reader = csv.reader(f)
#             # print(f"All is well !!!! {reader}")
#         #reader = f.read()
        
#         for row in reader.split('\n'):
#             print(row)
#             #row = " ".join(row)
#             row = row.replace(";", " ")
#             row = row.split()
#             #print(row)
#             user = User.objects.get(id = row[3])   
#             print(user)
#             prod , _ = Product.objects.get_or_create(name=row[0]) 
#             Purchase.objects.create(
#                 product=prod,
#                 price = int(row[2]),
#                 quantity =  int(row[1]), 
#                 salesman = user,
#                 date = row[4]+" "+row[5]
#                 ) 



#         #obj.activated=True
#         #obj.save()
#         success_message="Uploaded Successfully"
#         # except:
#         #     error_message = "Ooops!!!! , Something went wrong"

#     context = {
#         'form': form,
#         'success_message': success_message,
#         'error_message': error_message,
#     }


#     return render(request, 'csvs/upload.html', context)


def upload_file_view(request):
    error_message = None
    success_message = None
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()
        try:
            obj = Csv.objects.get(activated=False)
            reader= obj.file_name.read().decode()
            
            for row in reader.split('\n'):
                #print(row)
                #row = " ".join(row)
                row = row.replace(";", " ")
                row = row.split()
                #print(row)
                user = User.objects.get(id = row[3])   
                #print(user)
                prod , _ = Product.objects.get_or_create(name=row[0]) 
                Purchase.objects.create(
                    product=prod,
                    price = int(row[2]),
                    quantity =  int(row[1]), 
                    salesman = user,
                    date = row[4]+" "+row[5]
                    ) 



            obj.activated=True
            obj.save()
            success_message="Uploaded Successfully"
        except:
            error_message = "Ooops!!!! , Something went wrong"

    context = {
        'form': form,
        'success_message': success_message,
        'error_message': error_message,
    }


    return render(request, 'csvs/upload.html', context)
