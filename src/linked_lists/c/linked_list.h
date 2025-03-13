#ifndef LINKEDLIST_H
#define LINKEDLIST_H

typedef struct Node {
    int data;
    struct Node *next;
} Node;

// Function declarations
Node* create_node(int data);
void insert_at_head(Node **head, int data);
void print_list(Node *head);
void free_list(Node *head);

#endif
