from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_http_methods, require_GET

from . import forms


@require_http_methods(["GET", "POST"])
def analyze_text(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.AnalyzeTextForm(request.POST)
        if form.is_valid():
            form.execute()
            return redirect(reverse("words") + f"?text={form.instance.id}")
    else:  # "GET" method.
        form = forms.AnalyzeTextForm()
    return render(request, "nlp/analyze_text.html", {"form": form})


@require_GET
def words(request: HttpRequest) -> HttpResponse:
    form = forms.GetWordsForm(request.GET)
    if form.is_valid():
        filtered_words = form.execute()
        text = form.cleaned_data["text"]
    else:
        filtered_words = []
        text = None
    context = {"form": form, "words": filtered_words, "text": text}
    return render(request, "nlp/words.html", context)
