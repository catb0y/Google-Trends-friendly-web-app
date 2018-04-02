# Google Trends web app
Built in Flask with Bootstrap, pytrends library.

# Move file from one AWS S3 bucket to another - in steps
1. Created AWS account and first S3 bucket(s), adveritychallenge and adveritychallenge2
2. Uploaded file (aws_file) to adveritychallenge (note: file is approximately 4GB, as my laptop could not handle bigger files -- it is from 2007 after all)
3. Downloaded AWS CLI through pip and configured my credentials with IAM using aws configure
4. In order to copy the file from the first bucket to the second, I synced the buckets with the command: aws s3 sync s3://adveritychallenge s3://adveritychallenge2. I found out that the sync command is most likely the most efficient way to do so through much research and agreement on the matter on StackOverflow.
5. This command prints copy: s3://adveritychallenge/aws_file to s3://adveritychallenge2/aws_file
6. See screenshots in folder /screenshots

![aws s3 buckets](https://raw.githubusercontent.com/catb0y/adverity_challenge/master/screenshots/aws1.png?token=AWY-elUbeok3R_wyuKyFLiFBBYD2kiunks5ay9cGwA%3D%3D)

__________________________________________________
![adveritychallenge folder](https://raw.githubusercontent.com/catb0y/adverity_challenge/master/screenshots/aws3.png?token=AWY-ejhpAUjeO-_nF1VzpuMH3j3JsRrsks5ay_J1wA%3D%3D)

__________________________________________________

![adveritychallenge2 folder](https://raw.githubusercontent.com/catb0y/adverity_challenge/master/screenshots/aws2.png?token=AWY-es9torxPrHON_oYmkCkaL9EvT98Cks5ay_JdwA%3D%3D)
