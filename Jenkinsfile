node{
	def app
	def image = "8kmilesranjith/ubuntu:${env.BUILD_NUMBER}"
		
	stage('clone git Repo'){
		checkout scm
	}
	stage('docker build'){
		sh("docker build -it ${image}.")
	}
    }