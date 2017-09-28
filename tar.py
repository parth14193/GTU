import tarfile



source_dir = 'test/'
output_filename= 'bkp.tar.gz'

def tar(source_dir,output_filename):
	tar = tarfile.open(output_filename,"w:gz")
	tar.add(source_dir)
	tar.close()
tar(source_dir,output_filename)


