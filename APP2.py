import streamlit as st
from Bio import Entrez, SeqIO
import pandas as pd


# Set email address for Entrez
Entrez.email = "vincent.peta@usd.edu"

# Define function to fetch protein sequences
def fetch_protein_sequence(protein_name):
    handle = Entrez.esearch(db="protein", term=protein_name, retmax=200)
    record = Entrez.read(handle)
    handle.close()
    protein_ids = record["IdList"]
    protein_records = []
    for protein_id in protein_ids:
        handle = Entrez.efetch(db="protein", id=protein_id, rettype="fasta", retmode="text")
        protein_record = SeqIO.read(handle, "fasta")
        protein_records.append(protein_record)
        handle.close()
    return protein_records

# Set up Streamlit app
st.title("Protein Sequence Fetcher")

# Get user input
protein_name = st.text_input("Enter a protein name:")

# Fetch protein sequences and display in table
if st.button("Fetch protein sequences"):
    protein_records = fetch_protein_sequence(protein_name)
    if protein_records:
        st.write("Found the following protein sequences:")
        for protein_record in protein_records:
            st.write(protein_record.format("fasta"))
    else:
        st.write("No protein sequences found.")


