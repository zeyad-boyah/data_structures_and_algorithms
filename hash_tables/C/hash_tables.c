#include <stdio.h>
#include <stdlib.h>

#define CAPACITY 20 // initial size of the hash table array

// Structure representing a node in the hash table
typedef struct HashNode {
    int key;    // The key for the hash map entry
    int value;  // The corresponding value
} HashNode;

// Structure representing the hash map itself
typedef struct HashMap {
    HashNode** arr; // Array of pointers to HashNode
    int capacity;   // Total capacity of the array
    int current_size;       // Number of valid elements currently stored
    HashNode* dummy; // Dummy node to mark deleted positions
} HashMap;

// Create and initialize a new HashMap
HashMap* createHashMap() {
    HashMap* map = (HashMap*)malloc(sizeof(HashMap));
    map->capacity = CAPACITY;
    map->current_size = 0;
    // Allocate an array of HashNode* with size CAPACITY
    map->arr = (HashNode**)malloc(sizeof(HashNode*) * map->capacity);
    
    // Initialize all array slots to NULL
    for (int i = 0; i < map->capacity; i++) {
        map->arr[i] = NULL;
    }
    
    // Create a dummy node (using key and value -1) for deletion markers
    map->dummy = (HashNode*)malloc(sizeof(HashNode));
    map->dummy->key = -1;
    map->dummy->value = -1;
    
    return map;
}

// Hash function to compute an index for a given key
int hashCode(HashMap* map, int key) {
    return key % map->capacity;
}

// Insert a key-value pair into the hash map
void insertNode(HashMap* map, int key, int value) {
    // Create a new node with the given key and value
    HashNode* temp = (HashNode*)malloc(sizeof(HashNode));
    temp->key = key;
    temp->value = value;

    // Compute initial hash index using the hash function
    int hashIndex = hashCode(map, key);

    // Use linear probing to find the next free slot or a slot with the same key or dummy node
    while (map->arr[hashIndex] != NULL &&
           map->arr[hashIndex]->key != key &&
           map->arr[hashIndex]->key != -1) {
        hashIndex++;
        hashIndex %= map->capacity;
    }

    // If we're inserting into an empty or dummy slot, increment the size
    if (map->arr[hashIndex] == NULL || map->arr[hashIndex]->key == -1) {
        map->current_size++;
    }
    map->arr[hashIndex] = temp;
}

// Delete a node with the given key from the hash map
// Returns the value of the deleted node or -1 if not found.
int deleteNode(HashMap* map, int key) {
    int hashIndex = hashCode(map, key);

    // Use linear probing to find the node with the given key
    while (map->arr[hashIndex] != NULL) {
        if (map->arr[hashIndex]->key == key) {
            int value = map->arr[hashIndex]->value;
            // Free the node and replace it with the dummy node
            free(map->arr[hashIndex]);
            map->arr[hashIndex] = map->dummy;
            map->current_size--;
            return value;
        }
        hashIndex++;
        hashIndex %= map->capacity;
    }
    return -1; // Not found
}

// Retrieve the value associated with a key in the hash map
// Returns the value if found, otherwise returns -1.
int get(HashMap* map, int key) {
    int hashIndex = hashCode(map, key);
    int counter = 0;  // Prevent infinite loops

    // Use linear probing to search for the key
    while (map->arr[hashIndex] != NULL) {
        if (counter++ > map->capacity)
            return -1;
        if (map->arr[hashIndex]->key == key)
            return map->arr[hashIndex]->value;
        hashIndex++;
        hashIndex %= map->capacity;
    }
    return -1; // Not found
}

// Display the key-value pairs stored in the hash map
void display(HashMap* map) {
    for (int i = 0; i < map->capacity; i++) {
        if (map->arr[i] != NULL && map->arr[i]->key != -1)
            printf("key = %d  value = %d\n", map->arr[i]->key, map->arr[i]->value);
    }
}

// Free all memory allocated for the hash map
void freeHashMap(HashMap* map) {
    // Free all nodes in the array (except the dummy, which is freed later)
    for (int i = 0; i < map->capacity; i++) {
        if (map->arr[i] != NULL && map->arr[i] != map->dummy) {
            free(map->arr[i]);
        }
    }
    // Free the dummy node
    free(map->dummy);
    // Free the array of pointers
    free(map->arr);
    // Finally, free the HashMap structure itself
    free(map);
}

// Main function to test the hash map implementation
int main() {
    HashMap* h = createHashMap();
    
    // Insert key-value pairs
    insertNode(h, 1, 1);
    insertNode(h, 2, 2);
    // Inserting with an existing key updates the value (in our linear probing, it finds the same key)
    insertNode(h, 2, 3);
    
    // Display all key-value pairs
    display(h);
    printf("Size: %d\n", h->current_size);
    
    // Delete a key and display the returned value
    printf("Deleted value for key 2: %d\n", deleteNode(h, 2));
    printf("Size after deletion: %d\n", h->current_size);
    
    // Check if the map is empty (if size == 0)
    printf("Is empty: %s\n", h->current_size == 0 ? "true" : "false");
    
    // Try to get the value for key 2 after deletion
    printf("Get key 2: %d\n", get(h, 2));

    // Free allocated memory 
    freeHashMap(h);
    
    return 0;
}
