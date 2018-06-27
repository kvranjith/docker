node{
	def app
	def image = "8kmilesranjith/ubuntu:${env.BUILD_NUMBER}"
	agent any
	
	stage('clone git Repo'){
		checkout scm
	}
	stage('docker build'){
		sh("docker build -t ${image} .")
	}
    }