possible_combinations = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

s = "aabacadaeafagahaiajakalamanaoapaqarasatauavawaxayazbbcbdbebfbgbhbibjbkblbmbnbobpbqbrbsbtbubvbwbxbybzccdcecfcgchcicjckclcmcncocpcqcrcsctcucvcwcxcyczddedfdgdhdidjdkdldmdndodpdqdrdsdtdudvdwdxdydzeefegeheiejekelemeneoepeqereseteuevewexeyezffgfhfifjfkflfmfnfofpfqfrfsftfufvfwfxfyfzgghgigjgkglgmgngogpgqgrgsgtgugvgwgxgygzhhihjhkhlhmhnhohphqhrhshthuhvhwhxhyhziijikiliminioipiqirisitiuiviwixiyizjjkjljmjnjojpjqjrjsjtjujvjwjxjyjzkklkmknkokpkqkrksktkukvkwkxkykzllmlnlolplqlrlsltlulvlwlxlylzmmnmompmqmrmsmtmumvmwmxmymznnonpnqnrnsntnunvnwnxnynzoopoqorosotouovowoxoyozppqprpsptpupvpwpxpypzqqrqsqtquqvqwqxqyqzrrsrtrurvrwrxryrzsstsusvswsxsyszttutvtwtxtytzuuvuwuxuyuzvvwvxvyvzwwxwywzxxyxzyyzza"


def has_all_alphabet_combinations(string):
    for _, v1 in enumerate(possible_combinations):
        for _, v2 in enumerate(possible_combinations):
            target = v1 + v2
            # count the occurrences of the target
            count = string.count(target)
            if count == 0:
                return False
            if count >= 2:
                print(f"found {target} twice")
    return True


print(has_all_alphabet_combinations(s))
print(len(s))
