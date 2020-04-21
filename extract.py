
import sys
import json

from rubyslippers import extract_pages_from_dump
from rubyslippers import WikiExtractor

we = WikiExtractor()

output_dir = sys.argv[1]

for idx, page in enumerate(extract_pages_from_dump(sys.stdin)):
    wiki_page = we.parse(page)
    if wiki_page:
        with open(output_dir + str(wiki_page['id']) +'.json', 'w') as fout:
            json.dump(wiki_page, fout)
