#! Create New EC2 Instance 
import boto3
client = boto3.client('ec2')


def main():
    ec2 = ec2.run_instances(
        ImageId = 'ami-003634241a8fcdec0'
        MinCount = 1,
        MaxCount = 1,
        InstanceType = 't2.micro',
        KeyName = 'ec2-keypair')







if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nok. bye!\n')
        exit()