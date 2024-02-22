#!/bin/bash
echo "Please Wait... Make Sure This Is The Original ROM."
while IFS= read -r -d '' f; do
    if [ -f "$f" ] && [ -s "$f" ]; then
        echo -n "$(realpath "$f") - " >> output1.txt
        sha256sum "$f" | awk '{print $1}' >> output1.txt
    elif [ -f "$f" ]; then
        echo "An empty file was found: $f. Ignored the file."
    fi
done < <(find . -type f -print0)
echo -e "\e[32mAll Done!\e[0m"
sleep 5
exit