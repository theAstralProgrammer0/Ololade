#include <Python.h>
#define PY_UNICODE_TYPE wchar_t

/**
 * print_python_string - Entry Point
 *
 * Description: This is a function that uses CPython API to display information
 * about a PyStringObject
 *
 * @p: PyStringObject pointer
 *
 * Return: Nothing
 */

void print_python_string(PyObject *p)
{
	const Py_UNICODE *unicode_str;
	Py_ssize_t unicode_len;

	fflush(stdout);
	printf("[.] string object info\n");

	if (PyUnicode_Check(p))
	{
		unicode_str = PyUnicode_AsUnicodeAndSize(p, &unicode_len);
		if (PyUnicode_IS_COMPACT_ASCII(p))
		{
			printf("  type: compact ascii\n");
		}
		else if (PyUnicode_IS_COMPACT(p))
		{
			printf("  type: compact unicode object\n");
		}
		printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
		printf("  value: %ls\n", unicode_str);
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
}
