import os

def delete_unmatched_files(source_dir, target_dir):
    # Get set of filenames in target directory (recursively)
    target_files = set()
    for root, _, files in os.walk(target_dir):
        for f in files:
            target_files.add(f)

    # Go through source directory and delete files not in target
    for root, _, files in os.walk(source_dir):
        for f in files:
            if f not in target_files:
                file_path = os.path.join(root, f)
                print(f"Deleting: {file_path}")
                os.remove(file_path)

# Example usage:
# delete_unmatched_files('/path/to/source', '/path/to/target')

if __name__ == "__main__":
    source_directory = 'data/test/ISBI2016_ISIC_Part1_Test_GroundTruth'
    target_directory = 'ISIC_sampling_8'
    delete_unmatched_files(source_directory, target_directory)