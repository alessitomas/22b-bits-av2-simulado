#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""


from myhdl import *
from ula_aux import *


def exe1(a, b, c, q):
    @always_comb
    def comb():
        q.next = 0

    return instances()


def exe2(p, q, r, s):
    @always_comb
    def comb():
        s.next = 0

    return instances()


def exe3(x1, x0, y1, y0, z3, z2, z1, z0):
    @always_comb
    def comb():
        z0.next = 0
        z1.next = 0
        z2.next = 0
        z3.next = 0

    return instances()


def exe4_ula(a, b, inverte_a, inverte_b, c_in, c_out, selecao, zero, resultado):
    aneg = Signal(modbv(0)[32:])
    bneg = Signal(modbv(0)[32:])
    adderout = Signal(modbv(0)[32:])
    muxa_out= Signal(modbv(0)[32:])             
    muxb_out = Signal(modbv(0)[32:]) 
    orout, andout,slt, muxbigout = [Signal(modbv(0)[32:]) for i in range(4)]
    muxa = mux2way(muxa_out, a, aneg,inverte_a)
    muxb = mux2way(muxb_out, b, bneg,inverte_b)
    adder1 = adder(adderout,c_out,muxa_out,muxb_out,c_in)
    
    
    muxbig = mux4way(muxbigout,andout,orout,adderout,slt,selecao)

    

    
    



    @always_comb
    def comb():
        andout.next = muxa_out & muxb_out
        orout.next = muxa_out | muxb_out
        aneg.next = not a
        bneg.next = not b
        if muxbigout == 0:
            zero.next = 1
        else:
            zero.next = 0
        resultado.next = muxbigout



    
    return instances()
