from django.shortcuts import render

# Create your views here.
def home_screen_view(request, *args):
    context = {}
    if args:
        context.update((args[0]))
    return render(request, 'base/home.html', context)