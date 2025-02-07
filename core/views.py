from django.shortcuts import render, redirect, get_object_or_404
from core.models import Podcast
from django.contrib.auth.decorators import login_required
from core.forms import PodcastForm

# Create your views here.
def home(request):
    podcasts = Podcast.objects.all()[:3]
    return render(request, "index.html", context={"podcasts": podcasts})


@login_required
def upload_podcast(request):
    if request.method == "POST":
        form = PodcastForm(request.POST, request.FILES)

        if form.is_valid():
            podcast = form.save(commit=False)
            podcast.author = request.user
            podcast.save()

            return redirect("home")
        
    else:
        form = PodcastForm()
        return render(request, "upload_podcast.html", context={"form": form})
    
    
def list_podcasts(request):
    podcasts = Podcast.objects.all()
    return render(request, "list_podcasts.html", context={"podcasts": podcasts})


def podcast_detail(request, slug):
    podcast = get_object_or_404(Podcast, slug=slug)
    context = {"podcast": podcast}

    return render(request, "podcast_detail.html", context)