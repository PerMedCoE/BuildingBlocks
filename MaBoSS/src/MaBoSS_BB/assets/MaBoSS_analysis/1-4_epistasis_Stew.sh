#!/usr/bin/env bash
projectname=$1
other_args=$2

java -Xmx6000M -cp '/usr/local/jar/BiNoM.jar' fr.curie.BiNoM.pathways.MaBoSS.MaBoSSConfigurationFile -single ${other_args} -c ./${projectname}.cfg -b ./${projectname}.bnd
cp ./${projectname}.bnd ./${projectname}_mutants/
cd ${projectname}_mutants/
sed -i 's:../MaBoSS:MaBoSS:' run.sh
chmod 755 run.sh
echo "running MaBoSS instances"
./run.sh
cd ..
echo java -Xmx6000M -cp '/usr/local/jar/BiNoM.jar:/usr/local/jar/VDAOEngine.jar' fr.curie.BiNoM.pathways.MaBoSS.MaBoSSProbTrajFile -maketable -folder ${projectname}_mutants/ -prefix ${projectname} -out ${projectname}.xls
echo java -Xmx6000M -cp '/usr/local/jar/BiNoM.jar:/usr/local/jar/VDAOEngine.jar'  fr.curie.BiNoM.pathways.MaBoSS.MaBoSSProbTrajFile -normtable -table ${projectname}.xls
java -Xmx6000M -cp '/usr/local/jar/BiNoM.jar:/usr/local/jar/VDAOEngine.jar' fr.curie.BiNoM.pathways.MaBoSS.MaBoSSProbTrajFile -maketable -folder ${projectname}_mutants/ -prefix ${projectname} -out ${projectname}.xls
java -Xmx6000M -cp '/usr/local/jar/BiNoM.jar:/usr/local/jar/VDAOEngine.jar'  fr.curie.BiNoM.pathways.MaBoSS.MaBoSSProbTrajFile -normtable -table ${projectname}.xls
mkdir "${projectname}_epistasis"
mv ${projectname}_m* ${projectname}_n* ./${projectname}_epistasis/
mv ${projectname}.xls ./${projectname}_epistasis/
mv ${projectname}.xls.dat ./${projectname}_epistasis/
# cp ${projectname}_epistasis/${projectname}_norm.xls ./
