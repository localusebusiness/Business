#include<iostream>          
using namespace std;


int main() 
{
    int numVertices, i, j, k, row, col, minCost = 0, minWeight;
    char choice;
    cout << "Enter number of vertices: ";
    cin >> numVertices;
    int weightMatrix[numVertices][numVertices];
    int visited[numVertices];
    for (i = 0; i < numVertices; i++)
        visited[i] = 0;
    for (i = 0; i < numVertices; i++)
        for (int j = 0; j < numVertices; j++)
            weightMatrix[i][j] = -1;

    for (i = 0; i < numVertices; i++)
    {
        for (j = i + 1; j < numVertices; j++)
        {
            cout << "Do you want an edge between " << i << " and " << j << ": ";
           
            cin >> choice;
            if (choice == 'y' || choice == 'Y')
            {
                cout << "Enter weight: ";
                cin >> weightMatrix[i][j];
                weightMatrix[j][i] = weightMatrix[i][j];
            }
        }
    }
    visited[0] = 1;
    for (k = 0; k < numVertices - 1; k++)
    {
        minWeight = 999;
        for (i = 0; i < numVertices; i++)
        {
            for (j = 0; j < numVertices; j++)
            {
                if (visited[i] == 1 && visited[j] == 0)
                {
                    if (weightMatrix[i][j] != -1 && minWeight > weightMatrix[i][j])
                    {
                        minWeight = weightMatrix[i][j];
                        row = i;
                        col = j;
                    }
                }
            }
        }
        minCost += minWeight;
        visited[col] = 1;
        weightMatrix[row][col] = weightMatrix[col][row] = -1;
        cout << row << "->" << col << endl;
       
    }
    cout << "\nMin. Cost: " << minCost;
    return 0;
}
