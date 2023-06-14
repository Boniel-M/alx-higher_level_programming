#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
	Py_ssize_t size, i;
	PyListObject *list;

	if (!PyList_Check(p)) {
		fprintf(stderr, "[ERROR] Invalid Python List\n");
		return;
	}

	list = (PyListObject *)p;
	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++) {
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, typeName);
	}
}

void print_python_bytes(PyObject *p) {
	Py_ssize_t size, i;
	unsigned char *bytes;

	if (!PyBytes_Check(p)) {
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (unsigned char *)PyBytes_AsString(p);
	size = PyBytes_Size(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first %ld bytes:", (size > 10) ? 10 : size);
	for (i = 0; i < ((size > 10) ? 10 : size); i++) {
		printf(" %02x", bytes[i]);
	}
	printf("\n");
}

