#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the linked list
 * Return: pointer to the head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *second_half = NULL;
	listint_t *prev_slow_ptr = *head;
	listint_t *mid_node = NULL;
	int is_palindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast_ptr != NULL && fast_ptr->next != NULL)
		{
			fast_ptr = fast_ptr->next->next;
			prev_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		if (fast_ptr != NULL)
		{
			mid_node = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		second_half = reverse_list(second_half);

		while (*head != NULL && second_half != NULL)
		{
			if ((*head)->n != second_half->n)
			{
				is_palindrome = 0;
				break;
			}
			*head = (*head)->next;
			second_half = second_half->next;
		}
		second_half = reverse_list(second_half);

		if (mid_node != NULL)
		{
			prev_slow_ptr->next = mid_node;
			mid_node->next = second_half;
		}
		else
			prev_slow_ptr->next = second_half;
	}

	return (is_palindrome);
}

