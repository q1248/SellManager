from django.shortcuts import render

# Create your views here.
from speed.models import someTips


def index(request):
    allTips = someTips.objects.all()
    news = someTips.objects.filter(group="new")
    problem=someTips.objects.filter(group="problem")
    travelTips=someTips.objects.filter(group="travelTips")
    contex = {
        'allTips':allTips,
        'news': news,
        'problem':problem,
        'travelTips':travelTips,

    }
    return render(request, 'speed/index.html', contex)
