# pygrep

Filter input similar to grep.

There are a lot of options for conditional grep inputs.  You can see them here...

http://web.archive.org/web/20210129003513/https://www.thegeekstuff.com/2011/10/grep-or-and-not-operators/


I find these to be generally decent.  However, I often need the same capabilites on Windows.  Additionally, 


One of the issues with grep is that it is difficult to create complex or compund sets of filters.  In my 
cpp project [alf](https://github.com/zkSNARK/alf), I solve this problem by giving users the ability to 
create complext and nested sets of input filters using algebraic expressions.  This project here is a 
far more simplified version (currently) which only works as a 'additive' requirement set.  

The syntax is simple ...

python3 pygrep.py infile.txt filter1 filter 2 -o outfile.txt

In the above line, the lines in 'infile.txt. will be filtered so that only lines that contain the strings
'filter1' AND 'filter2' will be sent to outfile.txt.


In the future I would like to convert this program to a python version of the ALF project mentioned above, 
or potentially just make it into a grep copy that exists in python. At that point, the project would still
be meaningful because it would be cross platform, and would be able to be used programatically within 
python modules. 
