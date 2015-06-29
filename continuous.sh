#!/bin/bash
# Uses backtrace and stderr redirection to pipe the output of pocketsphinx to a python script

( pocketsphinx_continuous -inmic yes -kws keyphrase.list -backtrace yes 3>&1 1>&2- 2>&3- ) | python readlines.py