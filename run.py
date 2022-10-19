from re import I
import shutil
import json

file_names  = []
count = 0
for i  in range(607366912,(607366912+1001)):
    # 2nd option
    item = {}
    item["index"] = count
    item["name"] = f"01136120198500_MN_0{i}_F.tif"
    shutil.copy("01136120198500_MN_0607366912_F.tif", f"duplicates/01136120198500_MN_0{i}_F.tif")
    count = count + 1
    print(count)
    file_names.append(item)
with open('file_names.json', 'w', encoding='utf-8') as f:
    json.dump(file_names, f, ensure_ascii=False, indent=4)