import boto3


def upload_file_to_s3(file_path, bucket_name, object_name):
    # Create an S3 client
    s3_client = boto3.client("s3")

    # Upload the file
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File uploaded successfully to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Upload failed: {e}")


def download_file_from_s3(bucket_name, object_name, file_path):
    # Create an S3 client
    s3_client = boto3.client("s3")

    # Download the file
    try:
        s3_client.download_file(bucket_name, object_name, file_path)
        print(f"File downloaded successfully to {file_path}")
    except Exception as e:
        print(f"Download failed: {e}")


# Example usage
upload_file_to_s3("local_file.txt", "my-bucket", "remote_file.txt")
