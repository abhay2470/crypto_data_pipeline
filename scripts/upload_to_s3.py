import boto3
import os

BUCKET_NAME = "crypto-data-pipeline-abhay"

# Create S3 Client
s3 = boto3.client("s3")

# Current Folder
OUTPUT_FOLDER = r"E:\projects\real_time_crypto_pipeline\dags\output"
# Upload Files
for file_name in os.listdir(OUTPUT_FOLDER):

    if file_name.endswith(".csv"):

        local_file_path = os.path.join(OUTPUT_FOLDER, file_name)

        s3_file_path = f"raw/{file_name}"

        try:

            s3.upload_file(
                local_file_path,
                BUCKET_NAME,
                s3_file_path
            )

            print(f"Uploaded Successfully: {file_name}")

        except Exception as e:

            print(f"Upload Failed for {file_name}")
            print(e)