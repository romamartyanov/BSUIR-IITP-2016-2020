#!/usr/bin/env bash
python lab_1.py --code=vigener --mode=encode --input_file=text.txt --export_file=encoded.txt
echo "File encoded!"

python lab_1.py --code=vigener --mode=decode --input_file=encoded.txt --export_file=decoded.txt
echo "File decoded!"