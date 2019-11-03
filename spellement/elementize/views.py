from django.shortcuts import render
from elementize.models import Element
from django.http import HttpResponseRedirect
from itertools import chain
import pdb

def index(request):
    """View function for home page of site."""

    return render(request, 'index.html')

def result(request):
    """View function for displaying the input as elements."""

    input = request.GET['input']
    word_list = input.split()

    #Validate that the input contains only letters; return error if needed
    if not all(word.isalpha() for word in word_list):
        context = {
            'initial': input,
            'error': 'No numbers or punctuation, please!',
        }
        return render(request, 'index.html', context=context)

    #Elementize the input
    start, element_set = 0, Element.objects.none()

    while start+1 <= len(input):

        if start+2 <= len(input):
            i = 2
        else:
            i = 1

        match = Element.objects.filter(symbol__iexact=input[start:start+i])

        if bool(match) == False: #this can only happen if i = 2; all single letters have a match
            i -= 1
            match = Element.objects.filter(symbol__iexact=input[start:start+i])

        element_set = list(chain(element_set, match))
        start += i

    context = {
        'input': input,
        'element_set': element_set,
    }
        
    return render(request, 'result.html', context=context)
