!pip install python=3.6
!pip install Cython>=0.27.3
!pip install bottleneck>=1.2.1
!pip install numpy>=1.13.3
!pip install numexpr>=2.6.4
!pip install pytables
!pip install pandas==0.22.0
!pip install matplotlib>=2.2.0
!pip install networkx==2.1
!pip install scipy>=1.0.0
!pip install scikit-learn==0.19.2
!pip install jupyter
!pip install ipython
!pip install ipykernel
!pip install six
!pip install future
!pip install nose
!pip install coverage
!pip install pip
!pip install psycopg2
!pip install coveralls

!wget https://github.com/nilmtk/nilm_metadata/archive/master.zip#egg=nilm_metadata
!unzip master.zip
!cd nilm_metadata-master
!python setup.py install 
!cd ..
!rm -r nilm_metadata-master


!wget https://github.com/nilmtk/nilmtk/archive/master.zip#egg=nilmtk
!unzip master.zip
!cd nilmtk-master
!python setup.py install 
!cd ..
!rm -r nilmtk-master






!wget https://github.com/hmmlearn/hmmlearn/archive/ae1a41e4d03ea61b7a25cba68698e8e2e52880ad.zip#egg=hmmlearn
!unzip ae1a41e4d03ea61b7a25cba68698e8e2e52880ad.zip
!cd hmmlearn-ae1a41e4d03ea61b7a25cba68698e8e2e52880ad
!python setup.py install 
!cd ..
!rm -r hmmlearn-ae1a41e4d03ea61b7a25cba68698e8e2e52880ad

