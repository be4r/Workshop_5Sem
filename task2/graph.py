#!/usr/bin/python3
'''
Module docstring
Pylint told me to write this
Module implements class Graph which appears to be a Graph
Also modle implements 2 methods of searching through Graph
'''

class Graph:
    '''
    Graph class implements Graph as Graph
    '''
    weighted = False
    vert = {}
    allvert = ""
    w = {}
    def __init__(self, edges):
        for i in edges:
            s_0 = str(i[0]) #cmon man this is SNAKE CASE and IT SHLD BE respected
            s_1 = str(i[1]) #much better name than s0 and s1(which suck too but still)
            self.vert[s_0] = self.vert[s_0] + s_1 if self.vert.get(s_0) else s_1
            self.vert[s_1] = self.vert[s_1] + s_0 if self.vert.get(s_1) else s_0
            if s_0 not in self.allvert:
                self.allvert += s_0
            if s_1 not in self.allvert:
                self.allvert += s_1
            if len(i) > 2:
                self.weighted = True
                if not self.w.get(s_0):
                    self.w[s_0] = {}
                if not self.w.get(s_1):
                    self.w[s_1] = {}
                self.w[s_0][s_1] = int(i[2])
                self.w[s_1][s_0] = int(i[2])
        self.allvert = ''.join(sorted(self.allvert))

    def __repr__(self):
        return str(self.vert) + ('\n' + str(self.w)) if self.weighted else '' + '\n' + self.allvert

    def dfs(self, visited, start):
        "deepth"
        visited += start
        print(start, end=' ')
        for i in self.vert[start]:
            if not i in visited:
                self.dfs(visited, i)

    def bfs(self, start):
        "broad"
        que = start
        pth = {start:'-1'}
        visited = start
        print(start, end=' ')
        while que:
            cur = que[0]
            que = que[1:]
            for i in self.vert[cur]:
                if i not in visited:
                    visited += i
                    que += i
                    pth[i] = cur
                    print(i, end=' ')
        return pth

if __name__ == '__main__':
    #G = Graph(eval(input()))
    G = Graph([[0, 3], [1, 3], [2, 3], [4, 3], [5, 4], [2, 6]])
    #print(G)
    print()
    G.bfs(G.allvert[0])
    print()
    G.dfs([], G.allvert[0])
    print()