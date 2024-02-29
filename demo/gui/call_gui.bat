@echo off
cls

set start_path=%cd%

set KEY_NAME="HKEY_CURRENT_USER\Software\xemax\python_portable"
set VALUE_NAME=pp_path
FOR /F "usebackq skip=2 tokens=1,2*" %%A IN (`REG QUERY %KEY_NAME% /v %VALUE_NAME% 2^>nul`) DO (
    set ValueName=%%A
    set ValueType=%%B
    set pp_path=%%C
)
if defined pp_path (
    echo start_path = %start_path%
	echo pp_path = %pp_path%
  
	call "%pp_path%\venv\Scripts\activate"
	"%pp_path%\venv\Scripts\streamlit.exe" run "%start_path%\gui.py"
	call "%pp_path%\venv\Scripts\deactivate"	
) else (
    echo %KEY_NAME%\%VALUE_NAME% not found
)

::pause