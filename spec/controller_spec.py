from mamba import description, context, it
from expects import expect, equal

with description('when testing an feature') as self:
    with it('asserts its all right'):
        expect('This works!').to(equal('This works!'))
