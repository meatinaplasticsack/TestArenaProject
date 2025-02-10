@echo off
call .venv\Scripts\activate.bat

:: Running only tests marked as smoke. Add or remove "rem" at the beggining of the line.
pytest -s -v -m "smoke" --html .\reports\report.html

:: Running only tests marked as regression. Add or remove "rem" at the beggining of the line.
rem pytest -s -v -m "regression" --html .\reports\report.html

:: Running all tests. Add or remove "rem" at the beggining of the line.
rem pytest -s -v -m "smoke and regression" --html .\reports\report.html

pause