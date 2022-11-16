def resistansi_total(rp1, rp2, rp3, rs1, rs2, rs3):
    """Mencari Resistansi Total Rangkaian Campuran """
    
    resistansi_total = (1/(1/rp1 + 1/rp2 + 1/rp3)) + rs1 + rs2 + rs3

    return resistansi_total