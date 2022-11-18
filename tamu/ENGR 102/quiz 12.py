import numpy as np

with open("mod12activity.txt", "r") as keyText:
    plainText = keyText.readlines()
for i, v in enumerate(plainText):
    plainText[i] = v.strip()
keyArray = [plainText[i:i + 5] for i in range(0, len(plainText), 5)]

keyDict = {
    "B": 0,
    "I": 1,
    "N": 2,
    "G": 3,
    "O": 4
}

encrypted = "B2I4G4O4B3I5N2I4N5N2N3B1N4B2I1B3"
encrypted = "G2N2I4B5N2G1N5N5N3O5B5N3O1I5G5O5"
encryptedArray = [encrypted[i:i + 2] for i in range(0, len(encrypted), 2)]

decrypted = []
for i in encryptedArray:
    decrypted.append(keyArray[int(i[1]) - 1][keyDict[i[0]]])
decrypted = "".join(decrypted)

print(decrypted)
