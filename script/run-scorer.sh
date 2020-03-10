#!/bin/sh

. $HOME/srcomp-venv/bin/activate

firefox localhost:3000 &

FIREFOX_PID=$!
echo $FIREFOX_PID

kill_tasks() {
  if $(kill -s 0 $FIREFOX_PID 2> /dev/null)
  then
    echo "Killing $FIREFOX_PID"
    kill $FIREFOX_PID
  fi
}

trap kill_tasks EXIT

python -m sr.comp.scorer --local $HOME/compstate
