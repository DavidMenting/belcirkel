#!/bin/sh
pocketsphinx_continuous \
  -inmic yes \
  -kws keyphrase.list \
  #-hmm ./models/nl-nl \
  #-dict ./models/cmudict-nl-nl.dict
  -backtrace yes