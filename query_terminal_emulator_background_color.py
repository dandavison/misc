#!/usr/bin/env python
import subprocess
import sys

# https://iterm2.com/documentation-escape-codes.html
cmd = "read -s -N 26 -p $'\x1b]4;-2;?\x07' RESPONSE; echo \"$RESPONSE\""

response = subprocess.check_output(["bash", "-c", cmd]).strip().decode('utf-8')
r, g, b = map(lambda hex: int(hex[:2], 16), response.split(":")[1].split('/'))
lightness = sum([r, g, b]) / (3 * 0xFF)
sys.stdout.write("light\n" if lightness > 0.5 else "dark\n")
