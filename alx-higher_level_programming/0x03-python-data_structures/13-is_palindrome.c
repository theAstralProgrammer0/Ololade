#include "lists.h"
#include <stdio.h>
void tte(listint_t** temp, listint_t* tail, int* ret)
{
	if (tail == NULL)
		return;
	tte(temp, tail->next, ret);
	if ((*temp)->n != tail->n)
	{
		*ret = 0;
	}
	*temp = (*temp)->next;
}


int is_palindrome(listint_t **head)
{
	listint_t **temp = NULL;
	listint_t *tail = NULL;
	int ret = 1; 

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	tail = *head;
	temp = head;
	tte(temp, tail, &ret);
	return (ret);
}
