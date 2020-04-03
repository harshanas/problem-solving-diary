#  https://dev.to/thepracticaldev/daily-challenge-217-sms-w-an-old-phone-4g4d
import unittest


def sendMessage(user_str):
    key_clicks = ""
    is_toggle_clicked = False
    user_str = list(user_str)
    key_map = {
        "1":{"key": "1","clicks": 1, "holds": 1},
        ".":{"key": "1","clicks": 1, "holds": 0},
        ",":{"key": "1","clicks": 2, "holds": 0},
        "?":{"key": "1","clicks": 3, "holds": 0},
        "!":{"key": "1","clicks": 4, "holds": 0},

        "2":{"key": "2","clicks": 1, "holds": 1},
        "a":{"key": "2","clicks": 1, "holds": 0},
        "b":{"key": "2","clicks": 2, "holds": 0},
        "c":{"key": "2","clicks": 3, "holds": 0},
        
        "3":{"key": "3","clicks": 1, "holds": 1},
        "d":{"key": "3","clicks": 1, "holds": 0},
        "e":{"key": "3","clicks": 2, "holds": 0},
        "f":{"key": "3","clicks": 3, "holds": 0},

        "4":{"key": "4","clicks": 1, "holds": 1},
        "g":{"key": "4","clicks": 1, "holds": 0},
        "h":{"key": "4","clicks": 2, "holds": 0},
        "i":{"key": "4","clicks": 3, "holds": 0},

        "5":{"key": "5","clicks": 1, "holds": 1},
        "j":{"key": "5","clicks": 1, "holds": 0},
        "k":{"key": "5","clicks": 2, "holds": 0},
        "l":{"key": "5","clicks": 3, "holds": 0},

        "6":{"key": "6","clicks": 1, "holds": 1},
        "m":{"key": "6","clicks": 1, "holds": 0},
        "n":{"key": "6","clicks": 2, "holds": 0},
        "o":{"key": "6","clicks": 3, "holds": 0},

        "7":{"key": "7","clicks": 1, "holds": 1},
        "p":{"key": "7","clicks": 1, "holds": 0},
        "q":{"key": "7","clicks": 2, "holds": 0},
        "r":{"key": "7","clicks": 3, "holds": 0},
        "s":{"key": "7","clicks": 4, "holds": 0},

        "8":{"key": "8","clicks": 1, "holds": 1},
        "t":{"key": "8","clicks": 1, "holds": 0},
        "u":{"key": "8","clicks": 2, "holds": 0},
        "v":{"key": "8","clicks": 3, "holds": 0},

        "9":{"key": "9","clicks": 1, "holds": 1},
        "w":{"key": "9","clicks": 1, "holds": 0},
        "x":{"key": "9","clicks": 2, "holds": 0},
        "y":{"key": "9","clicks": 3, "holds": 0},
        "z":{"key": "9","clicks": 4, "holds": 0},

        "*":{"key": "*","clicks": 1, "holds": 1},
        "'":{"key": "*","clicks": 1, "holds": 0},
        "-":{"key": "*","clicks": 2, "holds": 0},
        "+":{"key": "*","clicks": 3, "holds": 0},
        "=":{"key": "*","clicks": 4, "holds": 0},

        " ":{"key": "0","clicks": 1, "holds": 0},
        
    }

    for index, character in enumerate(user_str):

        if character.isupper() and not is_toggle_clicked:
            is_toggle_clicked = True
            key_clicks += "#"
            character = character.lower()
        elif is_toggle_clicked:
            is_toggle_clicked = False
            key_clicks += "#"

        if index != 0 and key_map[user_str[index-1].lower()]['key'] == key_map[character]['key'] and key_clicks[-1] != "#" and key_clicks[-1] != "-":
            key_clicks += " "

        key_clicks += (key_map[character]['key'] *key_map[character]['clicks']) + ("-" * key_map[character]['holds'])
        
    
    return key_clicks

#  Unit Tests

class TestSendMessage(unittest.TestCase):

    def test_DefCon1(self):
        self.assertEqual(sendMessage("Def Con 1!"), "#3#33 3330#222#666 6601-1111")
    
    def test_hey(self):
        self.assertEqual(sendMessage("hey"), "4433999")
    
    def test_onetwothree(self):
        self.assertEqual(sendMessage("one two three"), "666 6633089666084477733 33")

    def test_helloworld(self):
        self.assertEqual(sendMessage("Hello World!"), "#44#33555 5556660#9#66677755531111")

if __name__ == "__main__":
    unittest.main()

