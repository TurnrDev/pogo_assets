import json
import os

base_path = os.path.dirname(os.path.abspath(__file__))

for file_name in [
    "Texts/Niantic Social/brazilianportuguese.json",
    "Texts/Niantic Social/chinesetraditional.json",
    "Texts/Niantic Social/english.json",
    "Texts/Niantic Social/french.json",
    "Texts/Niantic Social/german.json",
    "Texts/Niantic Social/italian.json",
    "Texts/Niantic Social/japanese.json",
    "Texts/Niantic Social/korean.json",
    "Texts/Niantic Social/spanish.json",
    "Texts/Niantic Social/thai.json",
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


for file_name in [
    "Texts/Latest APK/BrazilianPortuguese.txt",
    "Texts/Latest APK/ChineseTraditional.txt",
    "Texts/Latest APK/English.txt",
    "Texts/Latest APK/French.txt",
    "Texts/Latest APK/German.txt",
    "Texts/Latest APK/Italian.txt",
    "Texts/Latest APK/Japanese.txt",
    "Texts/Latest APK/Korean.txt",
    "Texts/Latest APK/Russian.txt",
    "Texts/Latest APK/Spanish.txt",
    "Texts/Latest APK/Thai.txt",
    "Texts/Latest Remote/BrazilianPortuguese.txt",
    "Texts/Latest Remote/ChineseTraditional.txt",
    "Texts/Latest Remote/English.txt",
    "Texts/Latest Remote/French.txt",
    "Texts/Latest Remote/German.txt",
    "Texts/Latest Remote/Italian.txt",
    "Texts/Latest Remote/Japanese.txt",
    "Texts/Latest Remote/Korean.txt",
    "Texts/Latest Remote/Spanish.txt",
    "Texts/Latest Remote/Thai.txt",
]:
    file = os.path.join(base_path, file_name)
    processed_file = (
        os.path.splitext(os.path.join(base_path, "Processed", file_name))[0] + ".json"
    )
    with open(file, "r") as f:
        data = f.read()
    data_dict = dict()
    for translation in data.split("RESOURCE ID: "):
        if translation:
            try:
                resource_id, text = translation.split("\nTEXT: ")
            except ValueError as e:
                print(e, translation)
                continue
            try:
                resource_id = resource_id.strip()
            except ValueError as e:
                print(e, resource_id)
                continue
            if text.endswith("\n\n"):
                text = text[:-2]
            data_dict[resource_id] = text
    with open(processed_file, "w") as f:
        json.dump(data_dict, f, ensure_ascii=False, indent=2)
