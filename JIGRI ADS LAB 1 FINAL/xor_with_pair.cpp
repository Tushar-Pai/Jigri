#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int data;
    Node *xn;
};

Node *Xor(Node *node1, Node *node2)
{
    return reinterpret_cast<Node *>(
        reinterpret_cast<uintptr_t>(node1) ^ reinterpret_cast<uintptr_t>(node2));
}

Node *insertfront(Node *head, int data)
{
    Node *newNode = new Node();
    newNode->data = data;
    newNode->xn = head;
    if (head != nullptr)
    {
        head->xn = Xor(newNode, head->xn);
    }
    head = newNode;
    return head;
}

Node *deletefront(Node *head)
{
    Node *next = head->xn;
    next->xn = Xor(head, next->xn);
    free(head);
    return next;
}

void print(Node *head)
{
    Node *temp = head;
    Node *prev = NULL;
    Node *next;

    cout << "The nodes of Linked List are: \n";
    while (temp != nullptr)
    {
        cout << temp->data << " ";
        next = Xor(prev, temp->xn);
        prev = temp;
        temp = next;
    }
    cout << endl;
}

void findpair(Node *head, int key)
{
    Node *temp = head;
    Node *prev = NULL;
    Node *next;
    unordered_map<int, int> umap;
    while (temp != nullptr)
    {
        int t = key % temp->data == 0 ? key / temp->data : -1;
        if (t != -1)
        {
            if (umap.find(t) != umap.end())
            {
                cout << t << " " << umap[t] << endl;
            }
            else
            {
                umap[temp->data] = t;
            }
        }
        next = Xor(prev, temp->xn);
        prev = temp;
        temp = next;
    }
}

int main()
{
    Node *head = nullptr;
    int n;

    head = insertfront(head, 1);
    head = insertfront(head, 2);
    head = insertfront(head, 3);
    head = insertfront(head, 4);
    head = insertfront(head, 5);
    head = insertfront(head, 6);
    print(head);
    cout << "Value producing Pairs are:" << endl;
    findpair(head, 6);

    return 0;
}