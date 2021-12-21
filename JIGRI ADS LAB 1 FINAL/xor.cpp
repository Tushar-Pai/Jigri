#include <iostream>
#include <bits/stdc++.h>
#include <cinttypes>
using namespace std;

typedef struct node
{
    int data;
    struct node *link;
} Node;

Node *XOR(Node *x, Node *y)
{
    return reinterpret_cast<Node *>(reinterpret_cast<uintptr_t>(x) ^ reinterpret_cast<uintptr_t>(y));
}

void traverse(Node *head)
{
    if (head == NULL)
    {
        cout << "List empty" << endl;
        return;
    }

    Node *curr = head;
    Node *prev = NULL;
    Node *next;

    while (curr != NULL)
    {
        cout << curr->data << " ";
        next = XOR(prev, curr->link);
        prev = curr;
        curr = next;
    }

    cout << endl;
}

Node *insert_begin(Node *head, int val)
{

    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = val;
    newNode->link = XOR(head, NULL);

    if (head != NULL)
    {
        head->link = XOR(newNode, XOR(head->link, NULL));
    }

    head = newNode;

    return head;
}

Node *delete_begin(Node *head)
{

    if (head == NULL)
    {
        cout << "List Empty" << endl;
        return NULL;
    }
    Node *temp = head;
    Node *next = XOR(temp->link, NULL);
    next->link = XOR(NULL, XOR(next->link, temp));
    temp->link = NULL;
    free(temp);
    head = next;

    return head;
}

int main()
{
    Node *head = NULL;
    head = insert_begin(head, 1);
    head = insert_begin(head, 2);
    head = insert_begin(head, 3);
    head = insert_begin(head, 4);
    head = insert_begin(head, 5);
    head = insert_begin(head, 6);
    traverse(head);
    head = delete_begin(head);
    head = delete_begin(head);

    traverse(head);
    return 0;
}