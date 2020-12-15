## README:  loops over labelled image directories and copies set amount 
##          of files to new directory

# image path home
s_path='/home/schenk/repos/german_char_recogniser/img/chars'
d_path='/home/schenk/repos/german_char_recogniser/img/chars_top500'

# loop over each label source dir
for label in $(ls -p $s_path | grep /)
do

    d_label_path=$d_path/$label
    s_label_path=$s_path/$label

    # if path exists print
    if [ -d "$d_label_path" ]; then
        echo "exists"
    # else make new one
    else
        echo "IS NOT a directory, making one"
        mkdir $d_label_path
    fi

    echo $d_label_path
    printf '\n\n'

    # loops over each file label dir
    # file in src path | where its not a directory | limited to 1000
    for file in $(ls -p $s_label_path | grep -v / | tail -500)
    do
        s_file="${s_label_path}${file}"
        cp $s_file $d_label_path$file
    done
done