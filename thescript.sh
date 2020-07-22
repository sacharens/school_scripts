#!/bin/bash
DIR=~/Documents/school/project/results/
cd $DIR/STAR-2.7.5a/bin/Linux_x86_64/
# making the genom directory 
./STAR --runMode genomeGenerate --genomeFastaFiles $DIR/GCF_000241465.1_ASM24146v1_genomic.fna --genomeDir $DIR/genom --sjdbGTFfile $DIR/GCF_000241465.1_ASM24146v1_genomic.gtf --runThreadN 1 --genomeSAindexNbases 10
COUNT=0
for file in `ls $DIR/fastq`; do
	let "COUNT += 1"
	./STAR  --readFilesIn $DIR/fastq/$file --outFileNamePrefix $DIR/output$COUNT --genomeDir $DIR/genom --runThreadN 1 --outSAMtype BAM Unsorted --quantMode GeneCounts --alignIntronMax 1 --genomeSAindexNbases 10 
	echo "star $COUNT end"
	echo $file
	cd ~
	python -m HTSeq.scripts.count -f bam -q -m union -s yes  -i gene_id  "$DIR"output"$COUNT"Aligned.out.bam $DIR/GCF_000241465.1_ASM24146v1_genomic.gtf  > $DIR/HTSeq/all"$COUNT".counts
	cd $DIR/STAR-2.7.5a/bin/Linux_x86_64/
done
