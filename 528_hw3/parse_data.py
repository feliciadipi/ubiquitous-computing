import csv

def txt_to_csv(src_path, dest_path):
    with open(dest_path, "w") as dest:
        writer = csv.writer(dest)
        writer.writerow(["xacc", "yacc", "zacc", "xgyro", "ygyro", "zgyro"])
        with open(src_path, "r") as src:
            lines = src.readlines()
            lines = map(lambda l: l.split(": ")[1].split(","), lines)
            for line in lines:
                writer.writerow(line)

for i in range(20):
    s = str(i).zfill(2)
    txt_to_csv(f"./data/up_{s}.txt", f"./data/up_{s}.csv")
    txt_to_csv(f"./data/down_{s}.txt", f"./data/down_{s}.csv")
    txt_to_csv(f"./data/left_{s}.txt", f"./data/left_{s}.csv")
    txt_to_csv(f"./data/right_{s}.txt", f"./data/right_{s}.csv")