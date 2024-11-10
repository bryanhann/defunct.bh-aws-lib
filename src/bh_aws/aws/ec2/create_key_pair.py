#!/usr/bin/env python3

from bh_aws import Root

class CREATE_KEY_PAIR(Root):
    def the_material(self):
        return self['KeyMaterial']

ROOT=CREATE_KEY_PAIR
