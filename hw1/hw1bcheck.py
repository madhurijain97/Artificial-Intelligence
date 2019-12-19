#n-policement with m scooters
import time
start_time = time.time()
fileopen=open('input_scooter.txt', 'r')
fileout=open('output_scooter_test.txt','w')
i,maxval,depth, flag=0,0,0, 10
maxvallist, finalmaxlist, zeroposition, maxchecker, maxcheckerval = [], [], [], [], []
maxchecker.append([0,0,-1,-1])
maxcheckerval.append(0)

def zerodepthfirstsearch(i, maxcheckerrow, maxcheckercol):
	for j in range(i+1, len(zeroposition)):
		zerolist = zeroposition[j]
		zerorow = zerolist[0]
		zerocol = zerolist[1]
		while maxcheckerrow != -1 and maxcheckercol != -1:
			if zerorow != maxcheckerrow and zerocol != maxcheckercol and abs(zerorow-maxcheckerrow) != abs(zerocol-maxcheckercol):
				maxcheckerlist = parent[maxcheckerrow][maxcheckercol]
				maxcheckerrow, maxcheckercol = maxcheckerlist[0], maxcheckerlist[1]
				maxcheckerrow = int(maxcheckerrow)
				maxcheckercol = int(maxcheckercol)
				if maxcheckerrow == -1 and maxcheckercol == -1:
					parent[zerorow][zerocol] = [rootrow, rootcol]
					depthchecker += 1
					flag=6
				if depthchecker == police:
					finalmaxlist.append(maxcheckervalue)
					flag = 5
					break
		maxcheckerrow=zerorow
		maxheckercol=zerocol
		if flag == 6:
			zerodepthfirstsearch(j, maxcheckerrow, maxcheckercol)
		if flag==5:
			break
	
		

def depthfirstsearch(rootrow, rootcol, depth):
	global maxval
	rootrowcheck = rootrow
	rootcolcheck = rootcol
	for j in range(rootrow, sizeofgrid):
		for k in range(sizeofgrid):
			if grid[j][k] > 0 and depth <= police:
				while(rootrowcheck != -1 and rootcolcheck != -1):
					if rootrowcheck == j: 
						flag = 2
						break
					elif rootcolcheck == k or abs(rootrowcheck-j) == abs(rootcolcheck-k):
						flag = 0
						break
					rootchecklist = parent[rootrowcheck][rootcolcheck]
					rootrowcheck, rootcolcheck = rootchecklist[0], rootchecklist[1]
					rootrowcheck = int(rootrowcheck)
					rootcolcheck = int(rootcolcheck)
					if rootrowcheck == -1 and rootcolcheck == -1:
						parent[j][k] = [rootrow, rootcol]
						maxval += grid[j][k]
						parentlist = parent[j][k]
						parentrow = parentlist[0]
						parentcol = parentlist[1]
						maxmatrix[j][k] = int(grid[j][k]) + int(maxmatrix[parentrow][parentcol])
						fileout.write("Adding:" + str(grid[j][k]) + " " + str(maxmatrix[parentrow][parentcol]) + " = " + str(maxmatrix[j][k]) + " depth" + str(depth) + "\n")	
						if depth == police:
							maxvallist.append(maxmatrix[j][k])
						else:
							maxcheckerval.append(maxmatrix[j][k])
							maxchecker.append([maxmatrix[j][k], depth, j, k])
						flag = 1
				fileout.write("maxvallist" + str(maxvallist) + "\n")
				fileout.write("maxchecker" + str(maxchecker) + "\n")
				rootrowcheck = rootrow
				rootcolcheck = rootcol
				if flag == 1 and depth + 1 <= police:
					depthfirstsearch(j, k, depth + 1)
				elif flag == 2:
					break
			else:
				flag = 3
				break
		if flag == 3:
			break
					
					
with fileopen as inputfile:
	for line in inputfile:
		if i == 0:
			sizeofgrid=int(line)
			sizeofgrid=5
			fileout.write(str(sizeofgrid))
			grid = [[0 for x in range(sizeofgrid)] for y in range(sizeofgrid)] 
			parent=[[0 for x in range(sizeofgrid)] for y in range(sizeofgrid)]
			maxmatrix=[[0 for x in range(sizeofgrid)] for y in range(sizeofgrid)]
			i += 1
		elif i == 1:
			police=int(line)
			police=4
			fileout.write("Police " + str(police) + "\n")
			i += 1
		elif i == 2:
			scooters=int(line)
			fileout.write("Scooters " + str(scooters) + "\n")
			i += 1
		else:
			row,col = line.split(",")
			grid[int(row)][int(col)] += 1
			if police == 1:
				if grid[int(row)][int(col)] > maxval:
					maxval = grid[int(row)][int(col)]
	
	grid = [[2, 0, 0, 0, 0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,5]]
	fileout.write(str(grid) + "\n")

	if police == 1:
		depth = 1
		fileout.write("maxval " + str(maxval) + "\n")
	else:
		for i in range(sizeofgrid):
			for j in range(sizeofgrid):
				del parent[:]
				del maxvallist[:]
				parent = [[0 for x in range(sizeofgrid)] for y in range(sizeofgrid)]
				del maxmatrix[:]
				maxmatrix = [[0 for x in range(sizeofgrid)] for y in range(sizeofgrid)]
				rootval = grid[i][j]
				depth = 1
				fileout.write("i,j " + str(i) + " " + str(j) + "\n")
				parent[i][j] = [-1,-1]
				maxmatrix[i][j] = rootval
				if rootval == 0:
					zeroposition.append([i,j])
					continue
				maxchecker.append([maxmatrix[i][j], depth, i, j])
				maxcheckerval.append(maxmatrix[i][j])
				maxvallist = []
				maxvallist.append(0)
				depthfirstsearch(i, j, depth + 1)
				fileout.write("maxvallist " + str(maxvallist) + "\n")
				fileout.write("max of maxvallist " + str(max(maxvallist)) + "\n")
				finalmaxlist.append(max(maxvallist))
		if max(maxcheckerval)>max(finalmaxlist):
			flag = 4
					
		if flag == 4:
			for i in range(len(maxchecker)):
				maxcheckerlist = maxchecker[i]
				maxcheckervalue = maxcheckerlist[0]
				maxcheckerdepth = maxcheckerlist[1]
				depthchecker=maxcheckerdepth
				maxcheckerrow = maxcheckerlist[2]
				maxcheckercol = maxcheckerlist[3]
				rootrow = maxcheckerrow
				rootcol = maxcheckercol
				
				if maxcheckervalue > max(finalmaxlist):
					if len(zeroposition) < (police - maxcheckerdepth):
						continue
					else:
						for k in range(len(zeroposition)):
							if flag!=5:
								zerodepthfirstsearch(-1, maxcheckerrow, maxcheckercol)
			
		fileout.write(str(finalmaxlist) + "\n")
		fileout.write(str(max(finalmaxlist)) + "\n")
fileout.write(str(grid) + "\n")
print("--- %s seconds ---" % (time.time() - start_time))			
fileopen.close()
fileout.close()
