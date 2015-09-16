# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:23:45 2015

@author: michael
"""

def ParseCube(data_file):

    MyData = open(str(data_file), 'r')
    lines = MyData.readlines()[2:]
    MyData.close()

    param = []
    mass = []
    x = []
    y = []
    z = []
    dens = []

    for line in lines:
        tokens = line.split()
        if len(tokens) == 4:
            param.append(int(tokens[0]))
        elif len(tokens) == 5:
            mass.append(int(tokens[0]))
            x.append(float(tokens[2]))
            y.append(float(tokens[3]))
            z.append(float(tokens[4]))
        elif len(tokens) == 1:
            dens.append(float(tokens[0]))
        else:
            print "WARNING: Unidentified cube file format"

    return param, mass, x, y, z, dens

def ParseXYZ(data_file):
    
    MyData = open(str(data_file), 'r')
    lines = MyData.readlines()
    MyData.close()
    
    Natoms = int(lines[0])
    
    sym = []
    x = []
    y = []
    z = []
    
    for line in lines:
        tokens = line.split()
        if len(tokens) != 4:
            continue
        else:
            sym.append(tokens[0])
            x.append(float(tokens[1]))
            y.append(float(tokens[2]))
            z.append(float(tokens[3]))
            
    if len(sym) != Natoms:
        print "WARNING: Unidentified XYZ file format"
    
    return Natoms, sym, x, y, z    