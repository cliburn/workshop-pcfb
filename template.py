# a one-line version of the template program in PCFB

def well(cmin=1, cmax=12, rmin='A', rmax='H'):
    return '\n'.join(
        [' '.join([chr(s) + str(n) for n in range(cmin, cmax+1)])
         for s in range(ord(rmin), ord(rmax)+1)])

print well()
