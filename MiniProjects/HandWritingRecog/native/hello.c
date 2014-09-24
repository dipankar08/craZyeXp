#include <Python.h>
//#include "DrawBlock.h"
#include <stdio.h>      /* printf, fgets */
#include <stdlib.h>

#define MAX_X 50
#define MAX_Y 50

PyObject* hello(PyObject* self)
{
    printf("Hello world!\n");
    Py_RETURN_NONE; 
}

static PyObject* tpp(PyObject* self, PyObject* args)
{
  PyObject* obj;
  PyObject* seq;
  int i, len; 
  PyObject* item;
  
  if (!PyArg_ParseTuple(args, "O", &obj)){
    printf("Item is not a list\n");
    return NULL;
  }
  
  seq = PySequence_Fast(obj, "Error: Expected a sequence");
  len = PySequence_Size(obj);
  
  int *data =(int *) malloc(sizeof(int)*len);
  for (i = 0; i < len; i++) {
    item = PySequence_Fast_GET_ITEM(seq, i);
 	data[i] = (int)PyInt_AsLong(item);
  }

  for( i=0;i<len;i++){ printf("%d, ",data[i]);}
#if 0 
  int matrix[MAX_X][MAX_Y];
  for(int i=0;i<  MAX_X;i++)
    for(int j=0;j< MAX_Y;j++)
      matrix[i][j]=0;
  for(i=0;i< len ;i++)
       matrix[data[i]%MAX_X][data[i]/MAX_X]=1;
	   
  run(0, 0, (int**)matrix);
#endif 
  Py_DECREF(seq);
  Py_RETURN_NONE;
}


static PyMethodDef functions[] = {
    {"hello",    (PyCFunction)hello, METH_NOARGS},
    { "init", (PyCFunction)tpp, METH_VARARGS, "[1,2,3,4,5]" },
    {NULL, NULL, 0, NULL},
};

DL_EXPORT(void)
init_hello(void)
{
    Py_InitModule("_hello", functions);
}
