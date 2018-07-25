class Queue:
	
	def __init__(self):
		self.queue=[]
	
	def enqueue(self,item):
		self.queue.insert(0,item)
	
	def isEmpty(self):
		return self.queue == []
	
	def dequeue(self):
		return self.queue.pop()
	
	def size(self):
		return len(self.queue)


class Vertex:
	def __init__(self,key):
		self.id=key
		self.connectedTo={}
		
	def addNeighbor(self,nbr,weight=0):
		self.connectedTo[nbr]=weight
		
	def __str__(self):
		return str(self.id)+' Connected To : '+str([x.id for x in self.connectedTo])
		
	def getConnections(self):
		return self.connectedTo.keys()
	
	def getId(self):
		return self.id
		
	def getWeight(self,nbr):
		return self.connectedTo[nbr]
	
	#def __repr__(self):
	#	return str(self.__dict__)


class Graph:
	def __init__(self):
		self.vertList={}
		self.numVertices=0
		
	def addVertex(self,key):
		self.numVertices=self.numVertices+1
		newVertex=Vertex(key)
		self.vertList[key]=newVertex
		return newVertex
	
	def addEdges(self,f,t,cost=0):
		if f in self.vertList:
			if t in self.vertList:
				self.vertList[f].addNeighbor(self.vertList[t],cost)
			else:
				return "Not present in Graph"
		else:
			return "Not present in Graph"
			
	def getVertex(self,n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None
	
	def getVertices(self):
		return self.vertList.keys()
	
	def __iter__(self):
		return iter(self.vertList.values())
	
	def __contains(self,n):
		return n in self.vertList


def bfs(graph,start):
		#Keep track of all visited nodes
		visited=[]
		#keep track of nodes to be checked using queue
		vertQueue= Queue()
		vertQueue.enqueue(start)
		#Keep looking until there are nodes still to be checked
		while vertQueue:
			#pop shallowest node (first node ) from queue
			currentVert=vertQueue.dequeue()
			visited.append(currentVert)
			#print(currentVert,end="")
			print(graph.vertList[currentVert].getConnections())
			for nbr in (graph.vertList[currentVert].getConnections()):
				if nbr not in visited:
					#add node to list of checked nodes
					vertQueue.enqueue(nbr)
					visited.append(currentVert)
			return visited		

'''# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
	# keep track of all visited nodes
	explored = []
	# keep track of nodes to be checked
	queue = [start]
	# keep looping until there are nodes still to be checked
	while queue:
		# pop shallowest node (first node) from queue
		node = queue.pop(0)
		if node not in explored:
			# add node to list of checked nodes
			explored.append(node)
			neighbours = graph[node]
			# add neighbours of node to queue
			for neighbour in neighbours:
				queue.append(neighbour)
	return explored'''
	
g=Graph()
for i in range(1,7):
	print(g.addVertex(i))
g.addEdges(1,2,12)
g.addEdges(2,3,23)
g.addEdges(1,3,13)
g.addEdges(2,4,24)
g.addEdges(6,4,64)
g.addEdges(3,6,36)
g.addEdges(3,5,35)
g.addEdges(5,6,56)
g.addEdges(6,1,61)
print(bfs(g,1))
