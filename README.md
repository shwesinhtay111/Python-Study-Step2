Python-Study-Step2
==================
Error Handling
==============
    try:
     You do your operations here...
     ...
    except ExceptionI:
       If there is ExceptionI, then execute this block.
    except ExceptionII:
       If there is ExceptionII, then execute this block.
       ...
    else:
       If there is no exception then execute this block. 
     
 Finally
 =======
    try:
     Code block here
     ...
     Due to any exception, this code may be skipped!
    finally:
       This code block would always be executed.

Build-In Functions
==================
    - Map
    ----
        map(function, iterable, ...)
        - map() returns an iterator - that is, map() returns a special object that yields one result at a time as needed
        - map() with multiple iterables, map() can accept more than one iterable. 
        - The iterables should be the same length - in the event that they are not, map() will stop as soon as the shortest iterable is exhausted.
