# finer-postprocessing

Postprocessing tools for FiNER tagger/data

## Quickstart

Test on examples from Wikipedia marked by FiNER-tagger:

```
python3 affixstrip.py --changed-only data/finer-wiki-examples.txt | less
```

Test on standoff annotations from Turku NER corpus:

```
diff data/turku-ner-corpus-train.ann \
    <(python3 affixstrip.py --standoff data/turku-ner-corpus-train.ann) | less
```
