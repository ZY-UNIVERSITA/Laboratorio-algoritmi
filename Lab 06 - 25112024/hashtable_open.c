#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/* Information pieces are key-value pairs */

typedef int TKey;
typedef int TValue;

typedef struct TInfo {
    TKey key;
    TValue value;
} TInfo;

typedef struct OpenArray {
    TKey key;
    TValue value;
    bool isEmpty;
} OpenArray;

typedef struct HashTable {
    OpenArray* bucket;
    int nbuckets;
    int size;
} HashTable;

int fi_grow = 2;

/* Indirizzamento aperto */
unsigned int hash_function(int key);
unsigned int hash_int(TKey key);
void hashtable_insert(HashTable* h, TKey key, TValue value);

unsigned int hash_function(int key) {
    return key;
}

unsigned int hashtable_hash(HashTable *h, TKey key) {
    return hash_function(key) % h->nbuckets;
}

bool array_resize(HashTable *h) {
    int new_size = h->nbuckets * fi_grow;
    OpenArray* array = (OpenArray*) malloc(sizeof(OpenArray) * new_size);

    if (array == NULL) {
        return array != NULL;
    }

    for (int i = 0; i < new_size; i++) {
        array[i] = (OpenArray) { 0, 0, true };
    }

    OpenArray* oldArray = h->bucket;
    int oldSize = h->nbuckets;

    h->bucket = array;
    h->nbuckets = new_size;
    h->size = 0;

    for (int i = 0; i < oldSize; i++) {
        hashtable_insert(h, oldArray[i].key, oldArray[i].value);
    }

    free(oldArray);

    return array != NULL;
}

HashTable *hashtable_create(int nbuckets) {
    HashTable *h = (HashTable*) malloc(sizeof(HashTable));

    if (h == NULL) {
        return NULL;
    }

    h->bucket = (OpenArray*) malloc(sizeof(OpenArray) * nbuckets);

    if (h->bucket == NULL) { 
        free(h); 
        return NULL; 
    }

    h->nbuckets = nbuckets;
    h->size = 0;

    for(int i = 0; i < nbuckets; i++) {
        h->bucket[i] = (OpenArray) { 0, 0, true };
    }

    return h;
}



void hashtable_insert(HashTable* h, TKey key, TValue value) {
    if (h != NULL) {
        bool isFull = false;
        if (h->size / h->nbuckets > 0.75) {
            isFull = true;
            isFull = array_resize(h);
        }

        if (!isFull) {
            int hashcode = hashtable_hash(h, key);
            while (hashcode < h->nbuckets && h->bucket[hashcode].isEmpty == false) {
                hashcode++;
            }

            h->bucket[hashcode].key = key;
            h->bucket[hashcode].value = value;
            h->bucket[hashcode].isEmpty = false;   

            h->size = h->size+1;
        }
    }
}


HashTable* hashtable_init(int nbuckets, TInfo TInfoArray[], int nValues) {
    HashTable* hashtable = hashtable_create(nbuckets);

    if (hashtable == NULL) {
        return NULL;
    }

    for (int i = 0; i < nValues; i++) {
        hashtable_insert(hashtable, TInfoArray[i].key, TInfoArray[i].value);
    }

    return hashtable;
}

void print_all_key_value(HashTable* h) {
    if (h != NULL) {
        for (int i = 0; i < h->nbuckets; i++) {
            if (!h->bucket[i].isEmpty) {
                printf("La coppia chiave-valore è: %d %d e si trova all'indice %d\n", h->bucket[i].key, h->bucket[i].value, i);
            }
        }
    }
}



int main(void) {

    TInfo entries[] = {
        { 0, 11 },
        { 1, 21 },
        { 2, 12 },
        { 3, 4 },
        { 5, 1 },
    };

    HashTable* newHashTable = hashtable_init(3, entries, 5);

    printf("Capacity: %d - Size: %d\n", newHashTable->nbuckets, newHashTable->size);

    print_all_key_value(newHashTable);
    
    return 0;
}
