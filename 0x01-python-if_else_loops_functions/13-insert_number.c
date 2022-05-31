#include <stdlib.h>
#include "lists.h"

/**
* insert_node - create node and insert to ssl
* @head: head of the list
* @number: number to be added in the nodes
* Return:  the address of the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!head || !(*head))
	{
		new_node->n = number;
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	node = *head;
	if (!new_node)
	{
		free(new_node);
		return (NULL);
	}
	if (number <= node->n)
	{
		new_node->n = number;
		new_node->next = node;
		node = new_node->next;
		*head = new_node;
		return (new_node);
	}
	while (node)
	{
		if (!node->next)
			return (add_nodeint_end(head, number));
		if ((number > node->n) && (number <= (node->next)->n))
		{
			new_node->n = number;
			new_node->next = node->next;
			node->next = new_node;
			return (new_node);
		}
		node = node->next;
	}
	free(new_node);
	return (NULL);
}
