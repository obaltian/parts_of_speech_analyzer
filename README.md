# Parts of Speech Analyzer

Parts of Speech is a web application analyzing text for parts of speech tags.

## Features

- Analyze your text for words and their part of speech tags.
- Review all previously analyzed data using filtering and word cloud chart.

## Tech

Dillinger uses a number of open source projects to work properly:

- [Django] - Simple web application builder framework.
- [Spacy] - Powerful library for natural language processing.
- [Googletrans] - Python interface to Google Translate API. Used for language detection.

## Limitations

Currently application may analyze English text only.


# To Do

The most important thing to do in the nearest future is to improve words page appearence.
Currently this is proof of concept, so appearence was not in focus.


## Installation

Analyzer requires python3.9 and higher to run.

Installation by poetry is shown, however, requirements.txt file is also present.
Install all dependencies, migrate database and run the server:

```sh
cd parts_of_speech_analyzer
poetry install
poetry run ./manage.py migrate
poetry run ./manage.py runserver
```


## License

GPLv3.0

**Free Software, Hell Yeah!**


[Django]: <https://www.djangoproject.com/>
[Spacy]: <https://spacy.io/>
[Googletrans]: <https://py-googletrans.readthedocs.io/en/latest/>

[PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
[PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
[PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
[PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
[PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
[PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
