#!/bin/bash
egrep -q "SigIgn:\s.{15}[13579bdf]" /proc/$$/status && echo nohuppy || echo normal
