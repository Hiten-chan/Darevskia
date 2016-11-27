import re

#enter the list of the desired genes!!!
genes = []

#enter the name of the organism in Latin
organisms = []

from Bio import Entrez as e
e.email = 'hidemi-chan@mail.ru'

from Bio import SeqIO as s

for gene in genes:
    print('GENE!', gene)
    for orgn in organisms:
        print(orgn)
        query = orgn + '[Orgn] AND ' + gene + '[Gene]'
        hnd = e.esearch(db='gene', term=query)
        record = e.read(hnd)
        hnd = e.elink(dbfrom='gene', db='nucleotide', id=record['IdList'][0], linkname='gene_nuccore_refseqrna')
        record = e.read(hnd)   
        nuc_id = record[0]["LinkSetDb"][0]["Link"][0]["Id"]
        hnd = e.efetch(db='nucleotide', id=nuc_id, rettype='fasta', retmode='text')
        seq = hnd.read()
        #If necessary, change the name of the output file (Default: genes_1)
        with open('genes_1' + '.fa', 'a') as ofile:
            ofile.write(seq.strip() + '\n')
