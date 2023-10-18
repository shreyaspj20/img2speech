from img2speech import image_to_sound
import string
import os
import pickle
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def compare_punctuation(true_label, predicted_label):
    punctuation = set(string.punctuation)
    true_count = 0
    predicted_count = 0

    for char in true_label:
        if char in punctuation:
            true_count += 1

    for char in predicted_label:
        if char in punctuation:
            predicted_count += 1

    diff = abs(true_count - predicted_count)
    return diff / len(true_label)


def wer(s1, s2):
    s1 = s1.split()
    s2 = s2.split()
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return float(dp[n][m]) / len(s1)


def cer(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return float(dp[n][m]) / len(s1)


def levenshtein_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[m][n]


b1 = "When people ask what I see in you, I just smile and look away because I'm afraid if they knew, they'd fall " \
     "in love with you too "
b2 = "The quick brown fox jumped over the 5 lazy dogs!"
b3 = "Creating an OCR Communication App with Tesseract.js and React (Part 1)"
b4 = "Long-Term Care Insurance"
b5 = "How to print a line break in Python"
b6 = "3. Write a program that prompts the user for two sentences and prints the combined words from both in " \
     "alphabetical order. You can ignore the case. "
b7 = "Therefore, Jakob has studied every night for a week. Therefore, he should get a good grade on the test."
b8 = "5 Milton would insert into the printed text of his poem his own anticipation that his epic would receive " \
     "the same universal approbation as Homer's and Virgil's."
b9 = "Word processing: This is the process of manipulating text, characters, words, and sentences in such a " \
     "manners as to make the final document free of errors and attractive to look at. "
b10 = "It doesn't matter what others are doing, it matters what you are doing."
b11 = "If the path be beautiful, let us not ask where it leads. - Anatole France"
b12 = "Everyone has three lives: a public life, a private life, and a secret life."
b13 = "The future belongs to those who believe in the beauty of their dreams. ELEANOR ROOSEVELT"
b14 = "Distance doesn't matter when two souls are united."
b15 = "EVERYONE WILL TEXT YOU, ONLY WHEN THEY NEED YOU."
b16 = "Quotes For Instagram Notes In English, Check Out Instagram Notes Quotes And Ideas"
b17 = "FAILURE is not the opposite of success it's PART OF SUCCESS"
b18 = " \"My mother was my role model before I even knew what the word was.\" - LISA LESLIE TOWN&COUNTRY"
b19 = "A poem is the very image of life expressed in its eternal truth. - Percy Bysshe Shelley"
b20 = "I never know you could matter so much to me, even with miles distance in between us."
b21 = "Small and Simple Thoughts in one line"
b22 = "The greatest glory in living lies not in never falling, but in rising every time we fall.  NELSON MANDELA"
b23 = "Distance doesn't matter when two souls are united."
b24 = " \" Perseverance is not a long race; it is many short races one after the other. Walter Elliot"
b25 = "If you set your goals ridiculously high and it's a failure, you will fail above everyone one else's " \
      "success. JAMES CAMERON "
b26 = "You will face many defeats in life, but never let yourself be defeated.  MAYA ANGELOU"
b27 = "Thank you for always being my rainbow after the storm"
b28 = "Change is the end result of all true learning. Leo Buscaglia"
b29 = "\"No matter how old she may be, sometimes a girl just needs her mom.\""
b30 = "\"The beginning is always today.\" - MARK SHELLEY"


var_list = []
var_list.extend(
    [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25,
     b26, b27, b28, b29, b30])

similarity_yes = []
similarity_no = []
wer_yes = []
wer_no = []
cer_yes = []
cer_no = []
leven_yes = []
leven_no = []

dir_path = "E:\my gitprojects\img2speech\Test_images"
files = os.listdir(dir_path)
files = sorted(files, key=lambda x: int(x.split('_')[0]))
ctr = 0

for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        print("Processing image {}".format(ctr + 1))
        image_path = os.path.join(dir_path, file)
        t1, s1 = image_to_sound(image_path, "ENGLISH", "NO")
        t2, s2 = image_to_sound(image_path, "ENGLISH", "YES")
        similarity_yes.append(similar(t2, var_list[ctr]))
        similarity_no.append(similar(t1, var_list[ctr]))
        wer_yes.append(wer(t2, var_list[ctr]))
        wer_no.append(wer(t1, var_list[ctr]))
        cer_yes.append(cer(t2, var_list[ctr]))
        cer_no.append(cer(t1, var_list[ctr]))
        leven_yes.append(levenshtein_distance(t2, var_list[ctr]))
        leven_no.append(levenshtein_distance(t1, var_list[ctr]))
        print("similarity_yes = {}".format(similar(t2, var_list[ctr])))
        print("similarity_no = {}".format(similar(t1, var_list[ctr])))
        print("wer_yes = {}".format(wer(t2, var_list[ctr])))
        print("wer_no = {}".format(wer(t1, var_list[ctr])))
        print("cer_yes = {}".format(cer(t2, var_list[ctr])))
        print("cer_no = {}".format(cer(t1, var_list[ctr])))
        print("leven_yes = {}".format(levenshtein_distance(t2, var_list[ctr])))
        print("leven_no = {}".format(levenshtein_distance(t1, var_list[ctr])))
        ctr = ctr + 1

print("SIMILARITY")
res1 = "\n".join("{} {}".format(x, y) for x, y in zip(similarity_yes, similarity_no))
print(res1)
print("WER")
res2 = "\n".join("{} {}".format(x, y) for x, y in zip(wer_yes, wer_no))
print(res2)
print("CER")
res3 = "\n".join("{} {}".format(x, y) for x, y in zip(cer_yes, cer_no))
print(res3)
print("LEVENSTEIN")
res4 = "\n".join("{} {}".format(x, y) for x, y in zip(leven_yes, leven_no))
print(res4)


with open("similarity_yes_list.pkl", "wb") as f:
    pickle.dump(similarity_yes, f)
with open("similarity_no_list.pkl", "wb") as f:
    pickle.dump(similarity_no, f)
with open("wer_yes_list.pkl", "wb") as f:
    pickle.dump(wer_yes, f)
with open("wer_no_list.pkl", "wb") as f:
    pickle.dump(wer_no, f)
with open("cer_yes_list.pkl", "wb") as f:
    pickle.dump(cer_yes, f)
with open("cer_no_list.pkl", "wb") as f:
    pickle.dump(cer_no, f)
with open("leven_yes_list.pkl", "wb") as f:
    pickle.dump(leven_yes, f)
with open("leven_no_list.pkl", "wb") as f:
    pickle.dump(leven_no, f)

