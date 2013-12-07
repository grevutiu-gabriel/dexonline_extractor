Script for extracting Romanian word list from www.dexonline.ro

python3 dexonline_extractor.py <letter>

Files were generated with following script:

for i in {a..z};
do
python3 dexonline_extractor.py $i
git add $i
git commit -m "Add list of words begining with letter $i"
done

The following script for non-English character

for i in ă â î ș ț; do python3 dexonline_extractor.py $i; git add $i; git commit -m "Add list of words begining with letter $i"; done
