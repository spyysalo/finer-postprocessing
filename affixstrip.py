#!/usr/bin/env python3

import sys

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


def _normalize_affix(affix):
    affix = affix.strip()
    lemmas = []
    for word in affix.split():
        forms = _voikko.analyze(word)
        if not forms:
            warning('failed to analyze: "{}"'.format(word))
            lemmas.append(word)
        else:
            if len(forms) > 1:
                forms = [f for f in forms if f['CLASS'] == 'nimisana']
            if len(forms) > 1:
                warning('multiple forms for "{}": {}'.format(word, forms))
            lemmas.append(forms[0]['BASEFORM'])
    info('_normalize_affix({}) = {}'.format(affix, ' '.join(lemmas)))
    return ' '.join(lemmas)


def strip_affix(string):
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
