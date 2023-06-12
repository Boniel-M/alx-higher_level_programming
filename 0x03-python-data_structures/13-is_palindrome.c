#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to head of list
 * Return: pointer to the new head of the reversed list
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

	return prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return 1;

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *second_half = reverse_list(slow);
	listint_t *first_half = *head;

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
			return 0;
		first_half = first_half->next;
		second_half = second_half->next;
	}

	return 1;
}
