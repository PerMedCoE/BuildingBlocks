#!/usr/bin/env bash
projectname=$1

rm -rf ${projectname}
./PlMaBoSS_2.0.pl ${projectname}.bnd ${projectname}.cfg
