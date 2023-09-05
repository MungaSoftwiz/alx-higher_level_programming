#include "lists.h"

/**
 * insert_node - inser a number into a sorted linked list
 * @head: the head othe node
 * @number: the digit to be inserted
 *
 * Return: address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insert, *current, *previous;

	insert = malloc(sizeof(listint_t));
	if (insert == NULL)
			return (NULL);
	insert->n = number;
	insert->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		insert->next = *head;
		*head = insert;
		return (insert);
	}

	current = *head;
	while (current != NULL)
	{
		if (number < current->n)
		{
			insert->next = current;
			previous->next = insert;
			break;
		}
		previous = current;
		current = current->next;
	}
	previous->next = insert;
	return (insert);
}
