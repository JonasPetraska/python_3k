#include <Python.h>

bool isPrime(int n)
{
    // Edge case
    if (n <= 1)
        return false;

    // Check from 2 to n-1 
    for (int i = 2; i < n; i++)
        if (n % i == 0)
            return false;

    return true;
}

static PyObject* error;

static PyObject* py_isPrime(PyObject* self, PyObject* args)
{
    int input;

    if (!PyArg_ParseTuple(args, "i", input)) {
        PyErr_SetString(error, "Invalid input: param has to be an integer");
        return NULL;
    }

    return Py_BuildValue("O", isPrime(input));
}

static PyMethodDef primeModuleMethods[] = {
    {"IsPrime", (PyCFunction)py_isPrime, METH_VARARGS, "Checks if a given number is a prime"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef primeModule = {
    PyModuleDef_HEAD_INIT,
    "PrimeModule",
    "Prime Module",
    -1,
    primeModuleMethods
};

PyMODINIT_FUNC PyInit_PrimeModule(void)
{
    PyObject* mod = PyModule_Create(&primeModule);
    anagramError = PyErr_NewException("PrimeModule.error", NULL, NULL);
    Py_INCREF(error);
    PyModule_AddObject(mod, "error", error);
    return mod;
}