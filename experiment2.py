naive = "aaabacadaeafagahaiajakalamanaoapaqarasatauavawaxayazbabbbcbdbebfbgbhbibjbkblbmbnbobpbqbrbsbtbubvbwbxbybzcacbcccdcecfcgchcicjckclcmcncocpcqcrcsctcucvcwcxcyczdadbdcdddedfdgdhdidjdkdldmdndodpdqdrdsdtdudvdwdxdydzeaebecedeeefegeheiejekelemeneoepeqereseteuevewexeyezfafbfcfdfefffgfhfifjfkflfmfnfofpfqfrfsftfufvfwfxfyfzgagbgcgdgegfggghgigjgkglgmgngogpgqgrgsgtgugvgwgxgygzhahbhchdhehfhghhhihjhkhlhmhnhohphqhrhshthuhvhwhxhyhziaibicidieifigihiiijikiliminioipiqirisitiuiviwixiyizjajbjcjdjejfjgjhjijjjkjljmjnjojpjqjrjsjtjujvjwjxjyjzkakbkckdkekfkgkhkikjkkklkmknkokpkqkrksktkukvkwkxkykzlalblcldlelflglhliljlklllmlnlolplqlrlsltlulvlwlxlylzmambmcmdmemfmgmhmimjmkmlmmmnmompmqmrmsmtmumvmwmxmymznanbncndnenfngnhninjnknlnmnnnonpnqnrnsntnunvnwnxnynzoaobocodoeofogohoiojokolomonooopoqorosotouovowoxoyozpapbpcpdpepfpgphpipjpkplpmpnpopppqprpsptpupvpwpxpypzqaqbqcqdqeqfqgqhqiqjqkqlqmqnqoqpqqqrqsqtquqvqwqxqyqzrarbrcrdrerfrgrhrirjrkrlrmrnrorprqrrrsrtrurvrwrxryrzsasbscsdsesfsgshsisjskslsmsnsospsqsrssstsusvswsxsysztatbtctdtetftgthtitjtktltmtntotptqtrtstttutvtwtxtytzuaubucudueufuguhuiujukulumunuoupuqurusutuuuvuwuxuyuzvavbvcvdvevfvgvhvivjvkvlvmvnvovpvqvrvsvtvuvvvwvxvyvzwawbwcwdwewfwgwhwiwjwkwlwmwnwowpwqwrwswtwuwvwwwxwywzxaxbxcxdxexfxgxhxixjxkxlxmxnxoxpxqxrxsxtxuxvxwxxxyxzyaybycydyeyfygyhyiyjykylymynyoypyqyrysytyuyvywyxyyyzzazbzczdzezfzgzhzizjzkzlzmznzozpzqzrzsztzuzvzwzxzyzz"

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

for i, v in enumerate(possible_combinations):
    naive = naive.replace(v * 3, v * 2)

for i, v in enumerate(possible_combinations):
    naive = naive.replace(v * 3, v * 2)

for i, v in enumerate(possible_combinations):
    naive = naive.replace(v * 3, v * 2)

print(naive)
print(len(naive))
