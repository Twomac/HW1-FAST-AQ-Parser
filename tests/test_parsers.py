# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    
    for header, sequence in FastaParser("data/test.fa"):
        assert header.startswith("seq")
        assert all(base in "ACGT" for base in sequence) # suggestion from VScode
        assert len(sequence) > 0  # sequence should not be empty
    
    blank_fasta = FastaParser("tests/blank.fa")
    with pytest.raises(ValueError, match=f"File {blank_fasta.filename} had 0 lines."):
        header, sequence in FastaParser("tests/blank.fa")

    bad_fasta = FastaParser("tests/bad.fa")
    with pytest.raises(ValueError, match=f"Got an empty line for {bad_fasta.filename} @ line 2"):
        header, sequence in FastaParser("tests/bad.fa")


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    fasta_parser = FastaParser("data/test.fq")
    header, sequence = next(iter(fasta_parser)) # grab first item without setting up loop
    assert header is None


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    for header, sequence, quality in FastqParser("data/test.fq"):
        assert header.startswith("seq")
        assert all(base in "ACGT" for base in sequence)
        assert len(sequence) > 0  # sequence should not be empty
        assert len(quality) == len(sequence)  # quality string should match sequence length

        # Additional edge case tests can be added here as well, but not being asked for it 
        # nor were we provided bad example files.

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fastq_parser = FastqParser("data/test.fa")
    header, sequence, quality = next(iter(fastq_parser)) # grab first item without setting up loop
    assert header is None