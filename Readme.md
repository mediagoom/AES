### GYP AES

## Linux

In order to build and install in linux:

```bash
./configure
make
sudo make install
```

## Windows VS 2008

```powershell
$env:GYP_MSVS_VERSION=2008

set-alias msb4 C:\Windows\Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe




gyp aes.gyp --depth 0 -D target_arch=ia32 -D host_arch=ia32 -I.\gyp2008.gypi

msb4 aes.sln /p:Configuration=Debug /p:Platform=Win32 
msb4 aes.sln /p:Configuration=Release /p:Platform=Win32 

rm Release -force
rm Debug -force

gyp aes.gyp --depth 0 -D target_arch=x64 -D host_arch=x64 -I.\gyp2008.gypi

```
