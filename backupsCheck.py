from boto.s3.connection import S3Connection
buckets = ['bucketname1','bucketname2']
notcheck=['folder1', 'folder2']

key = ''
secret = ''

s3 = S3Connection(key, secret)


for bucket in buckets:
    print "=== Checking Bucket " + bucket + "==="
    s3Bucket = s3.get_bucket(bucket)
    bucketFolders = s3Bucket.list("","/")
    for bucketFolder in bucketFolders:
        if (not bucketFolder.name[:-1] in notcheck):
            print bucketFolder.name
            bucketFiles = s3Bucket.list( "","/" + bucketFolder.name )
    backupFiles = {}
    for file in bucketFiles:
        filenameParts = file.name.split(".")
        extensionPart = filenameParts[-1]
        extension = extensionPart.split(".")
        extension = extension[-1]
        filenameParts = file.name.split("." + extension)
        rootFileName = filenameParts[0]
        sequenceParts = extension.split('j')
        sequence = sequenceParts[-1]
        if(sequence in ['ps', 'pa']):
            sequence = 000;
           print "fileName: " + file.name + " root: " + rootFileName
        try:    
            backupFiles[rootFileName].append(sequence)
        except:
            backupFiles = []
            backupFiles[rootFileName].append(sequence)
        backupFiles.sort()
        backupFiles
         
        #else:
        #    print "Not checking folder: "
