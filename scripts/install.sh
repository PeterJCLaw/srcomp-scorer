#!/bin/sh

python3 -m venv $HOME/srcomp-venv

. $HOME/srcomp-venv/bin/activate

MY_DIR=$(dirname $0)

pip install -r $MY_DIR/requirements.txt
pip install -e $MY_DIR/..

cp $MY_DIR/run-scorer.sh $HOME

echo "SRComp Scorer installed."
echo
echo "You will need to clone the compstate to ~/compstate."
echo
echo "Run the scorer via '~/run-scorer.sh'."
echo "That will launch the scorer and open the UI in Firefox."
echo
echo "You may also need to configure ssh access to the scorer machine"
echo "and install a suitable public key."
