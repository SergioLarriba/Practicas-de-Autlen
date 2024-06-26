#!/usr/bin/env python

import re
import unittest

from regular_expressions import RE0, RE1, RE2, RE3, RE4, RE5, RE6


class TestP0(unittest.TestCase):
    """Tests of assignment 0."""

    def check_expression(self, expr: str, string: str, expected: bool) -> None:
        with self.subTest(string=string):
            match = re.fullmatch(expr, string)
            self.assertEqual(bool(match), expected)
    
    def test_exercise_0(self) -> None:
        self.check_expression(RE0, "a", True)
        self.check_expression(RE0, "bbbbaba", True)

        self.check_expression(RE0, "abbab", False)
        self.check_expression(RE0, "b", False)
        self.check_expression(RE0, "", False)

    def test_exercise_1(self) -> None:
        self.check_expression(RE1, "", True)
        self.check_expression(RE1, "a", True)
        self.check_expression(RE1, "ab", True)
        self.check_expression(RE1, "aab", True)

        self.check_expression(RE1, "ba", False)
        self.check_expression(RE1, "aba", False)
    
    def test_exercise_2(self) -> None:
        self.check_expression(RE2, "a", True)
        self.check_expression(RE2, "aba", True)
        self.check_expression(RE2, "ab", True)

        self.check_expression(RE2, "aa", False)
        self.check_expression(RE2, "bb", False)
        self.check_expression(RE2, "aaa", False)
        self.check_expression(RE2, "", False)

    def test_exercise_3(self) -> None:
        self.check_expression(RE3, "aabb", True)
        self.check_expression(RE3, "abbaa", True)
        self.check_expression(RE3, "bbaaa", True) 

        self.check_expression(RE3, "ababaa", False)
        self.check_expression(RE3, "abbabb", False)
        self.check_expression(RE3, "bba", False) 
        self.check_expression(RE3, "", False) 
    
    def test_exercise_4(self) -> None:
        self.check_expression(RE4, "0", True)
        self.check_expression(RE4, "1", True)
        self.check_expression(RE4, "255", True)

        self.check_expression(RE4, "-1", False)
        self.check_expression(RE4, "3.33", False)
        self.check_expression(RE4, "256", False)


        self.check_expression(RE4, "", False) #rechazamos la cadena vacia
        self.check_expression(RE4, "007", False) #rechaza ceros innecesarios a la izquierda
        self.check_expression(RE4, "017", False) #rechaza ceros innecesarios a la izquierda
        self.check_expression(RE4, "/(*", False) #rechaza simbolos que nos estan en el alfabeto
        self.check_expression(RE4, "+1", False)
        for i in range(0, 255):
                self.check_expression(RE4, str(i), True)	
        for i in range(256, 2000):
                self.check_expression(RE4, str(i), False)
    
    def test_exercise_5(self) -> None:
        self.check_expression(RE5, "a", True)
        self.check_expression(RE5, "aa", True)
        self.check_expression(RE5, "abaa", True)
        self.check_expression(RE5, "abaabaa", True)
        self.check_expression(RE5, "baababaa", True)

        self.check_expression(RE5, "aaa", False)
        self.check_expression(RE5, "aabaaaa", False)
        self.check_expression(RE5, "bbaabaabababaa", False)
    
    def test_exercise_6(self) -> None:
        self.check_expression(RE6, "", True)
        self.check_expression(RE6, "1", True)
        self.check_expression(RE6, "0", True)
        self.check_expression(RE6, "0011", True)
        self.check_expression(RE6, "110", True)
        self.check_expression(RE6, "11010101", True)
        self.check_expression(RE6, "011001010", True)
        self.check_expression(RE6, "01100", True)
        self.check_expression(RE6, "0100101101", True)
        self.check_expression(RE6, "10110100", True)


        self.check_expression(RE6, "001011011101",False)
        self.check_expression(RE6, "000",False)
        self.check_expression(RE6, "111",False)
        self.check_expression(RE6, "0000", False)
        self.check_expression(RE6, "1111", False)
        self.check_expression(RE6, "0101010110101001011", False)
        self.check_expression(RE6, "101101000", False)
        self.check_expression(RE6, "10110100100", False)
        
    
    
if __name__ == '__main__':
    unittest.main()
