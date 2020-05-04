import sys

for line in sys.stdin:
    codepoint, _, _, rest = line.strip().split("@")
    *rest, utf8 = rest
    rest = ''.join(rest).rstrip().replace(' ', '_')
    print(f"pub const {rest}: char = '{utf8}'; // {codepoint}")
