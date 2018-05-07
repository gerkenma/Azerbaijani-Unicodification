from unidecode import unidecode
import codecs

# Creates tab delimited pairs of Azerbaijani text
# Output file has regular word followed by decorated word on a single line
# Used for Keras implementation

with open("azj-train.txt", "r", encoding="UTF-8") as train:
    output = {}
    for line in train:
        line = line.strip()
        output[unidecode(line).replace("@", "e")] = line

azj = codecs.open("azj-pairs.txt", "wb", encoding="UTF-8")
for key in output:
    azj.write(key + "\t" + output[key] + "\n")