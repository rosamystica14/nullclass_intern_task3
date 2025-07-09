import json
import csv

# Input and output files
input_file = r'C:/Users/rosaa/OneDrive/Documents/nullclass_intern_task3/archive/arxiv-metadata-oai-snapshot.json'
output_file = 'filtered_cs_papers.csv'

# Categories to keep
target_prefix = 'cs.'

# Open input and output
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    # Write CSV headers
    writer.writerow(['id', 'title', 'abstract', 'categories'])

    count = 0
    for line in infile:
        try:
            paper = json.loads(line)
            categories = paper.get('categories', '')
            if target_prefix in categories:
                writer.writerow([
                    paper.get('id', ''),
                    paper.get('title', '').strip(),
                    paper.get('abstract', '').strip(),
                    categories
                ])
                count += 1
            if count >= 5000:
                break  # Optional: stop after 5000 papers to keep output small
        except json.JSONDecodeError:
            continue

print(f"✅ Done! Saved {count} computer science papers to '{output_file}'.")
