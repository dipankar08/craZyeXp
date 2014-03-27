====================================================
Introduction to Ring-buffer in ZebOS.
====================================================

1. Introduction : Performance improvement of logging using ring buffer.

  ZebOS provide a number of ways of doing logging protocol activities, but most of them have some performance impacts due to expensive I/O operation. Here, we introduce a in-memory logging facility using ring buffer. A ring buffer or cyclic buffer, is a data structure that uses a single, fixed-size buffer as if it were connected end-to-end. This structure lends itself easily to buffering data streams.

2. Technical Overview

    2.1 Ring Buffer File Location/file information:
    
        Ring buffer code is the part of lib, located in lib/ringbuf/.  The following file are added to support this :
        - mythbaseexp.h
        - mythlogging.h
        - pes.c
        - pes.h
        - ringbuffer.c
        - ringbuffer.h

        Other File Changes:
        -lib/lib.h
        -lib/log.c - Perform actual ring_write operation and CLI Installation
        -lib/log.h - Adding prams ringbuf_severity and adding ZLOG_RINGBUF as 0x16 
     

    2.2 Ring Buffer Structure
    
        #define RING_SIZE  10000 /* This is global ring size to 10k Byte */
        #define EMPTY_BUFFER  -1000
                typedef struct ringbuffer {
                        int read_pos;
                        int write_pos;
                        uint32_t size;
                        uint8_t *buffer;
                } ringbuffer;

    2.2 Ring Buffer API support 

        Ring buffer support following API for different operations, listed as below: 
        --------------------------------------------------------------------------------------------
        int  ring_init (ringbuffer *rbuf, int size); /* Use to initialize the ring -buffer */
        char * ring_dump(ringbuffer *rbuf);/* Use to dump ring -buffer content */
        int  ring_reinit (ringbuffer *rbuf, int size);/* Use to re initialize the ring -buffer with a new size */
        void ring_clear(ringbuffer *rbuf); /* clear ring -buffer content */
        void ring_destroy(ringbuffer *rbuf); /* Remove ring -buffer instance */
        int ring_write(ringbuffer *rbuf, uint8_t *data, int count); /* write to  ring -buffer  */
        int ring_read(ringbuffer *rbuf, uint8_t *data, int count); /* read from  ring -buffer  */
        ----------------------------------------------------------------------------------------------
        
    2.3 How to add Ring buffer facility to any protocol
        Adding the ring-buffer facility is just a simple 3 steps: 
        Step1: You can define protocol specific Ring Buffer, like #Define RING_SIZE 1000
        Step2: initialize ring buffer in globals_init function, for example:
              #ifdef HAVE_RINGBUF
              struct ringbuffer *new1;
              new1 = XCALLOC (MTYPE_RB, sizeof (struct ringbuffer));
              pal_mem_set (new1, 0, sizeof (struct ringbuffer));
              zg->rb = new1;
              ring_init(zg->rb,RING_SIZE);
              #endif /* HAVE_RINGBUF */
        Step3: Installation <dmesg> and <dmesg clear> CLI for that protocol in _cli.c file.   

        
3. CLI/Configuration Guide

    3.0. Configuration and Flags
    All ring buffer codes is under HAVE_RINGBUF Flag. To enable ring-buffer, you need to add <--enable-ringbuf \> in your configuration file. Please do a <make clean;make all> after this changes.

    3.1 Enable Ring-buffer logging
    CLI: logging ringbuf <0-7>|
    MODE:CONFIG_MODE
    USES: enable ring-buffer logging.

    3.2 Disable Ring-Buffer Logging
    CLI: no logging ringbuf
    MODE:CONFIG_MODE
    USES: disable ring-buffer logging.

    3.3 Show Ring-buffer messages
    CLI: dmesg <Protocol name>
    MODE:EXEC_MODE
    USES: Show Ring buffer content for a protocol.
    Example: dmesg lldp

    3.4 Clear Ring-buffer Message.
    CLI: dmesg <Protocol name> clear
    MODE:EXEC_MODE
    USES: Clear Ring-buffer content for that protocol.
    Example: dmesg lldp clear


4. Performance Analysis:

    We also measured the performance improvement of using ring-buffer, which can be summarize as below:
    ---------------------------------------------------------------------------------------------
    Parameters	 |  Using exiting VZlog(ns) | 	  Using Ring Buffer(ns) | 	With No VZlog/Empty loop(ns)
    tstart	$3 = {tv_sec = 563, tv_nsec = 684576587}	$3 = {tv_sec = 615330, tv_nsec = 549335107}	$6 = {tv_sec = 616330, tv_nsec = 96013682}
    tend	$4 = {tv_sec = 566, tv_nsec = 860543087}	{tv_sec = 615330, tv_nsec = 556887039}	{tv_sec = 616330, tv_nsec = 96014330}
    Time taken  to execute  Full Block(include for loop)	(566*10^9 + 860543087) - (563*10^9 +684576587) 	7551932 NS	( 96014330- 96013682) = 648

    Time Taken only by Vzlog func	=3175965852	7551932 – 648 =7551284	                 
    Percentage of Improvement 	(3175965852- 7551284 )  /  3175965852* 100 = 99.76 %
    ------------------------------------------------------------------------------------------------





