while IFS= read -r line; do
    echo "a line: $line"
done < file
