# markplate
Python tool that automates writing markdown based on a callback

##### --temp  Jinja template file
##### --out  Output directory
##### --out-file  Output file, goes in output directory
##### --cb  python callbacks file see recursive_file_visit.py for example
##### --temp  Output directory where callbacks produce output


#### Example 
./markplate --temp leetcode.jinja --out ./../Leetcode/ --out-file README.md --cb ./callbacks/recursive_file_visit.py --ex-cb-dir ./../Leetcode --exclude [.git,.gitignore,README.md] -username cecinuga 