#! Create EC2 Instance 
import boto3
ec2 = boto3.resource('ec2')

outfile = open('ec2-keypair.pem','w')
key_pair = ec2.create_key_pair(KeyName='ec2-keypair')
KeyPairOut = str(key_pair.key_material)
print(KeyPairOut)
outfile.write(KeyPairOut)

instances = ec2.create_instances(
    ImageID='ami-003634241a8fcdec0'
    MinCount=1,
    MaxCount=2,
    InstanceType='t2.micro'
    KeyName='ec2-keypair'
)