from imgFind import *
from rutermextract import TermExtractor
term_extractor = TermExtractor()
text = u'Съешь ещё этих мягких французских булок да выпей же чаю.'
for term in term_extractor(text, nested=True):
	print(term.normalized)
	if getPict(term.normalized):
		break