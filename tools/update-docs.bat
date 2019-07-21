@echo off
cd ../app/static/docs/
sphinx-build source\ . -a -E
cd ../../../tools