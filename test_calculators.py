import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).parent


class CalculatorTests(unittest.TestCase):
    def run_script(self, script, answers):
        result = subprocess.run(
            [sys.executable, str(ROOT / script)], input=answers,
            text=True, capture_output=True, timeout=5,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_adds_numbers_instead_of_strings(self):
        self.assertTrue(self.run_script('number-adder.py', '2\n3\n').endswith('5.0\n'))
        self.assertTrue(self.run_script('number-adder.py', '-2.5\n3\n').endswith('0.5\n'))

    def test_divides_operands(self):
        output = self.run_script('day2-assignment.py', '8\n/\n2\n4\n15\n')
        self.assertIn('4.0\n', output)
        self.assertNotIn('10.0\n', output)

    def test_zero_divisor_does_not_crash(self):
        output = self.run_script('day2-assignment.py', '8\n/\n0\n4\n15\n')
        self.assertIn('Cannot divide by zero', output)


if __name__ == '__main__':
    unittest.main()
