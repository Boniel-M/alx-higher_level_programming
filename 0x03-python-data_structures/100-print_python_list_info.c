#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject* p)
{
	PyListObject* list = (PyListObject*)p;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = list->allocated;
	Py_ssize_t i;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++) {
		PyObject* item = PyList_GetItem(p, i);
		const char* typeName = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", i, typeName);
	}
}
