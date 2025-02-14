#!/usr/bin/env python3
import subprocess
import pstats
import os
subprocess.run([
    'python3', '-m', 'cProfile', '-o', 'profile_results', 
    'financial_enhanced.py', 'CRWD', 'Basic Average Shares'
], check=True)
stats = pstats.Stats('profile_results')
stats.sort_stats('cumulative')


with open('pstats-cumulative.txt', 'w') as f:
    stats.stream = f
    stats.print_stats(5)
os.remove('profile_results')