#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;
#define bucketSize 256

void bucketInput(int a, int b)
{
    if (a > bucketSize)
        cout << "\n\t\tBucket overflow";
    else
    {
        sleep(3);
        while (a > b)
        {
            cout << "\n\t\t" << b << " bytes outputted.";
            a -= b;
            sleep(3);
        }
        if (a > 0)
            cout << "\n\t\tLast " << a << " bytes sent\t";
        cout << "\n\t\tBucket output successful";
    }
}
int main()
{
    int op;

    op = 50;

    cout << "Output Rate is 50 Mbps" << endl;

    // cout << "Enter output rate : ";
    // cin >> op;
    int n = 10;

    int PacketArr[n] = {100, 345, 230, 78, 980, 130, 7, 89, 670, 256};
    srand(time(0));
    for (int i = 0; i < n; i++)
    {
        // sleep(rand() % 10);
        sleep(5);
        // pktSize = rand() % 700;
        cout << "\nPacket no " << i + 1 << "\tPacket size = " << PacketArr[i];
        bucketInput(PacketArr[i], op);
    }
    cout << endl;
    return 0;
}