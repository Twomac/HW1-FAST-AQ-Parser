# DNA -> RNA Transcription

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    # initialize empty list to store transcribed sequence
    transcribed_seq = []
    for nuc in seq:
        # validate nucleotide is one of the 4 allowed
        if nuc not in ALLOWED_NUC:
            raise ValueError(f"Invalid nucleotide found: {nuc}")
        transcribed_seq.append(TRANSCRIPTION_MAPPING[nuc])
    if reverse:
        transcribed_seq.reverse() # modify the list in place

    # convert list  to string and return
    return "".join(transcribed_seq)


def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    # transcribe takes care of validation and reversal
    return transcribe(seq, reverse=True)