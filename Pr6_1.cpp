#include <iostream>
#include <cstdlib>
using namespace std;
int graph[10][10], a, b, c, numVertices, x, y;
int stack[10], top = 0, visitStack[10], visitedStack[10];
int main()
{
    int numEdges;
    cout << "Enter number of vertices : ";
    cin >> numVertices;
    cout << "Enter number of edges : ";
    cin >> numEdges;

    cout << "\nEDGES :\n";
    for (c = 1; c <= numEdges; c++)
    {
        cout << "Enter X and Y:";
        cin >> a >> b;
        graph[a][b] = 1;
        graph[b][a] = 1;
    }

    cout << "The adjacency matrix of the graph is : " << endl;
    for (a = 1; a <= numVertices; a++)
    {
        for (b = 1; b <= numVertices; b++)
        {
            cout << " " << graph[a][b];
        }
        cout << endl;
    }

    cout << endl
         << "Enter initial vertex : ";
    cin >> y;
    cout << "The DFS of the Graph is\n";
    cout << y;
    visitedStack[y] = 1;
    c = 1;
    while (c < numVertices)
    {
        for (b = numVertices; b >= 1; b--)
            if (graph[y][b] != 0 && visitedStack[b] != 1 && visitStack[b] != 1)
            {
                visitStack[b] = 1;
                stack[top] = b;
                top++;
            }
        y = stack[--top];
        cout << y << " ";
        c++;
        visitStack[y] = 0;
        visitedStack[y] = 1;
    }
    return 0;
}
