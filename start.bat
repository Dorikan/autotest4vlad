@echo off
echo Starting process...
echo.
:begin
behave -i everything.feature
timeout /t 1800 /nobreak > NUL
goto begin