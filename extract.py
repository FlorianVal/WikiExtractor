import sys
import rapidjson as json

from tqdm import tqdm


from WikiExtractor import extract_pages_from_dump
from WikiExtractor import WikiExtractor

we = WikiExtractor('en')

output_dir = sys.argv[1]

for idx, page in tqdm(enumerate(extract_pages_from_dump(sys.stdin))):
    wiki_page = we.extract(page)
    if wiki_page:
        with open(output_dir + str(wiki_page['id']) +'.json', 'w') as fout:
            json.dump(wiki_page, fout)
