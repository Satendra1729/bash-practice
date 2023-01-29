#!/bin/bash

allTestPassed=true

python_test_filename="test.py"

testResults=`python test.py | awk '(NR>1)'` 
IFS=$'\n'
for i in $testResults 
    do 
      testResult=`echo $i | awk -F, '{ print $2 }'`
      testName=`echo $i | awk -F, '{ print $1 }'`
      if [[ $testResult != "Pass" ]]
      then
          echo $testName " -> " $testResult
          allTestPassed=false
      else 
          echo $testName " -> " $testResult
      fi
    done

if [ $allTestPassed == false ]
then
    echo "Some Test has been faild."
    exit 1
fi