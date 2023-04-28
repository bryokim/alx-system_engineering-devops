#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>


/**
 * infinite_while - Infinite while loop.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - Entry point.
 *
 * Return: Always 0.
 */
int main(void)
{
	int i;
	pid_t child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == -1)
			return (1);
		if (child_pid == 0)
			return (0);
	}

	i = infinite_while();

	return (i);
}
