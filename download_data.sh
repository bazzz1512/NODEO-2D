# Download the oasis dataset with indexes till 60 - first 2

rm -r data
mkdir data
cd data
wget https://surfer.nmr.mgh.harvard.edu/ftp/data/neurite/data/neurite-oasis.v1.0.tar

tar -xvf neurite-oasis.v1.0.tar
rm neurite-oasis.v1.0.tar
