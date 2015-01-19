#include "common.h"
// Program to rotate a linked list counter clock wise
#include<stdio.h>
#include<stdlib.h>
/* Link list node */
struct node{
    int data;
    struct node* next;
};
/* UTILITY FUNCTIONS */
/* Function to push a node */
void push (struct node** head_ref, int new_data){
    struct node* new_node =   (struct node*) malloc(sizeof(struct node));
    new_node->data  = new_data;
    new_node->next = (*head_ref);
    (*head_ref)    = new_node;
}
 
/* Function to print linked list */
void printList(struct node *node){
    while (node != NULL) {
        printf("%d  ", node->data);
        node = node->next;
    }
}
void rotate (struct node **head_ref, int k);

/* Drier program to test above function*/
int main(void){
    struct node* head = NULL; 
    
    // create a list 10->20->30->40->50->60
    for (int i = 60; i > 0; i -= 10)
        push(&head, i);
 
    printf("Given linked list \n");
    printList(head);
    rotate(&head, 2);
 
    printf("\nRotated Linked list \n");
    printList(head);
 
    return (0);
}

void rotate (struct node **head_ref, int k)
{
     if (k == 0) return;
    struct node* current = *head_ref;
    int count = 1;
    while (count < k && current != NULL) {
        current = current->next;
        count++;
    } 
    if (current == NULL)
        return;
 
    struct node *kthNode = current;
    while (current->next != NULL)
        current = current->next;
 
    current->next = *head_ref;
    *head_ref = kthNode->next;
    kthNode->next = NULL;
}
 