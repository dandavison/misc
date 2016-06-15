# How to pass fn _f to fn _g so that _g can call _f
_g() {
  local fn="$1"
  echo "In g, calling fn:"
  $fn
}

_f() {
  echo "In f"
}

_g _f
