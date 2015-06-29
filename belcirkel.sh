#!/bin/bash
# Uses backtrace and stderr redirection to pipe the output of pocketsphinx to a python script
#
# Initialize the Raspberry Pi

# Set mixer controls
./sound_scripts/Playback_to_Speakers.sh
./sound_scripts/Record_from_DMIC.sh

( pocketsphinx_continuous -inmic yes -kws keyphrase.list -backtrace yes 3>&1 1>&2- 2>&3- ) | python processkws.py