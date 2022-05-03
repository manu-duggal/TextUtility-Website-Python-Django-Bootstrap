# Self created file - Manu

from pydoc import pager
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def analyze(request):
    # Get the text
    text = request.POST.get('text', 'default')

    # Collect value of checkbox
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    # Analyze the text
    final_freq = ''
    final = text
    if removepunc == 'on':
        puncs = "!@#$%^&*()_+={[]}|,./<>?;':"
        final = ''
        for val in text:
            if val not in puncs:
                final += val
        text = final
    
    if uppercase == 'on':
        final = text.upper()
        text = final
    
    if newlineremove == 'on':
        final = ''
        for val in text:
            if val != '\n' and val != '\r':
                final += val
        text = final

    if spaceremove == 'on':
        final = ''
        for index, val in enumerate(text[:-1]):
            if not (val == ' ' and text[index+1] == ' '):
                final += val
        final += text[-1]
        text = final
    
    if charcount == 'on':
        freq = len(text)
        final_freq = 'The total count is ' + str(freq)


    params = {'text': final, 'freq' : final_freq}
    return render(request, 'analyze.html', params)



def contact(request):
    return render(request, 'contact.html')