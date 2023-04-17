import argparse

parser = argparse.ArgumentParser()
parser.add_argument('first', help="First File")
parser.add_argument('second', help="Second File")
args = parser.parse_args()

first_file = args.first
second_file = args.second 

with open(first_file) as file1:
    with open(second_file) as file2:
        difference = set(file1).difference(file2)

difference.discard("\n")

with open('first-diff', 'w') as file_out:
    for line in difference:
        file_out.write(line)
print("[+] IN First File NOT IN Second File \n")
dosya = open("first-diff", "r", encoding="utf-8")
read = dosya.read()
print(read)

with open(first_file) as file1:
    with open(second_file) as file2:
        difference1 = set(file2).difference(file1)

difference1.discard("\n")

with open('second-diff', 'w') as file_out:
    for line in difference1:
        file_out.write(line)

print("[+] IN Second File NOT IN First File \n")
dosya = open("second-diff", "r", encoding="utf-8")
read = dosya.read()
print(read)

