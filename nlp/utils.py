import typing as tp

import googletrans
import spacy
from django.conf import settings


class LanguageMeta(tp.NamedTuple):
    code: str
    name: str


def detect_language(text: str) -> tp.Optional[LanguageMeta]:
    """
    Detects the text language using Google Translate API.

    Google Translate was chosen over langdetect since the last one does not
    define correctly on small text (with just few words).

    :param text: Text to be used for definition.
    :returns: Language code, or None if language could not be defined.
    """
    result = None
    try:
        # TODO: Use detection confidence rate.
        #  Not used for now since googletrans may return confidence=None (why?).
        detection = googletrans.Translator().detect(text)
        result = LanguageMeta(detection.lang,
                              get_language_by_code(detection.lang),
                              )
    finally:
        return result


def get_language_by_code(language_code: str) -> str:
    return googletrans.LANGUAGES[language_code]


class AnalyzedWord(tp.NamedTuple):
    text: str
    pos: str

    @classmethod
    def fromtoken(cls, token: spacy.tokens.Token):
        return cls(text=token.text, pos=token.pos_)


def gen_alanyzed_words(text: str, lang: str, *, skip: tp.Iterable[str] = None,
                       ) -> tp.Generator[AnalyzedWord, None, None]:
    """
    Generates the analyzed word objects from text.

    :param text: Text to analyze.
    :param lang: Text language code.
    :param skip: Tokens to be skipped (e.g. punctuation symbols).
    """
    if skip is None:
        skip = []
    try:
        nlp = settings.LANGUAGE_MODELS[lang]
    except KeyError:
        raise ValueError(
            f"Language '{lang}' is not supported "
            f"(probably was forgotten to be added to setting "
            f"LANGUAGE_MODELS?). "
            f"Supported languages: {list(settings.LANGUAGE_MODELS)}."
        )

    tokens = nlp(text)
    for token in tokens:
        if token.text in skip:
            continue
        yield AnalyzedWord.fromtoken(token)
