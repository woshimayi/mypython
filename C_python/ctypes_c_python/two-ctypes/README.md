###  编译C 成为so 动态库
``` bash
	gcc -shared -Wl,-soname,adder -o adder.so -fPIC add.c
```
