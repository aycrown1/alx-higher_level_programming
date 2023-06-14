#include <stdlib.h>
#include "lists.h"
/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to the head of the list
 *
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *temp;
    int palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return palindrome;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        temp = slow;
        slow = slow->next;
        temp->next = prev;
        prev = temp;
    }

    if (fast != NULL)
        slow = slow->next;

    while (prev != NULL)
    {
        if (prev->n != slow->n)
        {
            palindrome = 0;
            break;
        }
        prev = prev->next;
        slow = slow->next;
    }

    temp = NULL;
    while (*head != NULL)
    {
        temp = (*head)->next;
        free(*head);
        *head = temp;
    }

    return palindrome;
}

