try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise


import unittest

class TestPessoa(unittest.TestCase):
    def setUp():
        self.p1 = Pessoa('Jonas', 'Henrique')

    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        pass

if __name__ == '__main__':
    unittest.main()