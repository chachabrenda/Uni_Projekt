#intergratiostest
import subprocess
import unittest

class IntegrationTest(unittest.TestCase):
    def test_stdin(self):
        input_data = b'Hello, World!\n'
        expected_output = b'SGVsbG8sIFdvcmxkIQ==\n'
        
        process = subprocess.Popen(['./bb64'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, _ = process.communicate(input=input_data)
        
        self.assertEqual(output.strip(), expected_output)

    def test_file_input(self):
        input_file = 'input.txt'
        expected_output = b'SGVsbG8sIFdvcmxkIQ==\n'
        
        with open(input_file, 'w') as file:
            file.write('Hello, World!\n')

        process = subprocess.Popen(['./bb64', input_file], stdout=subprocess.PIPE)
        output, _ = process.communicate()

        self.assertEqual(output.strip(), expected_output)

        # Aufräumen
        subprocess.run(['rm', input_file])

    def test_line_breaks(self):
        input_data = b'This is a long text that should be broken into multiple lines in the output.\n'
        expected_output = b'VGhpcyBpcyBhIGxvbmcgdGV4dCB0aGF0IHNob3VsZCBiZSBicm9rZW4gaW50byBtdWx0aXBsZSBsaW5lcyBpbiB0aGUgb3V0cHV0Lg==\nVGhpcyBpcyBhIGxvbmcgdGV4dCB0aGF0IHNob3VsZCBiZSBicm9rZW4gaW50byBtdWx0aXBsZSBsaW5lcyBpbiB0aGUgb3V0cHV0Lg==\n'
        
        process = subprocess.Popen(['./bb64'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, _ = process.communicate(input=input_data)
        
        self.assertEqual(output, expected_output)

if __name__ == '_main_':
    unittest.main()
