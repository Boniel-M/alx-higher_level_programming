#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - Prints basic info about Python lists
 * @p: Pointer to the Python object
 */
void print_python_list(PyObject *p) {
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++) {
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = item->ob_type->tp_name;

		printf("Element %ld: %s\n", i, typeName);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: Pointer to the Python object
 */

void print_python_bytes(PyObject *p) {
	Py_ssize_t size = PyObject_Length(p);
	Py_ssize_t i;
	char *bytes;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p)) {
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyUnicode_AsUTF8AndSize(p, &size) ? "yes" : "no");

	bytes = PyBytes_AsString(p);

	printf("  first %ld bytes:", size <= 10 ? size : 10);
	for (i = 0; i < (size <= 10 ? size : 10); i++) {
		printf(" %02hhx", bytes[i]);
	}
	printf("\n");
}
