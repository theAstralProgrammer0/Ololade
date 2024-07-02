#include "lists.h"

/**
 * insert_node - Entry Point
 *
 * Description: This function inserts a node at the correct position in a
 * sorted linked list
 *
 * @head: double pointer to head of linked list
 *
 * @number: Number member of the new node
 *
 * Return: (newnode) pointer to the newly inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL;
	listint_t *nextnode = NULL;
	listint_t *newnode = NULL;
	int count = 0;

	if (*head == NULL)
		return (add_nodeint_end(head, number));

	current = *head;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;

	while (current->n < number && current->next->n < number)
	{
		if (current->next->next == NULL)
			return (add_nodeint_end(head, number));
		current = current->next;
		++count;
	}
	if (count == 0)
	{
		newnode->next = *head;
		*head = newnode;
	}
	else
	{
		nextnode = current->next;
		current->next = newnode;
		newnode->next = nextnode;
	}
	return (newnode);
}

