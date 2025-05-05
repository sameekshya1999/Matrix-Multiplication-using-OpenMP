#include <Python.h>
#include "matrix.c"

static PyObject* multiply(PyObject* self, PyObject* args) {
    int n, use_openmp;
    double execution_time;

    if (!PyArg_ParseTuple(args, "ii", &n, &use_openmp)) {
        return NULL;
    }

    if (n <= 0) {
        PyErr_SetString(PyExc_ValueError, "Matrix size must be positive");
        return NULL;
    }

    multiply_matrices(n, use_openmp, &execution_time);

    return Py_BuildValue("{s:d}", "execution_time", execution_time);
}

static PyMethodDef MatrixMethods[] = {
    {"multiply", multiply, METH_VARARGS, "Multiply two nxn matrices and return execution time"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef matrixmodule = {
    PyModuleDef_HEAD_INIT,
    "matrix",
    NULL,
    -1,
    MatrixMethods
};

PyMODINIT_FUNC PyInit_matrix(void) {
    return PyModule_Create(&matrixmodule);
}