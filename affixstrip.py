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


def argparser():
    from argparse import ArgumentParser
    ap = ArgumentParser()
    ap.add_argument('--standoff', default=False, action='store_true',
                    help='input is standoff (default: text)')
    ap.add_argument('--keep-quotes', default=False, action='store_true',
                    help='do not strip quotes')
    ap.add_argument('--changed-only', default=False, action='store_true',
                    help='only output changed strings')
    ap.add_argument('file', nargs='+')
    return ap


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
            base_forms = unique([a['BASEFORM'] for a in analyses])
            case_preserving = [
                b for b in base_forms if b[0].isupper() == word[0].isupper()
            ]
            if not case_preserving:    # require case-preserving
                info('no case-preserving: {} ({})'.format(word, base_forms))
                lemmas.append(word)
            else:
                if len(case_preserving) > 1:
                    info('multiple lemmas for {}: {}'.format(
                        word, case_preserving))
                lemmas.append(case_preserving[0])
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
    return string.strip(' "\'“”‘’')


def process_text(fn, options):
    with open(fn) as f:
        for ln, l in enumerate(f, start=1):
            l = l.rstrip('\n')
            s = strip_affix(l)
            if not options.keep_quotes:
                s = remove_quotes(s)
            if l != s or not options.changed_only:
                print('{}\t->\t{}'.format(l, s))


def process_standoff(fn, options):
    with open(fn) as f:
        for ln, l in enumerate(f, start=1):
            l = l.rstrip('\n')
            if l.isspace() or not l:
                if not options.changed_only:
                    print(l)
            elif l[0] != 'T':
                if not options.changed_only:
                    print(l)    # only process textbounds
            else:
                id_, type_and_span, text = l.split('\t')
                type_, start, end = type_and_span.split(' ')
                start, end = int(start), int(end)
                stext = strip_affix(text)
                if not options.keep_quotes:
                    stext = remove_quotes(stext)
                offset = text.find(stext)
                assert offset != -1
                start += offset
                end = start + len(stext)
                if stext != text or not options.changed_only:
                    print('{}\t{} {} {}\t{}'.format(
                        id_, type_, start, end, stext))


def main(argv):
    args = argparser().parse_args(argv[1:])
    for fn in args.file:
        if args.standoff:
            process_standoff(fn, args)
        else:
            process_text(fn, args)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
