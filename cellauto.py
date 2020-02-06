import numpy as np
import sys

def make_rule( input ):
    rule = [int(x) for x in list('{0:0b}'.format(input))]
    rule.reverse()
    while len(rule) < 8:
        rule.append(0)
    return rule

def process_line( line, rule ):
    newline = []
    for i in range( 0, len(line) ): 
        test = line[i] * 2
        if i != 0:
            test += line[i-1] * 4
        if i != len(line) - 1:
            test += line[i+1]
        newline.append( rule[test] )
    return newline

def print_grid( grid ):

    num = 0
    for i in grid:
        sys.stdout.write( str(num) + "\t: ")
        for j in i:
            if j == 1:
                sys.stdout.write( '#' )
            else:
                sys.stdout.write( ' ' )
        print()




x = 200
y = 500

grid = [[]]
for i in range(0,x):
    grid[0].append( 0 )

grid[0][int(x/2)] = 1
grid[0][int(x/2)+1] = 1


rule = make_rule( 106 )
for i in range( 0, y ):
    grid.append( process_line( grid[i] , rule) )

print_grid( grid )
print('ys')