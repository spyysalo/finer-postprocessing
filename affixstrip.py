#!/usr/bin/env python3

import sys
import re

try:
    from voikko import libvoikko
except ImportError:
    print('''Failed to import voikko. See https://voikko.puimula.org/ and

    pip3 install voikko
''')
    sys.exit(1)

from logging import warning, info

from affixdata import stripped_affix, not_split


_voikko = libvoikko.Voikko('fi')


_NOUN_CLASSES = set(['nimisana', 'etunimi'])


# Handle "-niminen", "-merkkinen", etc. (e.g. "Aaro-niminen mies")
_SPLIT_AFFIX_RE = re.compile(r'^([^a-zA-ZäöÄÖ]*[a-zA-ZäöÄÖ].*)(- *)((?:nimi|merkki)(?:nen|set|sen|sten|seen|stä|siä|sessä|sestä|selle|sellä|senä|seksi|seltä|sissä|sistä|siin|sillä|sinä|siltä|sille|siksi) [^a-zA-ZäöÄÖ]*[a-zA-ZäöÄÖ].*)$')


def _possible_splits(text):
    start = 1
    while start < len(text) and not text[start].isalpha():
        start += 1    # don't split before first alpha
    while start < len(text):
        h_start = text.find('-', start)
        if h_start == -1:
            break
        h_end = h_start+1
        while h_end < len(text) and not text[h_end].isalpha():
            h_end += 1
        if h_end == len(text):
            break    # don't split after last alpha
        yield text[:h_start], text[h_start:h_end], text[h_end:]
        start = h_start + 1


def unique(iterable):
    uniq, seen = [], set()
    for i in iterable:
        if i not in seen:
            uniq.append(i)
            seen.add(i)
    return uniq


def _normalize_affix(affix):
    affix = affix.strip()
    lemmas = []
    for word in affix.split():
        if not any(c.isalpha() for c in word):
            lemmas.append(word)    # no change for non-alpha
            continue
        analyses = _voikko.analyze(word)
        if not analyses:
            if not word[0].isupper():    # no warning for likely proper nouns
                info('failed to analyze: "{}"'.format(word))
            lemmas.append(word)
        else:
            noun_analyses = [a for a in analyses if a['CLASS'] in _NOUN_CLASSES]
            if noun_analyses:
                analyses = noun_analyses    # prioritize noun readings
            baseforms = unique([a['BASEFORM'] for a in analyses])
            case_preserving = [
                b for b in baseforms if b[0].isupper() == word[0].isupper()
            ]
            if case_preserving:
                baseforms = case_preserving    # prioritize case-preserving
            if len(baseforms) > 1:
                info('multiple lemmas for "{}": {}'.format(word, baseforms))
            lemmas.append(baseforms[0])
    info('_normalize_affix({}) = {}'.format(affix, ' '.join(lemmas)))
    return ' '.join(lemmas)


def strip_affix(string):
    m = _SPLIT_AFFIX_RE.match(string)
    if m:
        text, hyphen, affix = m.groups()
        assert text + hyphen + affix == string
        return text
    for text, hyphen, affix in _possible_splits(string):
        assert text + hyphen + affix == string
        affix = _normalize_affix(affix)
        if (text, affix) in not_split:
            break
        elif affix in stripped_affix:
            return text
    return string


def remove_quotes(string):
    return string.strip('" ')


def process(fn):
    with open(fn) as f:
        for ln, l in enumerate(f, start=1):
            l = l.rstrip('\n')
            s = strip_affix(l)
            s = remove_quotes(s)
            print('{}\t->\t{}'.format(l, s))


def main(argv):
    for fn in argv[1:]:
        process(fn)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
