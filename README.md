# BruteForceStringGenerator
Python class that generates string in bruteforce way

![](docs/string_gen.gif)

### Prerequisites
Python  >= 3.4

Development prerequisites

```
pipenv install
```

Production prerequisites

```
pipenv install --dev
```

To activate project's virtualenv run:
```
pipenv shell
```
## Running the tests

```
pipenv check
mypy brute_force_string_generator.py
python -m pytest tests
```


### Examples:

```
>>gen = BruteForceStringGenerator()
>>next(gen)
>>'a'

>>gen = BruteForceStringGenerator(initial_sequence='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
>>next(gen)
>>'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
```
