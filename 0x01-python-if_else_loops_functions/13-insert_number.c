#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - insert the new node based on the sorting order.
 * @head: a pointer to the head of the linked list.
 * @number: the number to be inserted.
 * Return: returns the address of the new node or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *active = *head;

	new_node = (listint_t *)malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		while (active->next != NULL && active->next->n < number)
		{
			active = active->next;
		}
		new_node->next = active->next;
		active->next = new_node;
	}
	return (new_node);
}

