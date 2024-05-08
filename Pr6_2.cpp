#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Graph {
private:
    vector<vector<int>> adjMatrix;

public:
    Graph(int numVertices) : adjMatrix(numVertices, vector<int>(numVertices, 0)) {}

    void printAdjMatrix() {
        for (int i = 0; i < adjMatrix.size(); ++i) {
            for (int j = 0; j < adjMatrix[i].size(); ++j) {
                cout << adjMatrix[i][j] << " ";
            }
            cout << endl;
        }
    }

    void addEdge(int i, int j) {
        adjMatrix[i][j] = 1;
        adjMatrix[j][i] = 1;
    }

    

    void bfs(int startVertex) {
        vector<bool> visited(adjMatrix.size(), false);
        queue<int> q;

        visited[startVertex] = true;
        q.push(startVertex);

        while (!q.empty()) {
            int currentVertex = q.front();
            cout << currentVertex << " ";
            q.pop();

            for (int i = 0; i < adjMatrix.size(); ++i) {
                if (adjMatrix[currentVertex][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    q.push(i);
                }
            }
        }
    }
};

int main() {

    int n,e,k,i,j,start;
    cout<<"Enter no of vertices";
    cin>>n;
    cout<<"Enter no of edges";
    cin>>e;
    Graph g(n);
    for(k=0;k<e;k++)

    {
        cout<<"Enter U and V:";
        cin >> i >> j;
          g.addEdge(i,j);

    }
 

    g.printAdjMatrix();

    cout<<"Enter the starting vertex";
    cin>> start;

    cout << "BFS starting from vertex :"<< start<<endl;
    g.bfs(start);

    return 0;
}