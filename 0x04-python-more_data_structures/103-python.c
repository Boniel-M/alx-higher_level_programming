#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	size = PyList_Size(p);
	for (i = 0; i < size; i++) {
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

void print_python_bytes(PyObject *p) {
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p)) {
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  [.] Size: %ld\n", PyBytes_Size(p));
	printf("  [.] Trying string: %s\n", PyBytes_AsString(p));

	size = PyBytes_Size(p);
	if (size > 10)
		size = 10;

	printf("  [.] first %ld bytes: ", size);
	str = PyBytes_AsString(p);
	for (i = 0; i < size; i++) {
		printf("%02x", (unsigned char)str[i]);
		if (i != size - 1)
			printf(" ");
	}
	printf("\n");
}


