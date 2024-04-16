#!/bin/bash
echo -e "Please Wait... Make Sure This Is The \e[1mOriginal ROM\e[0m."
while IFS= read -r -d '' f; do
    if [ -f "$f" ] && [ -s "$f" ]; then
        echo -n "$(realpath "$f") - " >> output.ogfs
        sha256sum "$f" | awk '{print $1}' >> output.ogfs
    elif [ -f "$f" ]; then
        echo -e "\e[1;33mAn empty file was found: $f. Ignored the file.\e[0m"
    fi
done < <(find . -type f -print0)
echo -e "\e[32mAll Done!\e[0m"
sleep 5
exit
