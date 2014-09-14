/************************
 This basicaly the caller C++ function which calls java functions.
 1. We have created similar struct as in java student class here.
 2. We wrote a function, create_vm which can get the JVM env, used to call Java
 3. Get the calss and method
 4. use this metoda nd class to call the func
 5. At end Distoty the vm.


 *************************/
//#include "StdAfx.h"
#include <stdio.h>
#include <jni.h>
#include <string.h>

#define PATH_SEPARATOR ';' /* define it to be ':' on Solaris */
#define USER_CLASSPATH "." /* where Prog.class is */

struct Student
{
	char name[100];
	int roll;
}Student;

/* get the Java env */
JNIEnv* create_vm(JavaVM ** jvm) {

    JNIEnv *env;
    JavaVMInitArgs vm_args;
    JavaVMOption options;
    options.optionString = "-Djava.class.path=D:\\Java Src\\TestStruct"; //Path to the java source code
    vm_args.version = JNI_VERSION_1_6; //JDK version. This indicates version 1.6
    vm_args.nOptions = 1;
    vm_args.options = &options;
    vm_args.ignoreUnrecognized = 0;

    int ret = JNI_CreateJavaVM(jvm, (void**)&env, &vm_args);
    if(ret < 0)
    	printf("\nUnable to Launch JVM\n");
	return env;
}

int main(int argc, char* argv[])
{
	/* Step 1: get the Env */
	JNIEnv *env;
	JavaVM * jvm;
	env = create_vm(&jvm);
	if (env == NULL)
		return 1;

    /* Step 2.  getting the classes */
    jclass ClsR= env->FindClass("RJNI");
    jclass clsS = env->FindClass("Student");
    if (ClsR == NULL){ printf("ClsR: NullValue");retun;}
    if (clsS == NULL){ printf("ClsS: NullValue");retun;}

    /* Step 3. Getting the Methds */
    jmethodID m_main = env->GetStaticMethodID(ClsR, "main", "([Ljava/lang/String;)V");
    jmethodID m_takeString = env->GetStaticMethodID(ClsR,"takeString","(Ljava/lang/String;)V");
    jmethodID m_takeObj = env->GetStaticMethodID(ClsR,"takeObj","(LStudent;)I") ;
    jmethodID m_takeObjArr = env->GetStaticMethodID(ClsR,"takeObjArr","([LStudent;)V");
	jmethodID m_returnObj = env->GetStaticMethodID(ClsR,"returnObj","()Ljava/lang/Object;");

    jmethodID m_student_init = env->GetMethodID(clsS, "<init>", "(ILjava/lang/String;Ljava/lang/String;I)V");;

	/************************************************************************/
	/* Step 4. Now we will call the functions using the their method IDs			*/
	/************************************************************************/

	if(m_main != NULL)
		env->CallStaticVoidMethod(clsH, m_main, NULL); //Calling the main method.

	if (m_takeString!=NULL)
	{
		jstring StringArg = env->NewStringUTF("\nThis String from C++\n");
		env->CallStaticVoidMethod(clsH,m_takeString,StringArg);
	}

	jobject jobjDet = NULL;
	if (m_takeObj!=NULL)
	{
		if(clsS != NULL && m_student_init != NULL)
		{
			jstring StringArgName = env->NewStringUTF(s.name);
			jobject jobjDet = env->NewObject(clsS, m_student_init,StringArgName, (jint)s.roll);
		}

		if(jobjDet != NULL)
			env->CallStaticIntMethod(clsH,m_takeObj,jobjDet);
	}

	jobjectArray jobjArr = NULL;
	if (m_takeObjArr !=NULL)
	{
		if(clsS != NULL && m_student_init != NULL)
		{
			//Creating the Object Array that will contain 2 structures.
			jobjArr = (jobjectArray)env->NewObjectArray(2,clsS,
					                                      env->NewObject(clsS,m_student_init ,env->NewStringUTF("CPP1"),(jint)1));
			//Initializing the Array
			for(int i=0;i<2;i++)
			{
				env->SetObjectArrayElement(jobjArr,i,env->NewObject(clsS, m_student_init,env->NewStringUTF("CPP"),(jint)1));
			}
		}
		//Calling the Static method and passing the Structure array to it.
		if(jobjArr != NULL && m_takeObjArr != NULL)
			env->CallStaticVoidMethod(clsS,m_takeObjArr,jobjArr);
	}


	//Calling a Static function that return an Object
	jobject jobjRetData = NULL;
	if (m_returnObj != NULL)
	{
		//Calling the function and storing the return object into jobject type variable
		//Returned object is basically a structure having two fields (string and integer)
		jobjRetData = (jobject)env->CallStaticObjectMethod(clsS,m_returnObj,NULL);

		//Get the class of object
		clsS = env->GetObjectClass(jobjRetData);

		//Obtaining the Fields data from the returned object
		jint ret_roll = env->GetIntField(jobjRetData,env->GetFieldID(clsS,"roll","I"));
		jstring ret_name = (jstring)env->GetObjectField(jobjRetData,env->GetFieldID(clsR,"name","Ljava/lang/String;"));
		const char *name = env->GetStringUTFChars(ret_name,0);

		printf("\n\nValues Returned from Object are:\nreturnValue=%d\nLog=%s",ret_roll,name);
		//After using the String type data release it.
		env->ReleaseStringUTFChars(ret_name,ret_roll);
	}


	// Step 5. Release resources.
	int n = jvm->DestroyJavaVM();
    return 0;
}
