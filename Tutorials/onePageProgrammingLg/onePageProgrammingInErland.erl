%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%  Welcome to OnePageProgramming inErland 
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Ch 1. Basic of Erland 
	1.1 The  Erlang  shell -  is  where  you’ll  spend  most  of  your  time. 
	--------------------------------------------------------------------------
	$erl
	ErlangR16B...
	EshellV5.9 (abortwith^G)
	1> 123456*223344. % see at end it has a dot
	27573156864
	Note that each expression mustbe finished with a dot followed by a whitespace character. In this context, whitespace means a space, tab, or carriage return character.
	report erratum •discuss
	1.2 The = operator - We  can  assign  values  to  variables 
	--------------------------------------------------------------
	2> X=123.
	123
	3> X*2.
	246
	If we try to change the value of a variable, something strange happens: We  can’t rebind variables. try :
	4> X=999.
	** exceptionerror:no matchofrighthandsidevalue999
	= is not an assignment operator; it’s actually a pattern matching operator.	
	Note that Erlang variables start with uppercase characters. So, X, This, and A_long_name are  all  variables.
	Names  beginning  with  lowercase  letters—for example, mondayor friday—are not variables but are symbolic constants called atoms.
    1> abc=123.
	** exceptionerror:no matchofrighthandsidevalue123

	1.3 Processes, Modules, and Compilation
	-----------------------------------------------
	Processes evaluate  functions  that  are  defined  in  modules. 
	Modules  are  files  with  the extension .erl and must be compiled before they can be run.
	Having compiled a  module,  we  can  evaluate  the  functions  in  the  module  from  the  shell  or
	Ex: Compiling and Running “Hello World”in the Shell
	Make a file called hello.erl with the following content:
	hello.erl
	-module(hello).
	-export([start/0]).
	start()->
	io:format("Hello world~n").
	To compile and run this, we start the Erlang shell in the directory where we stored hello.erland do the following:
	$erl
	ErlangR16B...
	1> c(hello).
	{ok,hello}
	2> hello:start().
	Helloworld
	ok
	3> halt().
	$
	Compiling Outside the Erlang Shell
	$erlc hello.erl
	$erl-noshell-s hello start-s init stop
	Helloworld
	The compiler compiles the code in hello.erland produces an object code file called hello.beam.
	The $erl-noshell...command loads the module helloand evaluates the function hello:start().
	Running  the  Erlang  compiler  (erlc)  outside  the  Erlang  shell  is  the  preferred
