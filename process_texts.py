import json
import os

base_path = os.path.dirname(os.path.abspath(__file__))

for file_name in [
    "Texts/Latest APK/i18n_brazilianportuguese.json",
    "Texts/Latest APK/i18n_chinesetraditional.json",
    "Texts/Latest APK/i18n_english.json",
    "Texts/Latest APK/i18n_french.json",
    "Texts/Latest APK/i18n_german.json",
    "Texts/Latest APK/i18n_italian.json",
    "Texts/Latest APK/i18n_japanese.json",
    "Texts/Latest APK/i18n_korean.json",
    "Texts/Latest APK/i18n_spanish.json",
    "Texts/Latest Remote/English.txt",
    "Texts/Latest Remote/German.txt",
    "Texts/Latest Remote/Spanish.txt",
    "Texts/Niantic Social/brazilianportuguese.json",
    "Texts/Niantic Social/chinesetraditional.json",
    "Texts/Niantic Social/english.json",
    "Texts/Niantic Social/french.json",
    "Texts/Niantic Social/german.json",
    "Texts/Niantic Social/italian.json",
    "Texts/Niantic Social/japanese.json",
    "Texts/Niantic Social/korean.json",
    "Texts/Niantic Social/spanish.json",
]:
    file = os.path.join(base_path, file_name)
    processed_file = (
        os.path.splitext(os.path.join(base_path, "Processed", file_name))[0] + ".json"
    )
    with open(file, "r") as f:
        try:
            data = json.load(f).get("data")
        except:
            continue
    data_dict = dict()
    for i in range(0, len(data), 2):
        data_dict[data[i]] = data[i + 1]
    with open(processed_file, "w") as f:
        json.dump(data_dict, f, ensure_ascii=False, indent=2)
