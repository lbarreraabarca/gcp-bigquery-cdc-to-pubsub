

pycodestyle src/
status=$(echo $?)
if [ ! $status -eq 0 ]
then
    exit 1
else
    exit 0
fi