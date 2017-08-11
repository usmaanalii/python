import unittest


def raises_error(*args, **kwargs):
    raise ValueError('Invalid value: %s%s' % (args, kwargs))


class ExceptionTest(unittest.TestCase):
    """docstring for ExceptionTest."""

    def test_trap_locally(self):
        try:
            raises_error('a', b='c')
        except ValueError:
            pass
        else:
            self.fail('Did not see ValueError')

    def test_assert_raises(self):
        self.assertRaises(ValueError, raises_error, 'a', b='c')


if __name__ == '__main__':
    unittest.main()
