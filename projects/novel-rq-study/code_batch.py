import json
import sys

def load_batch(batch_num):
    with open(f'uncoded_batch_{batch_num}.json', 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    batch_num = int(sys.argv[1])
    batch = load_batch(batch_num)
    print(f"Loaded batch {batch_num}: {len(batch)} posts")
    
    # Print first few posts for verification
    for post in batch[:3]:
        print(f"\nID: {post['id']}")
        print(f"Text: {post['text'][:100]}...")
