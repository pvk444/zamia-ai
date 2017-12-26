#!/usr/bin/env python
# -*- coding: utf-8 -*- 

DEPENDS     = [ 'data' ]

PL_SOURCES  = [
               'config'
              ]

def get_data(kernal):

    #
    # name / self address utils
    #
    
    # macro(en, my_forename, W) :- forename (self, en, W).
    # macro(de, my_forename, W) :- forename (self, de, W).
   
    for soln in kernal.prolog.query("forename(self, L, W)"):
        kernal.add_macro(soln['L'], 'my_forename', soln)
 
    # macro(en, self_address, L) :- forename (self, en, L), str_append(L, ', ').
    # macro(en, self_address, L) :- L is "".
    # macro(de, self_address, L) :- forename (self, de, L), str_append(L, ', ').
    # macro(de, self_address, L) :- L is "".
    
    for soln in kernal.prolog.query("forename(self, L, W)"):
        kernal.add_macro(soln['L'], 'self_address', {'W': soln['W'] + ', '})
    kernal.add_macro('en', 'self_address', {'W': ''})
    kernal.add_macro('de', 'self_address', {'W': ''})


