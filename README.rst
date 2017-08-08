gbToFasta
==========================================================
Galaxy wrapper for UCSC tools gbToFasta and raToTab. Convert GenBank records to fasta, create TRIX index, and create table with coding regions information for each mRNA record.

gbToFasta
---------

gbToFaRa - Convert GenBank flat format file to an fa file containing
the sequence data, an ra file containing other relevant info and
a ta file containing summary statistics.

usage:
  gbToFaRa filterFile faFile raFile taFile genBankFile(s)
  where filterFile is definition of which records and fields
  use /dev/null if you want no filtering.

  $ gbToFaRa /dev/null gbfile.fa gbfile.ra gbfile.ta gbfile

raToTab
--------

* Create table with coding regions information for each mRNA record

  raToTab -cols=acc,cds gbfile.ra gbfile.cds


* Create TRIX index

 #. Create search index and metadata

    raToTab -cols=acc,def gbfile.ra gbfile.info

 #. Create TRIX index  

    ixIxx gbfile.info gbfile.ix gbfile.ixx

Source code:
============

http://hgdownload.cse.ucsc.edu/admin/exe/

Licence
-------
Please note that commercial download and installation of the Blat and In-Silico PCR software may be licensed through Kent Informatics (http://www.kentinformatics.com).
