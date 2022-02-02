## Bug identification

As recommended, we used the Microsoft [Restler](https://github.com/microsoft/restler-fuzzer) tool with the following output

```
Starting task Test...
Using python: 'python.exe' (Python 3.10.2)
Request coverage (successful / total): 6 / 6
No bugs were found.
Task Test succeeded.
Collecting logs...
```



To reproduce, we followed these steps:

1. Installed .NET 5.0

2. Downloaded the official repo
```sh
git clone https://github.com/microsoft/restler-fuzzer.git
cd restler-fuzzer
```

3. Created the folder for the Restler binaries
```sh
mkdir ../restler_bin
```

4. Built the Restler project
```sh
python3 ./build-restler.py --dest_dir ../restler_bin
```

5. Compile it
```sh
cd ../restler_bin
.\restler.exe compile --api_spec "C:\Facultate\Anul 3 Semestrul 1\KonnectedKars\openapi.json"
```

6. Run it
```sh
cd Compile

..\restler.exe test --grammar_file .\grammar.py --dictionary_file .\dict.json --settings engine_settings.json --no_ssl
```