#!/usr/bin/env python
import subprocess
import sys

def gamma_correct(rgb: int) -> float:
    rgb = rgb / 255
    return rgb / 12.92 if rgb <= 0.03928 else ((rgb + 0.055) / 1.055) ** 2.4


def luminance(r: int, g: int, b: int) -> float:
    """
    https://www.w3.org/TR/WCAG20/#relativeluminancedef
    """
    r, g, b = map(gamma_correct, [r, g, b])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

# https://iterm2.com/documentation-escape-codes.html
cmd = "read -s -N 26 -p $'\x1b]4;-2;?\x07' RESPONSE; echo \"$RESPONSE\""

response = subprocess.check_output(["bash", "-c", cmd]).strip().decode('utf-8')
r, g, b = map(lambda hex: int(hex[:2], 16), response.split(":")[1].split('/'))

sys.stdout.write("light\n" if luminance(r, g, b) > 0.5 else "dark\n")
