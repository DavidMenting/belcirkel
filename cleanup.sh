#!/bin/bash
#
# checks to see if any raw audio files and logfiles are still present
# if so, zips them in a timestamped archive and removes the files
if [ -e ./logdir/pocketsphinx.log ]; then
  tar -zcvf log-`date +%F`.tar.gz ./logdir/*
  rm -f logdir/*
fi