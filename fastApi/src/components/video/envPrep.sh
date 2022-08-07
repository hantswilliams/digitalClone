#bash file to set up the environment for the cloneVideo script
#run this file first
sudo apt-get update
sudo apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
pip install -r requirements.txt
cd checkpoints; wget --no-check-certificate --no-proxy https://nhit-public.s3.us-east-2.amazonaws.com/audio2head.pth.tar
cd checkpoints/; ls -l