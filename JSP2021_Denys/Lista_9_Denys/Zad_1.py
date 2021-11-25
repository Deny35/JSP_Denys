import numpy

a = numpy.array([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])
b = numpy.array([6,2,-5,17,12])
solvs = numpy.linalg.solve(a,b)
print("x=",solvs[0]," y=",solvs[1]," z=",solvs[2], " t=",solvs[3]," u=",solvs[4])