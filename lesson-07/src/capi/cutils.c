#include <stdlib.h>
#include <stdio.h>

#include <Python.h>

int fibonacci(int n)
{
    if (n < 2)
        return 1;
    return fibonacci(n-2) + fibonacci(n-1);
}

PyObject* cutils_dummy(PyObject* self, PyObject* args)
{
    return Py_BuildValue("[i, i]", 100, 500);
}

PyObject* cutils_fibonacci(PyObject* self, PyObject* args)
{
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
    {
        printf("ERROR: Failed to parse argument");
        return NULL;
    }
    PyObject* result = NULL;
    result = Py_BuildValue("L", fibonacci(n));
    return result;
}

PyObject* cutils_accumulate(PyObject* self, PyObject* args)
{
    PyObject* result = NULL;
    if (!PyArg_ParseTuple(args, "O", &result))
    {
        printf("ERROR: Failed to parse argument");
        return NULL;
    }

    long len = PyList_Size(result);
    long res = 0;
    for (int i = 0; i < len; ++i)
    {
        PyObject *tmp = PyList_GetItem(result, i);
        res += PyLong_AsLong(tmp);
    }
    return Py_BuildValue("i", res);
}

static PyMethodDef methods[] = {
    { "accumulate", cutils_accumulate, METH_VARARGS, "sum of elements of the list"},
    { "fibonacci", cutils_fibonacci, METH_VARARGS, "return fibonacci number"},
    { "dummy", cutils_dummy, METH_NOARGS, "dummy function"},
    { NULL, NULL, 0, NULL}
};

static struct PyModuleDef cutils_module = {
    PyModuleDef_HEAD_INIT, "cutils",
    NULL, -1, methods
};

PyMODINIT_FUNC PyInit_cutils(void) {
    return PyModule_Create( &cutils_module );
}

