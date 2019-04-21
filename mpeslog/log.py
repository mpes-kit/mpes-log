#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: R. Patrick Xian
"""

from __future__ import print_function, division
import numpy as np
import h5py as h5
import silx.io as silo
from collections import OrderedDict as odict


def dict_merge(D, others, rettype='ordered'):
    """
    Merge a (ordered) dictionary with other dictionaries

    :Parameters:
        D : dict
            Main dictionary.
        others : list/tuple/dict
            Other dictionary or composite dictionarized elements.
        rettype : str | 'ordered'
            Type of dictionary to return ('ordered' or 'unordered').

    :Return:
        D : dict
            Merged dictionary.
    """

    if type(others) in (list, tuple): # Merge D with a list or tuple of dictionaries
        for oth in others:

            if rettype == 'ordered':
                D = odict({**D, **oth})
            elif rettype == 'unordered':
                D = {**D, **oth}

    elif type(others) in (dict, odict): # Merge D with a single dictionary

        if rettype == 'ordered':
            D = odict({**D, **others})
        elif rettype == 'unordered':
            D = {**D, **others}

    return D


def dict_upscale(names, dicts, init=odict({})):
    """ Scale up dictionary.
    """

    metadict = init
    for name, pd in zip(names, dicts):
        metadict[name] = pd

    return metadict
