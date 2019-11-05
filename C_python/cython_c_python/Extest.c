#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Python.h"
 
int fac(int n)
{
	if (n < 2)
		return 1;
	return n* fac(n-1);
}
 
char *reverse(char *s)
{
	register char t,
		*p = s,
		*q = (s + (strlen(s) - 1));
 
	while (s && p < q)
	{
		t = *p;
		*p++ = *q;
		*q-- = t;
	}
	return s;
}
 
int test()
{
	char s[1024] = {0};
	printf("4! == %d\n", fac(4));
	printf("8! == %d\n", fac(8));
	printf("12! == %d\n", fac(12));
	strncpy(s, "abcdef", 1024);
	printf("reversing 'abcdef', we get '%s'\n", reverse(s));
	strncpy(s,"madam", 1024);
	printf("reversing 'madam', we get '%s'\n", reverse(s));
	return 0;
}
 
static PyObject* Extest_fac(PyObject *self, PyObject *args)
{
	int num;
	if (!PyArg_ParseTuple(args, "i", &num))
	{
		return NULL;
	}
	return (PyObject*)Py_BuildValue("i", fac(num));
}
 
static PyObject* Extest_doppel(PyObject *self, PyObject *args)
{
	char *orig_str;
	char *dupe_str;
	PyObject *retval;
	if (!PyArg_ParseTuple(args, "s", &orig_str))
	{
		return NULL;
	}
	
	retval = (PyObject*)Py_BuildValue("ss", orig_str, dupe_str=reverse(strdup(orig_str)));
	free(dupe_str);
	return retval;
}
 
static PyObject* Extest_test(PyObject *self, PyObject *args)
{
	test();
	return (PyObject*)Py_BuildValue("");
}
 
static PyMethodDef ExtestMethods[] =
{
	{"fac", Extest_fac, METH_VARARGS, "fac func"},
	{"doppel", Extest_doppel, METH_VARARGS, "reverse str"},
	{"test", Extest_test, METH_VARARGS, "test func"},
	{NULL, NULL, 0, NULL},
};
 
static struct PyModuleDef ExtestMoudle =
{
	PyModuleDef_HEAD_INIT,
	"Extest",
	NULL,
	-1,
	ExtestMethods
};
 
void PyInit_Extest()
{
    PyModule_Create(&ExtestMoudle);
}
