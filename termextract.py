from imgFind import *
from rutermextract import TermExtractor
term_extractor = TermExtractor()
text = u'Съешь ещё этих мягких французских булок да выпей же чаю.'
for term in term_extractor(text):
	print(term.normalized)
	getPict(term.normalized)


