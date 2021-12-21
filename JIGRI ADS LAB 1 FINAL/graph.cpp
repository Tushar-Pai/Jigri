#include <bits/stdc++.h>
using namespace std;
const int N = 1000;
int parent[N];
int rank_arr[N];
int flag = 0;
int cycles = 0;

void makeset()
{
    for (int i = 1; i < 1000; i++)
    {
        parent[i] = i;
        rank_arr[i] = 0;
    }
}

int findparent(int node)
{
    if (node == parent[node])
        return node;
    return parent[node] = findparent(parent[node]);
}

void union_fun(int u, int v)
{
    u = findparent(u);
    v = findparent(v);
    if (u == v)
    {
        flag = 1;
        cycles++;
    }

    if (rank_arr[u] < rank_arr[v])
    {
        parent[u] = v;
    }
    else if (rank_arr[u] > rank_arr[v])
    {
        parent[v] = u;
    }
    else
    {
        parent[v] = u;
        rank_arr[u]++;
    }
}

int main()
{

    makeset();
    int m;
    cin >> m;

    while (m--)
    {
        int u, v;
        cin >> u >> v;
        union_fun(u, v);
    }
    cout << (flag == 1 ? "yes" : "no") << endl;
    cout << "NUMBER OF CYCLES IS"
         << " " << cycles << endl;
    return 0;
}