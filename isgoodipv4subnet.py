#!/usr/bin/env python
#coding=utf-8
#***************************************#
#       ScriptName: martinvpc.py        #
#       ------Author:Matrin-----        #
#       -------version:2.0------        #
#***************************************#

def isgoodsubnet(subnet):
    i = subnet.split('/')
    if len(i) != 2:
        return False
    i0 = i[0].split('.')
    if len(i0) != 4:
        return False
    i1 = i[1].split('.')
    if len(i1) != 1:
        return False
    else:
        print i1
        i1 = i1[0]
        print i1
    print i
    print i0
    print i1
    if not i1.isdigit():
        return False
    i1 = int(i1)
    if i1 > 32 or i1 < 20:
        return False
    i00 = i0[0]
    i01 = i0[1]
    i02 = i0[2]
    i03 = i0[3]
    print i00
    print i01
    print i02
    print i03
    if not i00.isdigit():
        print "00000000000000000000000000000000000"
        return False
    i00 = int(i00)
    if i00 not in [10,172,192]:
        print 111111111111111111111111111111111111111111
        return False
    if not i01.isdigit():
        return False
    i01 = int(i01)
    if i01 < 0 or i01 > 255:
        print 222222222222222222222222222222222222222
        return False
    if i00 == 172:
        if i01 < 16 or i01 > 32:
            print 222222222222222222222222222222222222222
            return False
    if i00 == 192:
        if i01 != 168:
            print 222222222222222222222222222222222222222
            return False
    if not i02.isdigit():
        return False
    i02 = int(i02)
    if i02 < 0 or i02 > 255:
        print 33333333333333333333333333333333333333333
        return False
    iiii = 23
    iii = 1
    while iiii > 19:
        network_number = locals()
        iii = iii * 2
        network_number[iiii] = []
        ii = 0
        while ii < 255:
            network_number[iiii].append(ii)
            ii = ii + iii
        print network_number[iiii]
        if i1 == iiii:
            print network_number[iiii]
            if i02 not in network_number[iiii]:
                print 2313213213213213213213213213213213
                return False
        iiii = iiii - 1
    if not i03.isdigit():
        return False
    i03 = int(i03)
    if i03 < 0 or i03 > 255:
        print 444444444444444444444444444444444444444
        return False
    if i1 < 25:
        if i03 != 0:
            print 798798798798797987987
            return False
    iiii = 31
    iii = 1
    while iiii > 24:
        network_number = locals()
        iii = iii * 2
        network_number[iiii] = []
        ii = 0
        while ii < 255:
            network_number[iiii].append(ii)
            ii = ii + iii
        print network_number[iiii]
        if i1 == iiii:
            print network_number[iiii]
            if i03 not in network_number[iiii]:
                print 23132132132132132132132132132132131
                return False
        iiii = iiii - 1
    return True
input = raw_input("please input:")
ip = isgoodsubnet(input)
if ip == True:
    print "right"
while ip == False:
    print "error"
    input = raw_input("please input:")
    ip = isgoodsubnet(input)
    if ip == True:
        print "right"
