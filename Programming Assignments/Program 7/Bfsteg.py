import subprocess
import argparse
import string

# You can do a default-style run for this by just having the classic "python Bfsteg" followed by -B or -b for byte and bit, respectively

def is_likely_text(data):
    try:
        text = data.decode('utf-8')
        # Allow some non-printable characters like \n, \t, etc.
        printable_ratio = sum(c in string.printable for c in text) / len(text)
        return printable_ratio > 0.9
    except UnicodeDecodeError:
        return False

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-w", required=True)
parser.add_argument("-b", action="store_true")
parser.add_argument("-B", action="store_true")
parser.add_argument("--interval-start", type=int, default=1)   #literally just change these to change the interval range
parser.add_argument("--interval-end", type=int, default=10)     #  <=== This end value is exclusive, not inclusive
args = parser.parse_args()

# Validate method
if args.b and args.B:
    print("Error: Choose only one method: -b or -B")
    exit(1)
elif not args.b and not args.B:
    print("Error: You must choose a method: -b or -B")
    exit(1)

method_flag = "-b" if args.b else "-B"
offsets = [2 ** i for i in range(11)]  #  <====== change the range value to alter offset, it alters the power of 2 it goes to, its exclusive

# Brute-force through all combinations
for offset in offsets:
    for interval in range(args.interval_start, args.interval_end):
        print(f"\nTrying offset={offset}, interval={interval} using {'bit' if args.b else 'byte'}-level method...")

        result = subprocess.run(
            [
                "python", "Steg.py",
                "-r",
                method_flag,
                f"-o{offset}",
                f"-i{interval}",
                f"-w{args.w}"
            ],
            capture_output=True,
            text=True
        )

        extracted = result.stdout.strip()
        if extracted:
            print(f"Output:\n{extracted}")
            try:
                with open("extracted_output.txt", "rb") as f:
                    raw_data = f.read()
                if is_likely_text(raw_data):
                    print(f"\nSuccess! Found readable message at offset={offset}, interval={interval}")
                    print(f"\nFinal Message:\n{extracted}")
                    exit(0)
                else:
                    print("Output is not valid readable text (by filter).\n")
            except Exception as e:
                print(f"Could not read extracted_output.txt: {e}")

print("Brute-force failed to find any valid message.")
