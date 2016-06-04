class Equals(object):

    def __init__(self, data):
        self.data = data

    def interpret(self, context):
        return self.data == context


class Contains(object):

    def __init__(self, data):
        self.data = data

    def interpret(self, context):
        return self.data in context


class Compare(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second


class Or(Compare):

    def interpret(self, context):
        return (
            self.first.interpret(context) or self.second.interpret(context)
        )


class And(Compare):

    def interpret(self, context):
        return (
            self.first.interpret(context) and self.second.interpret(context)
        )


rules = {
    'is': {
        'parrot': Equals('parrot'),
        'sparrow': Equals('sparrow'),
        'cat': Equals('cat'),
    },
    'has': {
        't': Contains('t'),
        'p': Contains('p'),
        'c': Contains('c'),
    }
}

rules['is']['bird'] = Or(rules['is']['parrot'], rules['is']['sparrow'])
rules['is']['animal'] = Or(rules['is']['bird'], rules['is']['cat'])
rules['is']['animal with t'] = And(rules['is']['animal'], rules['has']['t'])
rules['is']['animal with t and a bird'] = And(rules['is']['animal with t'], rules['is']['bird'])


print 'Is cat a bird? {}'.format(rules['is']['bird'].interpret('cat'))
print 'Is sparrow a bird? {}'.format(rules['is']['bird'].interpret('sparrow'))
print 'Is cat an animal? {}'.format(rules['is']['animal'].interpret('cat'))
print 'Is parrot an animal and a bird and has letter "t"? {}'.format(rules['is']['animal with t and a bird'].interpret('parrot'))
print 'Is sparrow an animal and a bird and has letter "t"? {}'.format(rules['is']['animal with t and a bird'].interpret('sparrow'))
