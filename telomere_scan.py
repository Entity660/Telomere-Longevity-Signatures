from Bio import SeqIO
import os

def run_immortality_pipeline(file_path):
    print(f"=== PIPELINE ACTIVE: EVALUATING {file_path} ===")
    
    total_reads = 0
    # Task A: Dual-Strand Telomere Motif Tracking
    telomere_matches = 0
    fwd_motif, rev_motif = "TTAGGG", "CCCTAA"
    
    # Task B: Homology/Alignment Tracking for Key Longevity Regulators
    # Scanning for core conserved consensus sequence targets in genomic reads
    p53_target = "GAACATGTCC"  
    mtor_target = "ATTGTTGCCA" 
    
    p53_matches = 0
    mtor_matches = 0

    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    with open(file_path, "r") as handle:
        for record in SeqIO.parse(handle, "fastq"):
            total_reads += 1
            seq = str(record.seq).upper()
            
            # Task A Scan
            if fwd_motif in seq or rev_motif in seq:
                telomere_matches += 1
                
            # Task B Scan
            if p53_target in seq:
                p53_matches += 1
            if mtor_target in seq:
                mtor_matches += 1
                
    print(f"\n[RESULTS - TOTAL READS: {total_reads}]")
    print(f"🧬 Telomeric Signatures Identified: {telomere_matches} ({(telomere_matches/total_reads)*100:.4f}%)")
    print(f"🛡️ Conserved p53 Homology Hits: {p53_matches} ({(p53_matches/total_reads)*100:.4f}%)")
    print(f"🔋 Conserved mTOR Homology Hits: {mtor_matches} ({(mtor_matches/total_reads)*100:.4f}%)")

if __name__ == "__main__":
    run_immortality_pipeline("SRR21824172_1.fastq")
