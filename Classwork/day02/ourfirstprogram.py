# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:03:14 2014

@author: sophie
"""

print "Hello world!"

import unum
from unum import Unum
from unum.units import *
unit = Unum.unit

ft = Unum.unit('foot',M/3.28084)
lbf= Unum.unit('lbf',4.4482216*N)

torque = 181 * ft * lbf

print torque.asUnit(N*M)

units1 = (1*W*V*F*ohm*S)/(1*C*Hz*J)

print units1