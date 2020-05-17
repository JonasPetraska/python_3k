#include <Python.h>
#include <structmember.h>
#include <stdio.h>

typedef struct {
    PyObject_HEAD
    float x;
    float y;
} Point;

static PyObject* pointError;

static void Point_dealloc(Point* self) {
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject* Point_new(PyTypeObject* type, PyObject* args, PyObject* kwds)
{
    Point* self;

    self = (Point*)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->x = 1;
        self->y = 1;
    }

    return (PyObject*)self;
}

static int Point_init(Point* self, PyObject* args, PyObject* kwds)
{
    float tempX, tempY;
    if (!PyArg_ParseTuple(args, "ff", &tempX, &tempY))
        return -1;

    self->x = tempX;
    self->y = tempY;

    return 0;
}

//***********************************************************************************************************

static PyObject* Point_move(Point* self, PyObject* args)
{
    float tempX, tempY;
    if (!PyArg_ParseTuple(args, "ff", &tempX, &tempY)) {
        PyErr_SetString(pointError, "Points must be numbers.");
        return NULL;
    }

    self->x = tempX;
    self->y = tempY;

    return Py_None;
}

static PyObject* Point_str(Point* self) {
    char str1[20];
    char str2[20];
    sprintf(str1, "%.2f", self->x);
    sprintf(str2, "%.2f", self->y);
    return PyUnicode_FromFormat("x=%s, y=%s", str1, str2);
}

//***********************************************************************************************************

static PyMemberDef Point_members[] = {
    {"x", T_FLOAT, offsetof(Point, x), 0, "X coordinate of the point"},
    {"y", T_FLOAT, offsetof(Point, y), 0, "Y coordinate of the point"},
    {NULL}
};

static PyMethodDef Point_methods[] = {
    {"move", (PyCFunction)Point_move, METH_VARARGS, "Moves the point to X and Y coordinates."},
    {NULL}
};

//***********************************************************************************************************

static PyTypeObject PointType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "point.Point",             /* tp_name */
    sizeof(Point),             /* tp_basicsize */
    0,                         /* tp_itemsize */
    (destructor)Point_dealloc, /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_reserved */
    0,                         /* tp_repr */
    0,                         /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash  */
    0,                         /* tp_call */
    (reprfunc)Point_str,       /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,   /* tp_flags */
    "This is a point (X,Y)",        /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    Point_methods,             /* tp_methods */
    Point_members,             /* tp_members */
    0,           				/* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)Point_init,      /* tp_init */
    0,                         /* tp_alloc */
    Point_new,                 /* tp_new */
};

static struct PyModuleDef pointModule = {
  PyModuleDef_HEAD_INIT,
  "pointModule", // name of module
  "Point type", // module documentation, may be NULL
  -1, // size of per- interpreter state of the module, or -1 if the module keeps state in global variables. 
  NULL, NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC PyInit_pointModule(void) {
    PyObject* m;
    if (PyType_Ready(&PointType) < 0)
        return NULL;
    m = PyModule_Create(&pointModule);
    if (m == NULL)
        return NULL;
    Py_INCREF(&PointType);
    PyModule_AddObject(m, "Point", (PyObject*)&PointType);

    pointError = PyErr_NewException("point.error", NULL, NULL);
    Py_INCREF(pointError);
    PyModule_AddObject(m, "error", pointError);

    return m;
}
