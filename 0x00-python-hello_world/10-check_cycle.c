#include "lists.h"
/**
 * check_cycle - determines whether the linked list has a cycle or not.
 * @list: pointer to the head of a singly linked list.
 * Return: returns an integer value.
 * The function uses the Floyd's cycle-finding algorithm.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	/* Traverse the list using the slow and fast pointers */
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		/* If there is a cycle, the both pointers will meet at some point */
		if (slow == fast)
		{
			return 1; /* therefore, Cycle detected */
		}
	}
	return 0; /* otherwise, No cycle detected */
}

