import string

from django import forms

from . import models
from . import utils


class AnalyzeTextForm(forms.ModelForm):
    class Meta:
        model = models.Text
        fields = ["text", ]
        labels = {
            "text": "Text to analyze",
        }

    def execute(self) -> None:
        """
        Save words and their part of speech tags, met in text.
        """
        self.save()
        raw_text = self.cleaned_data["text"]
        for analyzed_word in utils.gen_alanyzed_words(
                text=raw_text,
                lang=self.instance.language.code,
                skip=string.punctuation,
        ):
            pos, _ = models.PartOfSpeech.objects.get_or_create(
                name=analyzed_word.pos,
            )
            models.Word.objects.create(
                word=analyzed_word.text,
                part_of_speech=pos,
                text=self.instance,
            )


class GetWordsForm(forms.Form):
    pos = forms.ModelChoiceField(
        queryset=models.PartOfSpeech.objects.all(),
        required=False,
    )
    text = forms.ModelChoiceField(
        queryset=models.Text.objects.all(),
        required=False,
    )

    def execute(self) -> list[models.Word]:
        words_query = {}
        if text := self.cleaned_data["text"]:
            words_query["text"] = text
        if pos := self.cleaned_data["pos"]:
            words_query["part_of_speech"] = pos
        words = list(models.Word.objects.filter(**words_query))
        return words
