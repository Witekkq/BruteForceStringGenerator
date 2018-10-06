# BruteForceStringGenerator
Python class that generates string in bruteforce way

### Prerequisites
Python  >= 3.4

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
>>gen = BruteForceStringGenerator()
>>next(gen)
>>'a'

>>gen = BruteForceStringGenerator(initial_sequence='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
>>next(gen)
>>'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
```
