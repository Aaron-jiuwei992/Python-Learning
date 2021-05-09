from django.shortcuts import render
from django.views import View
from .kuwoMusic_api import get_music_info
# Create your views here.

class Index(View):
    def get(self, request):
        key_word = request.GET.get("q")
        if not key_word:
            return render(request, 'index.html')
        else:
            music_info = get_music_info(key_word)
            return render(request, 'index.html', {'music_info': music_info})




