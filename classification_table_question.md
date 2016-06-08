You are given a list of objects and a list of functions.

Each function takes an object and returns True or False. So each function corresponds to a question that can be asked about an object.

The task is to write a function called 'classify_objects' that creates a table showing how many objects are True/False for each question. The following example should explain this precisely.

The function you need to write will take in a list of objects and a list of question functions, like this:


```python
def classify_objects(list_of_objects, list_of_functions):
    pass
```

Suppose the objects are

````python
sparrow = {'name': 'sparrow', 'type': 'bird'}
eagle= {'name': 'eagle', 'type': 'bird'}
fox = {'name': 'fox', 'type': 'mammal'}
```

and the functions are

```python
def is_bird(object):
    return object['type'] == 'bird'


def is_mammal(object):
    return object['type'] == 'mammal'
```

Then we would call the function like this:

```python
objects = [sparrow, eagle, fox]
functions = [is_bird, is_mammal]

classify_objects(objects, functions)
```

Your function should return this data structure, which represents a classification table:

```python
[
    (False, False, 0),
    (False, True, 1),
    (True, False, 2),
    (True, True, 0),
]
```

Each tuple is of the form

```
(function_1_true?, function_2_true?, number_of_matching_objects)
```

So in that example return value, the first tuple shows that there are zero objects that are not-bird AND not-mammal, and the second shows that there is one object that is not-bird AND mammal.


#### Example solutions

##### Solution 1


```python
import itertools


def classify_objects(objects, functions):
    possible_answers = [(False, True) for f in functions]

    all_row_answers = itertools.product(*possible_answers)

    def negate(function):
        return lambda obj: not function(obj)

    def object_matches_this_row(obj, row_functions):
        return all(f(obj) for f in row_functions)

    rows = []
    for row_answers in all_row_answers:

        row_functions = [
            function if answer else negate(function)
            for function, answer in zip(functions, row_answers)
        ]

        count = sum(object_matches_this_row(obj, row_functions)
                    for obj in objects)

        rows.append(row_answers + (count,))

    return rows
```

##### Solution 2

```python
import itertools


class Question:
    def __init__(self, function, answer):
        self.function = function
        self.answer = answer

    def negated(self):
        return Question(
            function=lambda obj: not self.function(obj),
            answer=not self.answer
        )


def classify_objects_2(objects, functions):
    questions = [Question(f, True) for f in functions]
    negated_questions = [q.negated() for q in questions]

    pairs_of_questions = zip(negated_questions, questions)

    all_row_questions = itertools.product(*pairs_of_questions)

    def object_matches_this_row(obj, row_questions):
        return all(q.function(obj) for q in row_questions)

    rows = []
    for row_questions in all_row_questions:

        count = sum(object_matches_this_row(obj, row_questions)
                    for obj in objects)

        row = [q.answer for q in row_questions]
        row.append(count)

        rows.append(tuple(row))

    return rows
```
