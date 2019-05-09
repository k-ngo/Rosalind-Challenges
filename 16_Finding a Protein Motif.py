from urllib.request import urlopen
import re

def where_in_protein_is_motif(protein_id):
    url = 'http://www.uniprot.org/uniprot/' + protein_id + '.fasta'
    with urlopen(url) as f:
        data = f.read().decode('utf-8', 'ignore')
    data = data.split('\n', 1)
    data = ''.join(data[1].split('\n'))
    # Check for motif at *each and every* index
    # i.e., don't skip checking index when a match is found because matches might overlap.
    motif = re.compile(r'(?=(N[^P][ST][^P]))') # N-glycosylation motif
    matches = re.findall(motif, data)
    print('Protein ID:', protein_id)
    print('Protein Sequence:', data)
    print('Matches:', matches)
    indices = [i.start(0) + 1 for i in re.finditer(motif, data)]
    # With regards to above:
    # Adding 1 to each index is purely done so the answers will match
    # with the 1-based indexing format used by Rosalind.
    # There would be no point to doing it otherwise.
    print('Index Locations:', indices)
    return indices


result = []

with open('rosalind_mprt.txt', 'r') as f:
    input = f.read().split('\n')

for i in input:
    result.append([i, where_in_protein_is_motif(i)])
    print()

print('Results:', '-'*20, sep = '\n')
for line in result:
    if line[1] != []:
        print(line[0], ' '.join(map(str, line[1])), sep = '\n')

# References:
# https://stackoverflow.com/questions/1393324/in-python-given-a-url-to-a-text-file-what-is-the-simplest-way-to-read-the-cont
# https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2
# https://www.w3schools.com/python/python_regex.asp
# https://stackoverflow.com/questions/5616822/python-regex-find-all-overlapping-matches
# https://stackoverflow.com/questions/2674391/python-locating-the-position-of-a-regex-match-in-a-string/16360404
# https://stackoverflow.com/questions/3765024/different-behavior-between-re-finditer-and-re-findall
