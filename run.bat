@echo off
call .venv\Scripts\activate.bat

:: Running only tests marked as smoke. Add or remove "rem" at the beggining of the line.
pytest -m -s -v "smoke" --html .\reports\report.html

:: Running only tests marked as regression. Add or remove "rem" at the beggining of the line.
rem pytest -m -s -v "regression" --html .\reports\report.html

:: Running all tests. Add or remove "rem" at the beggining of the line.
rem pytest -m -s -v "smoke and regression" --html .\reports\report.html

pause