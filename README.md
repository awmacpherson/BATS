# BATS
Python loader for the Bigger Analogy Test Set (BATS).

API:
- `load(path)` --- finds BATS files rooted at `path` and parses filenames, storing the state in the module's global namespace.
- `print_tags()` --- print a list of pairs `{ID}: {tag}` identifying files.
- `get_question(id_or_tag)` --- retrieve a "question" as a nested tuple in the format
  ```
  ( (example_word_1, example_word_2), test_word_1 ), test_word_2
  ```
  where `(example_word_1, example_word_2)` and `(test_word_1, test_word_2)` are *analogous*, i.e. "`example_word_1` is to `example_word_2` as `test_word_1` is to `test_word_2`." Pairs are selected randomly using the standard library `random` module. If no argument is given, select a file randomly.
- `get_all_questions(id_or_tag)` --- Retrieve a list of "questions" exhausting all pairs of analogies from a given file or, if no argument is given, the entire dataset.

Sample session:
```Python
In [1]: import BATS

In [2]: BATS.load()
In [3]: BATS.print_tags()
```
```
I01: noun - plural_reg
I02: noun - plural_irreg
I03: adj - comparative
I04: adj - superlative
I05: verb_inf - 3pSg
I06: verb_inf - Ving
I07: verb_inf - Ved
I08: verb_Ving - 3pSg
I09: verb_Ving - Ved
I10: verb_3pSg - Ved
D01: noun+less_reg
D02: un+adj_reg
D03: adj+ly_reg
D04: over+adj_reg
D05: adj+ness_reg
D06: re+verb_reg
D07: verb+able_reg
D08: verb+er_irreg
D09: verb+tion_irreg
D10: verb+ment_irreg
E01: country - capital
E02: country - language
E03: UK_city - county
E04: name - nationality
E05: name - occupation
E06: animal - young
E07: animal - sound
E08: animal - shelter
E09: things - color
E10: male - female
L01: hypernyms - animals
L02: hypernyms - misc
L03: hyponyms - misc
L04: meronyms - substance
L05: meronyms - member
L06: meronyms - part
L07: synonyms - intensity
L08: synonyms - exact
L09: antonyms - gradable
L10: antonyms - binary
```
```Python
In [4]: BATS.get_question("L07")                              
Out[4]: [('interesting', 'exciting'), ('tired', 'exhausted')] 

In [5]: BATS.get_question("male - female")
Out[5]: [('emperor', 'empress'), ('daddy', 'mommy')]

In [6]: BATS.get_all_questions("I01")
Out[6]:
[[('album', 'albums'), ('fact', 'facts')],
 [('example', 'examples'), ('area', 'areas')],
 [('town', 'towns'), ('solution', 'solutions')],
 [('car', 'cars'), ('resource', 'resources')],
 [('language', 'languages'), ('song', 'songs')],
 [('department', 'departments'), ('member', 'members')],
 [('night', 'nights'), ('college', 'colleges')],
 [('population', 'populations'), ('road', 'roads')],
 [('death', 'deaths'), ('friend', 'friends')],
 [('development', 'developments'), ('student', 'students')],
 [('application', 'applications'), ('god', 'gods')],
 [('law', 'laws'), ('director', 'directors')],
 [('hour', 'hours'), ('office', 'offices')],
 [('event', 'events'), ('day', 'days')],
 [('customer', 'customers'), ('week', 'weeks')],
 [('science', 'sciences'), ('website', 'websites')],
 [('street', 'streets'), ('player', 'players')],
 [('river', 'rivers'), ('year', 'years')],
 [('difference', 'differences'), ('period', 'periods')],
 [('thing', 'things'), ('version', 'versions')],
 [('user', 'users'), ('product', 'products')],
 [('idea', 'ideas'), ('month', 'months')],
 [('problem', 'problems'), ('role', 'roles')],
 [('village', 'villages'), ('council', 'councils')],
 [('government', 'governments'), ('system', 'systems')]]
```
