def func5(arg52, arg53):
    var56 = class6()
    for var57 in range(3):
        var58 = var56.func7
        var58(arg53, var57)
    var61 = class8()
    for var62 in func10(arg52, arg53):
        var75 = var61.func9
        var75(var62, arg52)
    var90 = func11(arg53, arg52)
    var91 = (arg53 - 691) ^ arg53
    result = var91 ^ var91 ^ var90
    return result
def func11(arg76, arg77):
    var78 = arg76 + arg77 + -2016839187 ^ arg76
    var79 = ((arg77 + var78) & 555) | arg76
    var80 = 1879239415 & (var78 & var79)
    var81 = arg77 + (504 ^ var80) | var79
    var82 = (arg76 & var78) | -984
    var83 = (-860 | arg77) ^ var81
    var84 = (var80 & arg77 + var81) & var79
    var85 = var81 & var80 | var84 - var82
    var86 = var83 + 853 & var80 - var80
    var87 = (var78 + var83) - var83
    var88 = arg77 + var84
    var89 = var88 ^ 995 ^ var81 + var87
    result = (var87 & var80) | (var85 ^ 1694523718) - var88
    return result
def func10(arg63, arg64):
    var65 = 754 | (-556418778 | arg64 - arg64)
    yield var65
    var66 = arg63 | -888277945 + arg64 - 1816384675
    yield var66
    var67 = 550 - -23163634 + (arg63 | arg63)
    yield var67
    var68 = arg63 | 912 - arg64 - var65
    yield var68
    var69 = -160 | var68
    yield var69
    var70 = var68 & 633
    yield var70
    var71 = (arg64 ^ var70) | var69 & -86
    yield var71
    var72 = 393610843 - -544013334
    yield var72
    var73 = var69 ^ arg63
    yield var73
    var74 = var71 + var69 | var69 | var67
    yield var74
class class8(object):
    def func9(self, arg59, arg60):
        return 0
class class6(object):
    def func7(self, arg54, arg55):
        return 0
def func4(arg27, arg28):
    var29 = 1110683104 | arg27
    var30 = 665 - -154006312 - arg28
    var31 = var29 + 392
    var32 = (var30 - 828270908) | var29 | var31
    var33 = var32 | (var31 | arg27 + var29)
    var34 = -345 - var31 + var30 | arg28
    var35 = ((var32 ^ var32) | var32) & var30
    var36 = -1168490510 - var32 + (var35 & var31)
    var37 = var32 | ((arg27 + 762679365) & var31)
    var38 = var37 + (var35 + (var31 ^ 310614214))
    var39 = var30 & ((var31 ^ arg27) | var33)
    if var36 < var36:
        var40 = arg27 | var34
    else:
        var40 = (-707 ^ var30) & var37 - var38
    var41 = var33 + var32
    if var38 < var35:
        var42 = var31 ^ var33
    else:
        var42 = var36 - var39
    var43 = arg27 + ((var34 + var33) ^ var33)
    var44 = ((var39 + var30) + var35) - var32
    if var35 < var39:
        var45 = 631 + var32
    else:
        var45 = var39 + arg28
    var46 = var39 ^ var44 ^ (arg28 + var34)
    if var29 < arg28:
        var47 = var31 + var29
    else:
        var47 = (arg28 | var30 & var29) ^ var39
    var48 = (var44 | var31 ^ var33) ^ var34
    var49 = (var29 - var30) ^ (arg28 & var41)
    var50 = var33 - var48
    var51 = var31 | var31 ^ var37 ^ var31
    result = var43 ^ var29 ^ var30
    return result
def func1(arg1, arg2):
    var6 = func2(arg1, arg2)
    var7 = var6 | arg1
    if arg1 < var7:
        var8 = ((670 - arg2) | arg1) + var7
    else:
        var8 = var7 - var7
    var9 = -171901259 | ((arg2 | 636) - arg2)
    var10 = arg2 + arg2
    var11 = var7 ^ (var10 & arg2 ^ 938)
    var12 = (var11 - var9) + var6 + -219484529
    var13 = var7 | var12
    var14 = var13 | var12 + var7 | var6
    var15 = var7 | var9
    var16 = var14 + var13 & var13 + var11
    var17 = var7 - 658 + (63 & arg2)
    var18 = (var16 & var11) & arg2
    if var7 < var15:
        var19 = var14 + 74 | var10 ^ var7
    else:
        var19 = var18 | var12 & (var14 & var9)
    var20 = var11 + var9
    var21 = var17 ^ var20
    var22 = var7 + var11 + arg1 ^ var14
    var23 = var18 ^ arg2
    var24 = var17 & var20 | var20 - 593
    var25 = (var18 ^ var24 ^ var21) ^ var10
    var26 = (var18 | (var18 ^ arg2)) | var12
    result = 648 - (((var15 & 265 + arg1 ^ (var23 - (var7 ^ var13) & (var14 | var9) ^ var22)) + arg2) - 334)
    return result
def func2(arg3, arg4):
    def func3(acc, rest):
        var5 = acc | 1 + -3
        if acc == 0:
            return var5
        else:
            result = func3(acc - 1, var5)
            return result
    result = func3(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 1'
    print 'func_number: 4'
    print 'arg_number: 27'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 1'
    print 'func_number: 5'
    print 'arg_number: 52'
    for i in xrange(25000):
        x = 5
        x = func4(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 12'
    print 'arg_number: 92'
    for i in xrange(25000):
        x = 5
        x = func5(x, i)
        print x,
