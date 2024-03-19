#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int h;
	PyListObject *objct = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", objct->allocated);
	for (h = 0; h < size; h++)
		printf("Element %i: %s\n", h, Py_TYPE(objct->ob_item[h])->tp_name);

}
