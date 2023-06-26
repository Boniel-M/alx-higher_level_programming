#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid PyListObject\n");
		fflush(stdout);
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid PyBytesObject\n");
		fflush(stdout);
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  [.] size: %ld\n", size);
	printf("  [.] trying string: %s\n", string);

	if (size > 10)
		size = 10;

	printf("  [.] first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02x", (unsigned char)string[i]);
		if (i + 1 < size)
			printf(" ");
	}
	printf("\n");
}

void print_python_float(PyObject *p)
{
	PyFloatObject *float_obj = (PyFloatObject *)p;
	double value;

	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid PyFloatObject\n");
		fflush(stdout);
		return;
	}

	value = float_obj->ob_fval;
	printf("[.] float object info\n");
	printf("  [.] value: %f\n", value);
}

