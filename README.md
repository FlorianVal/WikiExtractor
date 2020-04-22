# A Wikipedia Plain Text Extractor with Link Annotations (and stuff)

This is port of @jodaiber's [Annotated-WikiExtractor](https://github.com/jodaiber/Annotated-WikiExtractor) which is built upon [Wikipedia Extractor by Medialab](http://medialab.di.unipi.it/wiki/Wikipedia_Extractor).

# Requirements

Supports Python 3 only.

```
pip install -U tqdm joblib python-rapidjson
```

# Usage

```

$ git clone https://github.com/alvations/rubyslippers.git
$ cd rubyslippers

# This will take a while...
$ wget https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2

# Single thread.
$ mkdir extracted-new
$ bzip2 -dc enwiki-latest-pages-articles.xml.bz2 | python3 extract.py extracted-new/

# Multi-thread.
$ mkdir extracted-new
$ bzip2 -dc enwiki-latest-pages-articles.xml.bz2 | python3 extract_parallel.py extracted

```
