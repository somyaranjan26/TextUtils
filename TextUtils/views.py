from django.shortcuts import render
import string


def index(request):
    return render(request, "Index.html")


def analyze(request):
    data = request.POST.get('text', 'default')
    removePunc = request.POST.get('removePunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newLineRemover = request.POST.get('newLineRemover', 'off')
    charCount = request.POST.get('charCount', 'off')
    spaceRemover = request.POST.get('spaceRemove', 'off')

    if removePunc == 'on':
        analyzedData = ""
        for char in data:
            if char not in string.punctuation:
                analyzedData = analyzedData + char

        paras = {'task': 'Removed Punctuations', 'analyzedText': analyzedData}
        data = analyzedData
        return render(request, 'analyze.html', paras)

    if capitalize == 'on':
        analyzedData = ""
        for char in data:
            analyzedData = analyzedData + char.upper()

        paras = {'task': 'Convert Uppercase', 'analyzedText': analyzedData}
        return render(request, 'analyze.html', paras)

    elif newLineRemover == 'on':
        analyzedData = ""
        for char in data:
            if char != '\n' and char != '\r':
                analyzedData = analyzedData + char

        paras = {'task': 'Extra line Remover', 'analyzedText': analyzedData}
        return render(request, 'analyze.html', paras)

    elif charCount == 'on':
        count = 0
        for char in data:
            count = count + 1

        paras = {'task': 'Character Counter', 'analyzedText': count}
        return render(request, 'analyze.html', paras)

    elif spaceRemover == 'on':
        analyzeData = ''
        for i, char in enumerate(data):
            if not (data[i] == ' ' and data[i + 1] == ' '):
                analyzeData = analyzeData + char

        paras = {'task': 'Space Remover', 'analyzedText': analyzeData}
        return render(request, 'analyze.html', paras)

    else:
        error = {'task': 'Select any one option', 'analyzedText': '----x-----x----'}
        return render(request, 'analyze.html', error)
