@echo off
tasm\tasm /zd /zi %1.asm
if errorlevel 1 goto end
tasm\tlink /x /v %1
if errorlevel 1 goto end
del %1.obj
tasm\td %1.exe
:end