#! Create New EC2 Instances
import boto3
ec2 = boto3.resource('ec2')

def main():
    CreateEC2()
    print("EC2 instance created")
    for instance in ec2.instances.all():
        print(instance.id, instance.image.id)
    userInput = input('Delete Instance? Enter Instance ID ')
    DeleteEC2(userInput)

    
def CreateEC2():
    ec2.create_instances (
        ImageId = 'ami-003634241a8fcdec0',
        MinCount = 1,
        MaxCount = 1,
        InstanceType = 't2.micro',
        KeyName = 'ec2-keypair')   
    
    
def DeleteEC2(InstanceID):
        instance = ec2.Instance(InstanceID)
        print(instance.terminate()) 
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nok. bye!\n')
        exit()




