import yara
import sys
import os

def load_rules(rule_file):
    rules = yara.compile(filepath=rule_file)
    return rules


def scan_file(rules, filepath):
    matches =rules.match(filepath)
    if matches:
        print(f"\n matches found in {filepath}\n")
        for match in matches:
            print(f"Rule:{match.rule}")
            print(f"Description:{match.meta.get('description')}")
            print(f"Severity:{match.meta.get('severity','N/A')}")
            print(f"Matched Strings:")
            for string in match.strings:
                print(f"identifier: {string.identifier}")
                print(f"Matched: {string.instances[0].matched_data.decode()}")

    else:
        print(f"\n NO matches found")

def main():
    if len(sys.argv) != 3:
        print("Usage : python yarascanner.py [rules.yar] [Files to scan]")
        sys.exit(1)
    
    rule_file = sys.argv[1]
    target_file = sys.argv[2]

    print(f"loading rules form {rule_file}")
    rules = load_rules(rule_file)

    print(f"Scanning {target_file}...")
    scan_file(rules,target_file)

if __name__ == "__main__":
    main()
