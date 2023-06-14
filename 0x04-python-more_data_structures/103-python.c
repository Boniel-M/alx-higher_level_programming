#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: Pointer to the Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = PyList_Size(p);  /* Get the size of the list */
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);  /* Get the item at index i */
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: Pointer to the Python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *data;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);  /* Get the size of the bytes object */
	data = PyBytes_AsString(p);  /* Get a pointer to the data */

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", data);

	if (size > 10)
		size = 10;  /* Limit printing to first 10 bytes */

	printf("  first %ld bytes:", size);
	for (i = 0; i < size; i++)
		printf(" %02x", (unsigned char)data[i]);
	printf("\n");
}

