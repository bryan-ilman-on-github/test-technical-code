from django.shortcuts import render, redirect
from test_technical_code.forms import AngkaForm

import sympy

def show_homepage(request):
    form = AngkaForm()
    return render(request, 'index.html', {'form': form})

def backend(request):
    output = ""

    if 'generate-segitiga' in request.POST:
        form = AngkaForm(request.POST)
        if form.is_valid():
            angka = form.save(commit=False)

            counter = 1
            for char in str(angka.masukan):
                output += char + (counter * "0") + "\n"
                counter += 1
    elif 'generate-bilangan-ganjil' in request.POST:
        form = AngkaForm(request.POST)
        if form.is_valid():
            angka = form.save(commit=False)

            for i in range(int(angka.masukan) + 1):
                if i % 2 == 1:
                    output += f"{i}, "
    elif 'generate-bilangan-prima' in request.POST:
        form = AngkaForm(request.POST)
        if form.is_valid():
            angka = form.save(commit=False)

            for i in range(int(angka.masukan) + 1):
                if sympy.isprime(i):
                    output += f"{i}, "
            redirect('homepage')
    else:
        form = AngkaForm()

    return render(request, 'index.html', {'form': form, 'output': output})