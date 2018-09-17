# BruteForceStringGenerator
Python class that generates string in bruteforce way

### Prerequisites

Development prerequisites

```
pip install pytest
```

Production prerequisites

```

```

## Running the tests

```
python -m pytest tests
```


### Examples:

```
gen = BruteForceStringGenerator()
gen.next_string()
'a'

gen = BruteForceStringGenerator(initial_sequence='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
gen.next_string()
'baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
```
