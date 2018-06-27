node{
	def app
	def image = "ubuntu"
	def repo = "8kmilesranjith"
		
	stage('clone git Repo'){
		checkout scm
	}
	stage('docker build'){
		
		app = docker build("${repo}/${image}")
	}
    }