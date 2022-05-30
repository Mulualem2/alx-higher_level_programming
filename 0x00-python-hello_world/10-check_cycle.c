#include "lists.h"
/**
* check_cycle - function that checks if the linked list has cycle
* @list: pointer
* Return: 1 if it have cycle, else 0
*/
int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (!list)
	{
		return (0);
	}

	while (list)
	{
		temp = list;
		list = list->next;

		if (temp <= list)
		{
			return (1);
		}
	}
	return (0);
}
