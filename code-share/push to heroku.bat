REM push to heroku

set /p Input=Enter commit desc:

git add *
git commit -am "%Input%"
cd ..
git subtree push --prefix code-share heroku master
pause