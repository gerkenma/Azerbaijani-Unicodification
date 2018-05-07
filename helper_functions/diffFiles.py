import difflib

# Was used to find the differences between two output files
# Had a subsequent test that scored worse. Wanted to
#   identify what mistakes the newer implementation was making
with open('dictionaries/prediction.csv', encoding="utf-8") as text1:
    with open('90-prediction.csv', encoding="utf-8") as text2:
        d = difflib.Differ()
        diff = list(d.compare(text1.readlines(), text2.readlines()))
        with open('diff.txt', 'w', encoding="utf-8") as diff_file:
            _diff = ''.join(diff)
            diff_file.write(_diff)
