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
$ bzip2 -dc enwiki-latest-pages-articles.xml.bz2 | python3 extract_parallel.py extracted-new/

```

# Example output

After the above, you will see the json files in `extracted-new/` directory, e.g.

```
{"id":892,"url":"http://en.wikipedia.org/wiki/Alfons_Maria_Jakob","text":"Alfons Maria Jakob (2 July 1884 in Aschaffenburg/Bavaria \u2013 17 October 1931 in Hamburg) was a German neurologist who worked in the field of neuropathology.\nHe was born in Aschaffenburg, Bavaria and educated in medicine at the universities of Munich, Berlin, and Strasbourg, where he received his doctorate in 1908. During the following year, he began clinical work under the psychiatrist Emil Kraepelin and did laboratory work with Franz Nissl and Alois Alzheimer in Munich.\nIn 1911, by way of an invitation from Wilhelm Weygandt, he relocated to Hamburg, where he worked with Theodor Kaes and eventually became head of the laboratory of anatomical pathology at the psychiatric State Hospital Hamburg-Friedrichsberg. Following the death of Kaes in 1913, Jakob succeeded him as prosector. During World War I he served as an army physician in Belgium, and afterwards returned to Hamburg. In 1919 he obtained his habilitation for neurology and in 1924 became a professor of neurology. Under Jakob's guidance the department grew rapidly. He made significant contributions to knowledge on concussion and secondary nerve degeneration and became a doyen of neuropathology.\nJakob was the author of five monographs and nearly 80 scientific papers. His neuropathological research contributed greatly to the delineation of several diseases, including multiple sclerosis and Friedreich's ataxia. He first recognised and described Alper's disease and Creutzfeldt\u2013Jakob disease (named along with Munich neuropathologist Hans Gerhard Creutzfeldt). He gained experience in neurosyphilis, having a 200-bed ward devoted entirely to that disorder. Jakob made a lecture tour of the United States (1924) and South America (1928), of which, he wrote a paper on the neuropathology of yellow fever.\nHe suffered from chronic osteomyelitis for the last seven years of his life. This eventually caused a retroperitoneal abscess and paralytic ileus from which he died following operation.","categories":[],"infobox_types":[],"annotations":[{"uri":"Aschaffenburg","surface_form":"Aschaffenburg","offset":35},{"uri":"Bavaria","surface_form":"Bavaria","offset":49},{"uri":"Hamburg","surface_form":"Hamburg","offset":78},{"uri":"Neurologist","surface_form":"neurologist","offset":100},{"uri":"Neuropathology","surface_form":"neuropathology","offset":139},{"uri":"Aschaffenburg","surface_form":"Aschaffenburg","offset":170},{"uri":"Bavaria","surface_form":"Bavaria","offset":185},{"uri":"Medicine","surface_form":"medicine","offset":209},{"uri":"University_of_Munich","surface_form":"Munich","offset":241},{"uri":"University_of_Berlin","surface_form":"Berlin","offset":249},{"uri":"University_of_Strasbourg","surface_form":"Strasbourg","offset":261},{"uri":"Psychiatrist","surface_form":"psychiatrist","offset":374},{"uri":"Emil_Kraepelin","surface_form":"Emil Kraepelin","offset":387},{"uri":"Franz_Nissl","surface_form":"Franz Nissl","offset":431},{"uri":"Alois_Alzheimer","surface_form":"Alois Alzheimer","offset":447},{"uri":"Munich","surface_form":"Munich","offset":466},{"uri":"Wilhelm_Weygandt","surface_form":"Wilhelm Weygandt","offset":512},{"uri":"Hamburg","surface_form":"Hamburg","offset":546},{"uri":"Theodor_Kaes","surface_form":"Theodor Kaes","offset":576},{"uri":"Anatomical_pathology","surface_form":"anatomical pathology","offset":637},{"uri":"Prosector","surface_form":"prosector","offset":776},{"uri":"World_War_I","surface_form":"World War I","offset":794},{"uri":"Belgium","surface_form":"Belgium","offset":840},{"uri":"Habilitation","surface_form":"habilitation","offset":909},{"uri":"Neurology","surface_form":"neurology","offset":926},{"uri":"Concussion","surface_form":"concussion","offset":1083},{"uri":"Neuropathology","surface_form":"neuropathology","offset":1149},{"uri":"Multiple_sclerosis","surface_form":"multiple sclerosis","offset":1339},{"uri":"Friedreich%27s_ataxia","surface_form":"Friedreich's ataxia","offset":1362},{"uri":"Alper%27s_disease","surface_form":"Alper's disease","offset":1417},{"uri":"Creutzfeldt%E2%80%93Jakob_disease","surface_form":"Creutzfeldt\u2013Jakob disease","offset":1437},{"uri":"Hans_Gerhard_Creutzfeldt","surface_form":"Hans Gerhard Creutzfeldt","offset":1505},{"uri":"Neurosyphilis","surface_form":"neurosyphilis","offset":1556},{"uri":"Yellow_fever","surface_form":"yellow fever","offset":1760},{"uri":"Osteomyelitis","surface_form":"osteomyelitis","offset":1799},{"uri":"Abscess","surface_form":"abscess","offset":1892},{"uri":"Paralysis","surface_form":"paralytic","offset":1904},{"uri":"Ileus","surface_form":"ileus","offset":1914}]}
```
