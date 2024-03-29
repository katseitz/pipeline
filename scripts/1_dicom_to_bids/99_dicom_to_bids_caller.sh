#!/usr/bin/bash

#SBATCH -A p31833
#SBATCH -p normal
#SBATCH -t 1:00:00
#SBATCH --mem=1G
#SBATCH -J tran_1


DIR=$1 #check if $ needed. 
echo $DIR
SUB=$2
echo $SUB
SES=$3
echo $SES
#Pipeline calls, one after another. 
source /projects/b1108/studies/transitions2/scripts/1_dicom_to_bids/1_dic_to_nifti.sh $DIR $SUB $SES
python /projects/b1108/studies/transitions2/scripts/1_dicom_to_bids/2_nifti_to_bids_naming.py $SUB $SES
source /projects/b1108/studies/transitions2/scripts/1_dicom_to_bids/3_deface.sh $SUB $SES





