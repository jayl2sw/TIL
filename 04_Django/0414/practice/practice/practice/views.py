from django.shortcuts import redirect


def index(request):
    print('a')
    return redirect('eithers:index')