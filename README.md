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
    Map
    ----
        map(function, iterable, ...)
        - map() returns an iterator - that is, map() returns a special object that yields one result at a time as needed
        - map() with multiple iterables, map() can accept more than one iterable. 
        - The iterables should be the same length - in the event that they are not, map() will stop as soon as the shortest iterable is exhausted.
    Reduce
    -------
        reduce(function, sequence) 
        -If seq = [ s1, s2, s3, ... , sn ], calling reduce(function, sequence) works like this:
            At first the first two elements of seq will be applied to function, i.e. func(s1,s2)
            The list on which reduce() works looks now like this: [ function(s1, s2), s3, ... , sn ]
            In the next step the function will be applied on the previous result and the third element of the list, i.e. function(function(s1, s2),s3)
            The list looks like this now: [ function(function(s1, s2),s3), ... , sn ]
            It continues like this until just one element is left and return this element as the result of reduce()
     Filter
     -----
         filter(function, list)
         -return a Boolean value (either True or False)
       
    
        
