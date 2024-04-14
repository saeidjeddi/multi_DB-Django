from django.shortcuts import render
from django.views import View
from .models import Home

class HomeView(View):
    def get(self, request):
        name = Home.objects.using('home_db').all()   # or   #name = Home.objects.all()
        context = {'name':name}
        return render(request, 'home/index.html', context)

