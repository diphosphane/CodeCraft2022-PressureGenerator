# CodeCraft2022-PressureGenerator
a pressure data generator made for CodeCraft-2022 华为CodeCraft2022压测数据及模拟数据生成器

## Usage: 用法:  
for debug usage:  Debug压测用法  
```bash
python3 data_gen_pressure.py [data_path]
```
for online data simulation:  在线数据模拟用法  
```bash
python3 data_gen_simulated.py [data_path]
```

All data will generated at path "data_path".  `data_path` is optional, if not specified, **pressure_data** or **simulated_data** will be used.  
所有数据会生成在“data_path”中。该参数是可选的，如果没有指定，将使用**pressure_data** 或 **simulated_data**。


Attached a pressure=0.6 debug pressure test data and pressure=0.3 online data simulated data.  
附赠了个debug用的压力0.6的数据 以及 线上数据模拟的压力为0.3的数据。    

If you can pass the test, but can not pass the online test, then it would be the problem of your program, you can try to generate pressure test data, then use the data that can not pass to debug.  
如果你可以通过判题器的测试，但却无法通过线上测试，那么你可以尝试着使用压测程序生成数据，使用无法通过测试的数据进行debug。  

## Attention 注意  
In some cases, you can pass through the official dataset, but may have unnexpected behavior at other data, so data_gen_pressure.py may help you debug.  
在某些情况下，你可以通过官方的线下数据，但可能会在其他数据中出现分配错误，在这种情况下，data_gen_pressure.py可以帮助到你。  

But if you want to simulate the official data, you should use data_gen_simulated.py. Because I can not know the data distribution online, so I can not ensure the data generated can accurately judge your program.  
但如果你想要模拟官方的数据，你应该使用data_gen_simulated.py。但因为我无法得知官方的数据分布，所以我也无法保证生成的数据能准确地评判你的程序。  
## benchmark 判题器  
benchmark is avail at [here](https://github.com/diphosphane/CodeCraft2022-benchmark).  
判题器可在[这](https://github.com/diphosphane/CodeCraft2022-benchmark)下载到。  

## Wechat Reward 微信打赏  
If you find this tool helpful, please consider buy me a cup of coffee.  
如果你觉得该工具有用，可以考虑打赏一杯咖啡。  
![打赏](img/reward.jpg)