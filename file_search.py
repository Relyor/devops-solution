import sys
import boto3

"""
    Checks if a specified S3 bucket exists.

    Parameters:
    - bucket_name (str): The name of the bucket to check.
    - s3_object (boto3.client): An instance of the S3 client.

    Returns:
    - bool: True if the bucket exists, False otherwise. Also prints a message if the bucket is not found.
"""
def does_bucket_exist(bucket_name, s3_object):
    is_present = False
    buckets = []

    # List all buckets
    aws_response = s3_object.list_buckets()

    # Output the bucket names
    for bucket in aws_response['Buckets']:
        buckets.append(bucket['Name'])
        if bucket_name == bucket['Name']:
            is_present = True

    if not is_present:
        print(f"Bucket {bucket_name} not found!")
        print(f"Existing buckets: {buckets}")

    return is_present

"""
    Retrieves filenames from an S3 bucket that contain a specified substring and have a .txt extension.

    Parameters:
    - bucket_name (str): The name of the S3 bucket to search.
    - substring (str): The substring to search for in the filenames.

    Returns:
    - list: A list of filenames (keys) that contain the substring and have a .txt extension.
            Returns None if the bucket does not exist.
"""
def get_filenames(bucket_name, substring):
    found_file_names = []

    # Create an S3 client
    s3 = boto3.client('s3')

    # Check if bucket exists
    if not does_bucket_exist(bucket_name=bucket_name, s3_object=s3):
        return None

    # List all objects in the specified S3 bucket
    list_obejcts_response = s3.list_objects_v2(Bucket=bucket_name)

    # Check if the bucket contains any objects (files or directories)
    if 'Contents' in list_obejcts_response:
        # Iterate through the objects in the bucket
        for object in list_obejcts_response['Contents']:
            # Parse the path to only take the file name
            file_name = str(object['Key']).split('/')[-1]
            # Check if the file name matches the substring and the extension is .txt
            if substring in file_name and file_name.endswith('.txt'):
                found_file_names.append(object['Key'])

    return found_file_names

###
# argv[1] is the S3 bucket name
# argv[2] is the searched substring
###
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python file_search.py <s3_bucket_name> <substring>")
    else:
        file_names = get_filenames(sys.argv[1], sys.argv[2])
        if file_names == []:
            print(f"Files which contain the key word: '{sys.argv[2]}' were not found in bucket '{sys.argv[1]}'.")
        elif file_names is None:
            print(f"Please check your bucket name. {sys.argv[1]} does not exist!")
        else:
            print(f"File that contain substring {sys.argv[2]} found: {file_names}")
