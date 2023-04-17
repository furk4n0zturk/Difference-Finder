# Difference-Finder
Detects different contents in two files and prints them separately.

Note: The files you will compare must be in the same directory as `diffinder.py`

## Usage

When the contents of the files named file1 and file2 that we will compare are as follows;

file1 Content:
```
Hi
I'm
Furkan
Ozturk
```
file2 Content:
```
Hello
Furkan
Ozturk
I'm
Hacker
```
To see the different data between file1 and file2 files;
```
python3 diffinder.py file1 file2 
```
Output:
```
[+] IN First File NOT IN Second File

Hi

[+] IN Second File NOT IN First File

Hacker
Hello
```
