#include "lists.h"

/**
 * check_cycle - Entry Point
 *
 * Description: This function checks if there is a cycle in a singly linked
 * list
 *
 * @list: head pointer of the list
 *
 * Return: 1 if cycle exists, 0 otherwise
 */


int check_cycle(listint_t *list)
{
	listint_t *tortoise = NULL;
	listint_t *hare = NULL;

	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = list;
	hare = list->next;

	while (hare != NULL && hare->next != NULL)
	{
		if (tortoise == hare)
			return (1);

		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	return (0);
}
