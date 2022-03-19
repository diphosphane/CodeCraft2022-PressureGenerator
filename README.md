# CodeCraft2022-PressureGenerator
a pressure data generator made for CodeCraft-2022 华为CodeCraft2022数据压测生成器

## Usage: 用法:
```bash
python3 data_gen.py [data_path]
```
All data will generated at path "data_path".  `data_path` is optional, if not specified, **pressure_data** will be used.  
所有数据会生成在“data_path”中。该参数是可选的，如果没有指定，将使用**pressure_data**.  


Attached a pressure=0.6 data.
附赠了个压力0.6的数据。  

If you can pass the test, but can not pass the online test, then it would be the problem of your program, you can try to generate pressure test data, then use the data that can not pass to debug.  
如果你可以通过判题器的测试，但却无法通过线上测试，那么你可以尝试着使用压测程序生成数据，使用无法通过测试的数据进行debug。  

## benchmark 判题器  
benchmark is avail at [here](https://github.com/diphosphane/CodeCraft2022-benchmark).  
判题器可在[这](https://github.com/diphosphane/CodeCraft2022-benchmark)下载到。  
