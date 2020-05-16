#include <Python.h>
#include <stdbool.h>

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

static PyObject* primeError;

static PyObject* isPrimePy(PyObject* self, PyObject* args)
{
	int n;
	if (!PyArg_ParseTuple(args, "i", &n)) {
		PyErr_SetString(primeError, "Please input a number.");
		return NULL;
	}

	return Py_BuildValue("i", isPrime(n));
}

static PyMethodDef primeModuleMethods[] = {
	{"isPrime", (PyCFunction)isPrimePy, METH_VARARGS, "Tells whether the given numbers is a prime or not."},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef primeModule = {
	PyModuleDef_HEAD_INIT,
	"primeModule",
	"Prime module",
	-1,
	primeModuleMethods
};

PyMODINIT_FUNC PyInit_primeModule(void)
{
	PyObject* mod = PyModule_Create(&primeModule);
	primeError = PyErr_NewException("primeModule.error", NULL, NULL);
	Py_INCREF(primeError);
	PyModule_AddObject(mod, "error", primeError);
	return mod;
}