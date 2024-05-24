import csv

def generate_csv(prefix):
    with open(f"./{prefix}.txt", "r") as src:
        lines = src.readlines()
        rows = [l.rstrip("\n").split(",") for l in lines]
        for i in range(20):
            with open(f"./{prefix}_{str(i).zfill(2)}.csv", "w") as dest:
                writer = csv.writer(dest)
                writer.writerow(["xacc", "yacc", "zacc", "xgyro", "ygyro", "zgyro"])
                for j in range(400):
                    writer.writerow(rows[400*i+j])

# generate_csv('up')
generate_csv('down')
generate_csv('left')
generate_csv('right')