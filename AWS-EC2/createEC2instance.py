#! Create EC2 Instance 
import boto3
ec2 = boto3.resource('ec2')

# create a file to store the key locally
outfile = open('ec2-keypair.pem','w')

# call the boto ec2 function to create a key pair
key_pair = ec2.create_key_pair(KeyName='ec2-keypair')
# capture the key and store it in a file
KeyPairOut = str(key_pair.key_material)
print(KeyPairOut)
outfile.write(KeyPairOut)

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-003634241a8fcdec0',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='ec2-keypair'
 )