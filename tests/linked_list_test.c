#include <stdio.h>
#include "../src/c/linked_lists/linked_list.h"

int main() {
    Node *head = NULL;

    // Test insertion
    insert_at_head(&head, 10);
    insert_at_head(&head, 20);
    insert_at_head(&head, 30);

    // Expected output: 30 -> 20 -> 10 -> NULL
    print_list(head);

    // Clean up
    free_list(head);
    return 0;
}