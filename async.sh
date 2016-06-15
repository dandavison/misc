on_success() {
  local task="$1"
  local poll="$2"
  local callback="$3"
  local poll_frequency="${4:-1}"

  task &
  until poll; do sleep $poll_frequency; done
  callback
}

FLAG=/tmp/flag

task() {
  echo "Task start"
  sleep 4
  echo "Task done"
  touch $FLAG
}

poll() {
  echo "Poll"
  [ -e $FLAG ]
}

callback() {
  echo "In callback"
}

rm -f $FLAG
on_success task poll callback
