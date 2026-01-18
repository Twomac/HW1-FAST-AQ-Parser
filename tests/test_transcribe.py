# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)

import pytest

def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    dna_seq = "ACGTAAGT"
    rna_seq = transcribe(dna_seq)
    assert rna_seq == "UGCAUUCA"

    bad_seq = "ACGTXAGT"

    with pytest.raises(ValueError, match="Invalid nucleotide found: X"):
        transcribe(bad_seq)



def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    
    dna_seq = "ACGTAAGT"
    rna_seq = reverse_transcribe(dna_seq)
    assert rna_seq == "ACUUACGU"

    bad_seq = "ACGTXAGT"

    with pytest.raises(ValueError, match="Invalid nucleotide found: X"):
        reverse_transcribe(bad_seq)