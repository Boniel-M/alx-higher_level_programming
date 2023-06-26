#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic information about a Python list object
 *
 * @p: Pointer to the PyObject representing the Python list
 *
 * Return: None
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyListObject *list;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = Py_SIZE(list);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object
 *
 * @p: Pointer to the PyObject representing the Python bytes
 *
 * Return: None
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	PyBytesObject *bytes;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = Py_SIZE(bytes);

	printf("[.] Bytes object info\n");
	printf("  Size: %zd\n", size);
	printf("  Trying string: %s\n", bytes->ob_sval);

	if (size > 10)
		size = 10;

	printf("  first %zd bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == size - 1)
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic information about a Python float object
 *
 * @p: Pointer to the PyObject representing the Python float
 *
 * Return: None
 */

void print_python_float(PyObject *p)
{
	PyFloatObject *float_obj;
	double value;

	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	float_obj = (PyFloatObject *)p;
	value = float_obj->ob_fval;

	printf("[.] Float object info\n");
	printf("  Value: %lf\n", value);
}
