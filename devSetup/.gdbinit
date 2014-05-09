1. Print a Linkedlist
=====================
struct node {
    data_t data;
    node_t *next;
};

typedef struct {
    node_t *head;
    node_t *foot;
    node_t *curr;   // for iterator
    unsigned int size;
} list_t;

Scripts :::
define plist
  set var $n = $arg0->head
  while $n
    printf "%d ", $n->data
    set var $n = $n->next
  end
end

(gdb) plist myList
