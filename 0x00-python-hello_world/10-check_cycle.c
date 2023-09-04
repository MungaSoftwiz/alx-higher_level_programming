#include "lists.h"

/**
 * check_cycle - check for singly linked list
 * @list: the list to check for a cycle
 *
 * Return: 0 - no cycle, 1 - for cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	tortoise = list;
	hare = list;

	if (list == NULL)
		return (0);
	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
			return (1);
	}

	return (0);
}
