name="Lab"
labTemp="tempLab"
labNum=1
while [[ -e "$name$labNum" ]] ; do
    let labNum++
done
name="$name$labNum"
mkdir "$name"
cp -r "$labTemp/." "$name"
