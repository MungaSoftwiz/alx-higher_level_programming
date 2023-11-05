#include "lists.h"

/**
 * is_palindrome - function checks if a linked list is a palindrome
 * @head: a pointer to the head of the list
 *
 * Return: 1 if it's a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;

	/* find the middle */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	/* reverse the second half */
	slow = reverse_listint(slow);
	fast = *head;

	/* start comparing one by one */
	while (slow != NULL)
	{
		if (fast->n != slow->n)
			return (0);

		fast = fast->next;
		slow = slow->next;
	}
	return (1);
}

/**
 * reverse_listint - function that reverses a listint_t linked list.
 * @head: a pointer to the first node in the list.
 *
 * Return: a pointer to the first node of the reversed linked list.
 */

listint_t *reverse_listint(listint_t *head)
{
	listint_t *prev_node, *next_node;

	next_node = NULL;
	prev_node = NULL;
	while (head != NULL)
	{
		next_node = head->next;
		head->next = prev_node;
		prev_node = head;
		head = next_node;
	}
	return (prev_node);
}
