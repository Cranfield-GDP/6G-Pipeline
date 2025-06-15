@echo off

:: Get the directory of the current script
set SCRIPT_DIR=%~dp0

:: Navigate to the project root directory (two levels up from the script's directory)
cd /d "%SCRIPT_DIR%..\.."

:: Print the current working directory to verify
echo Current directory: %cd%

:: Start the BubbleRAN FlexRIC
echo Starting the BubbleRAN FlexRIC...
docker compose -f docker-compose-ran-ue.yaml up br-flexric -d

:: Wait for 10 seconds
echo Waiting for 10 seconds...
timeout /t 10 /nobreak >nul

:: Start the OAI gNodeB
echo Starting the OAI gNodeB ...
docker compose -f docker-compose-ran-ue.yaml up oai-gnb -d

:: Wait for 10 seconds
echo Waiting for 10 seconds...
timeout /t 10 /nobreak >nul

:: Start the first UE
echo Starting the OAI NR UE 1 ...
docker compose -f docker-compose-ran-ue.yaml up oai-nr-ue-1 -d

:: Wait for 10 seconds
echo Waiting for 10 seconds...
timeout /t 10 /nobreak >nul

:: Start the second UE
echo Starting the OAI NR UE 2 ...
docker compose -f docker-compose-ran-ue.yaml up oai-nr-ue-2 -d

:: Wait for 10 seconds
echo Waiting for 10 seconds...
timeout /t 10 /nobreak >nul

echo Done!