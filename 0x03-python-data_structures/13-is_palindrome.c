#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverses the second half of the linked list
 * @head: pointer to head of the linked list
 * Return: pointer to the head of the reversed second half
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
 * compare_lists - compares two linked lists
 * @head1: pointer to the head of the first linked list
 * @head2: pointer to the head of the second linked list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n != temp2->n)
			return 0;
		temp1 = temp1->next;
		temp2 = temp2->next;
	}

	if (temp1 == NULL && temp2 == NULL)
		return 1;

	return 0;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return 1;

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *second_half = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		second_half = slow->next;
	}
	else
	{
		second_half = slow;
	}

	prev_slow->next = NULL;

	second_half = reverse_list(second_half);

	int result = compare_lists(*head, second_half);

	second_half = reverse_list(second_half);

	if (fast != NULL)
	{
		prev_slow->next = slow;
		slow->next = second_half;
	}
	else
	{
		prev_slow->next = second_half;
	}

	return result;
}

