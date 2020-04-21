FROM continuumio/anaconda3

RUN apt install -y git gcc g++

COPY get_genia_pubmed.py /home/

RUN cd home && \
    git clone https://github.com/ncbi-nlp/NegBio.git && \
    cd ../
ENV PYTHONPATH=/home/NegBio/:$PYTHONPATH

RUN git clone https://github.com/beringresearch/chexpert-labeler/ && \
    cd chexpert-labeler && \
    conda env create -f environment.yml

RUN python -m nltk.downloader universal_tagset punkt wordnet
RUN pip install bioc==1.1.dev3 bllipparser==2016.9.11 \
deprecation==2.0.6 docutils==0.13.1 \
packaging==18.0 pyparsing==2.3.0 pystanforddependencies==0.3.1

RUN python /home/get_genia_pubmed.py 

