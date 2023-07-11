import unittest
import dataprepro.tokenizer as tokenizer


class test(unittest.TestCase):

    def test_tokenize_test_case_1(self):
        """in this case we give a sentence with
        a name including _"""
        sent = "h_e_l_l_o = _good_"
        sent = tokenizer.tokenize(sent)
        self.assertEqual(sent, ["h_e_l_l_o", ' ', '=', ' ', "_good_"])

    def test_tokenize_test_case_2(self):
        """in this case we give a sentence with
        a lot of characters"""
        sent = "int* h_e_l_l_o = & _good_;"
        sent = tokenizer.tokenize(sent)
        self.assertEqual(sent, ["int", "*", ' ',"h_e_l_l_o", ' ', '=', ' ', "&", " ", "_good_", ';'])

    def test_tokenize_generalformataddspace_case_1(self):
        """testing if it gives the true form and values to
        replace or no."""

        sent = "h_e_l_l_o = _good_"
        sent = tokenizer.tokenize(sent)
        sent = tokenizer.generalformataddspace(sent)
        self.assertEqual(sent, ("SNS=SNS", ["h_e_l_l_o", "_good_"]))

    def test_tokenize_generalformataddspace_case_2(self):
        """testing if it gives the true form and values to
        replace or no."""

        sent = "int* h_e_l_l_o = & _good_;"
        sent = tokenizer.tokenize(sent)
        sent = tokenizer.generalformataddspace(sent)
        self.assertEqual(sent, ("SNS*SNS=S&SNS;S", ["int","h_e_l_l_o", "_good_"]))
