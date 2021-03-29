import sys
from io import BytesIO
from unittest.mock import patch

with patch.object(sys, "stdin", BytesIO()):
    sys.stdout.write("\x1b[6n")
    print(sys.stdin.getvalue())
